import random

def complete_order(userid, product_list):
    subtotal=0
    for name,price in product_list:
        subtotal += price

    discount_percent = random.randint(5,50)
    discount_amt = subtotal*(discount_percent/100)

    tax_amt = (subtotal-discount_amt)*0.13

    total = subtotal - discount_amt + tax_amt

    #Formatted Receipt
    print("-" * 50)
    print(f"User ID: {userid}")
    print("-" * 50)
    print(f"{'Items':<25}{'Price':>{25}}")
    print("-" * 50)
    for name, price in product_list:
        print(f"{name:<25}{('$' + format(price, '.2f')):>{25}}")
    print("-" * 50)
    print(f"{'Subtotal:':<25}{('$' + format(subtotal, '.2f')):>{25}}")
    print(f"{('Discount (' + str(discount_percent) + '%):'):<25}{('$' + format(discount_amt, '.2f')):>{25}}")
    print(f"{'Tax (13%):':<25}{('$' + format(tax_amt, '.2f')):>{25}}")
    print(f"{'Total:':<25}{('$' + format(total, '.2f')):>{25}}")
    print("-" * 50)

    #Write into File
    file=open("orders.csv","a")
    write= userid+","+ "{:.2f}".format(total)
    for name,price in product_list:
        write+=","+name
    write+="\n"
    file.write(write)
    file.close()