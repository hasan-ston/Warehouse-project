def pack_products(product_list):
    if len(product_list) == 0:
        print("No products to pack")
        return

    for product in product_list:
        current = product[0]
        print(f"Packing {current}")


pack_products(product_list)