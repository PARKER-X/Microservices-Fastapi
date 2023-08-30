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
print(product.name)

@app.get('/products')
def all():
    return Product.all_pks()

    
@app.post('/products')
async def create(product: Product):
    print(product)
    return product.save()