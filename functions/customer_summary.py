import os
from collections import Counter


def customer_summary(userid):
    """
    Reads orders.csv and prints a professional summary of all previous
    orders for the given userid:
        - number of orders
        - total spent
        - count of each unique product ordered
    """
    if not os.path.exists("orders.csv"):
        print("No orders found for this user.")
        return

    order_count = 0
    total_spent = 0.0
    product_counts = Counter()

    with open("orders.csv", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) < 2:
                continue

            file_userid = parts[0].strip()
            if file_userid != str(userid).strip():
                continue

            order_count += 1

            # total cost is second field
            try:
                total_spent += float(parts[1])
            except ValueError:
                pass

            # remaining fields are product names
            for name in parts[2:]:
                name = name.strip()
                if name:
                    product_counts[name] += 1

    if order_count == 0:
        print("No orders found for this user.")
        return

    width = 50
    print("\n" + "=" * width)
    print(f"{'CUSTOMER SUMMARY':^{width}}")
    print("=" * width)
    print(f"User ID: {userid}")
    print(f"Number of orders: {order_count}")
    print(f"Total spent: ${total_spent:,.2f}")
    print("-" * width)

    print(f"{'Product':<30}{'Quantity':>20}")
    print("-" * width)

    for name, qty in sorted(product_counts.items()):
        print(f"{name:<30}{qty:>20}")

    print("=" * width + "\n")
