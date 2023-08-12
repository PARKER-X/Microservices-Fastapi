from fastapi import FastAPI
from .schema import Product
from fastapi.middleware.cors import CORSMiddleware
from .rediss import redis

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://localhost:3000'],
    allow_methods = ['*'],
    allow_headers=['*']
)
redis.set('test' ,'hello world')
print(redis.get('test'))



redis.set('test' ,'hello world')
print(redis.get('test'))

product = Product(
        name="Parker",
        price=100,
        quantity=100
    )

product.save()
print(product.pk)

@app.get('/products')
def all():
    return Product.all_pks()

# @app.post('/products', response_model=None)
# def create(product: Product):
#     product = Product(
#         name="Parker",
#         price=100,
#         quantity=100
#     )
#     return product.save()
    
@app.post('/products',response_model=Product)
def create(product: Product):
    return product.save()