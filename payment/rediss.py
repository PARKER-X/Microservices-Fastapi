#Redis Database for paymnet api
from redis_om import get_redis_connection,Migrator
from inventory.credientals import credientials


redis = get_redis_connection(
    host = "redis-14652.c264.ap-south-1-1.ec2.cloud.redislabs.com",
    port ="14652",
    password = credientials,
    decode_responses = True
    
)

Migrator().run()
