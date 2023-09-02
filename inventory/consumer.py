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
        # print(results)

        if results !=[]:
            for result in results:
                obj = result[1][0][1]
                product = Product.get(obj['product_id'])
                print(product)
                product.quantity = product.quantity-int(obj['quantity'])
                product.save()
    except Exception as e:
        print(str(e))
