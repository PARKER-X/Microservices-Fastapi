from .schema import Product
from .rediss import redis

key = 'order_completed'
group = "inventory-group"

try:
    redis.xgroup_create(key,group)
except:
    print('Group Already present!')

while True:
    try:
        results = redis.xreadgroup(group,key)
        print(results)
    except Exception as e:
        print(str(e))
