from .rediss import redis
from redis_om import HashModel

class Order(HashModel):
    product_id:str
    price:float
    fee:float
    total:float
    quantity:int
    status:str

    class Meta:
        database = redis

#Hashmodel docs = https://github.com/redis/redis-om-python/blob/main/docs/models.md