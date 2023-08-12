from .rediss import redis
from redis_om import HashModel

class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis
    

