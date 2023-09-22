from .schema import Order
from .rediss import redis

key = 'refund_order'
group = "payment-group"

try:
    redis.xgroup_create(key,group)
except:
    print('Group Already present!')

while True:
    try:
        results = redis.xreadgroup(group,key)
        # print(results)

        if results !=[]:
            for result in results:
                obj = result[1][0][1]
                order = Order.get(obj['pk'])
                order.status='refunded'
                order.save()
                # print(order)
                
    except Exception as e:
        print(str(e))
