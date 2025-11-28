import csv

def customer_summary(userid):

    with open ("orders.csv", "r", userid) as file:
        reader = csv.reader(file)
        orders = [row for row in reader if row[0] == userid]

    while len(orders) == 0:
            print(f"No orders found for {userid}. Scan products to start an order.")
            return scan_barcode()

    total_orders = len(orders)
    total_spent = sum(float(order[1]) for order in orders)

    unique_products = {}
    for order in orders:
        for product in order[2:]:
            unique_products[product] = product_counts.get(product, 0) + 1

    """Old Code Nonfunctional

    total_orders = 0
    total_spent = 0.00
    unique_products = 0

    for i in range(len(orders.csv)):

        total_orders = len(orders.csv[1])

        if total_orders == 0:
            print(f"No orders found for {userid}. Scan products to start an order.")
            return scan_barcode()

        else:

            while len(orders.csv) > 0:
                total_orders += 1
                total_spent += len(orders.csv[2])
                unique_products += """

    # Add some colour
    print("\n" + "="*55)
    print(f" 📦 Summary of Orders for {userid} 📦 ".center(55))
    print("="*55)
    print(f" ➕ Total Orders: {total_orders} ➕ ")
    print(f" 💰 Total Spent: ${total_spent:,.2f } 💰 ")
    print("-"*55)
    print(f"{'Product':<35}{'Amount Ordered':>10}")
    print("-"*55)

    for product, count in product_counts.items():
        print(f"{product:<30}{count:>10}")

    print("="*50)
    print("Customer Summary Complete.\n")


## Test Cases

print(customer_summary(userid))
