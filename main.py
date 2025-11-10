from functions import customer_summary, complete_order, authenticate, lookup_products, scan_barcode, pack_products


def main():
    print(f"Welcome!")
    userid = input("Enter your id: ")

    user_input = input("Would you like to fill an order? (y/n): ").lower()
        if user_input == "n":
            break
    
    while not authenticate(userid):
        print("Invalid ID. Please try again.")
        userid = input("Enter your id: ")
        
    product_list = []

    while True:
        barcode = scan_barcode()
        product = lookup_products(barcode)

        if product:
            product_list.append(product)

        else:
            print("No products found.")
        
    pack_products(product_list)
    complete_order(userid, product_list)
    customer_summary(userid)

