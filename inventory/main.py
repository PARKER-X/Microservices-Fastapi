from fastapi import FastAPI
from .schema import Product

app = FastAPI()


@app.get('/products')
def all():
    return Product.all_pks()
