# Imports
from fastapi import FastAPI
from .schema import Order
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks
from .rediss import redis
from starlette.requests import Request
import requests



# APP
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://localhost:3000'],
    allow_methods = ['*'],
    allow_headers=['*']
)

# Checking Redis connection 
redis.set('test' ,'hello world')
print(redis.get('test'))


@app.get('/orders/{pk}')
def get(pk:str):
    # order = Order.get(pk)
    # redis.xadd('refund_order',order.dict(),'*')
    return Order.get(pk)


@app.post('/orders')
async def create(request:Request,background_tasks=BackgroundTasks):
    body = await request.json()
    req = requests.get('https://localhost:8000/products/%s' %body['id'])
    product = req.json()

    order =  Order(
        product_id=body["id"],
        price = body["price"],
        fee = 0.2 * body["price"],
        total = 1.2 * body["price"],
        quantity = body["quantity"],
        status = 'pending'
    )
    
    order.save()

    # Background Task :-> (function,parameter)
    background_tasks(order_completed,order)

    # Instead of background Task
    # Order Call
    # order_completed(order)
    return order


def order_completed(order:Order):
    order.status = "completed"
    order.save()
    redis.xadd('order_completed',order.dict(),'*')  # * for auto generated id and xadd is redis stream functionality to add adds a new entry to a stream.

