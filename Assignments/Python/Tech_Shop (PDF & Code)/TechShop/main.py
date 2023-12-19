from services.product_manager import ProductManager

p1 = ProductManager()
a = p1.list_all_products()
for x in a:
    print(x.get_product_id())