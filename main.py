from functions import customer_summary, complete_order, authenticate, lookup_products, pack_products,sign_up

import sys
from time import sleep
sys.path.append("../")

from functions import authenticate, lookup_products, pack_products, complete_order, customer_summary
# to test
# try:
#     from Common.qarm_interface_wrapper import BarcodeScanner
#
#     scan_barcode = BarcodeScanner.scan_barcode
# except ImportError:

def scan_barcode():
    print("\n--- Read to Scan ---")
    barcode_data = input("Scan barcode (enter product names): ").strip()
    return barcode_data


def main():
    print("-" * 60)
    print(" " * 10 + "Warehouse Processing System")
    print(" " * 8 + "Design Studio - 1P13 Project")
    print("-" * 60)

    # authenticate() returns userid
    userid = authenticate()

    if not userid:
        print("Authentication cancelled. Exiting system.")
        return

    # Product scanning and lookup
    product_list = []

    print("-" * 60)
    print(f"Order session active for user: {userid}")
    print("-" * 60)

    keep_ordering = True
    while keep_ordering:
        barcode_data = scan_barcode()

        if not barcode_data:
            print("Please scan again.")
            continue

        # Look up products from barcode scan
        products = lookup_products(barcode_data)

        if products:
            product_list.extend(products)
            print(f"Added {len(products)} item(s) to order")
            print(f"Current total: {len(product_list)} item(s)")
        else:
            print("No valid products found from scan.")

        # does the user want to continue?
        continue_input = input("\nScan another barcode? (y/n): ").lower().strip()
        if continue_input != 'y':
            keep_ordering = False

    # Process order if products were scanned
    if not product_list:
        print("\nNo products in order. Exiting system.")
        return

    print(f"\n{'-' * 60}")
    print(f"Processing order with {len(product_list)} product(s)...")
    print(f"{'-' * 60}")

    # Pack products using Q-Arm
    pack_products(product_list)

    # Complete order
    complete_order(userid, product_list)

    # Display customer summary
    customer_summary(userid)

    print("\nThank you for using the Warehouse Processing System!")
    print("-" * 60)


if __name__ == "__main__":
    main()
