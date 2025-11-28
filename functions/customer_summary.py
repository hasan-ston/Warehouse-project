import csv

def customer_summary(userid):

    with open ("orders.csv", "r") as file:
        reader = csv.reader(file)
        orders = [row for row in reader if row[0] == userid]

    if not orders:
        print(f"No orders found for {userid}.")
        return None

    total_orders = len(orders)
    total_spent = sum(float(order[1]) for order in orders)

    product_counts = {}
    for order in orders:
        for product in order[2:]:
            product_counts[product] = product_counts.get(product, 0) + 1

    # Add some colour
    print("\n" + "="*55)
    print(f" 📦 Summary of Orders for {userid} 📦 ".center(55))
    print("="*55)
    print(f" ➕ Total Orders: {total_orders} ➕ ")
    print(f" 💰 Total Spent: ${total_spent:,.2f} 💰 ")
    print("-"*55)
    print(f"{'Product':<35}{'Amount Ordered':>10}")
    print("-"*55)

    for product, count in product_counts.items():
        print(f"{product:<30}{count:>10}")

    print("="*50)
    print("Customer Summary Complete.\n")

