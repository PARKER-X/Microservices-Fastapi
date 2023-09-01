from fastapi import FastAPI
# from .schema import Product
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