from Common.qarm_interface_wrapper import QArmInterface, BarcodeScanner
from time import sleep
import bcrypt

scan_barcode = BarcodeScanner.scan_barcode
# SIGN UP

SYMBOLS = "!.@#$%^&*()_[]"

def sign_up():
    filename = "users.csv"

    # Load existing IDs
    existing_ids = []
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 1:
                    existing_ids.append(parts[0])
    except:
        pass  # file does not exist yet

    print("\n--- Create Account ---")
    userid = input("Enter user ID: ").strip()
    if userid == "":
        print("Enter valid user ID.")
        return None    # authenticate() is responsible for looping

    if userid in existing_ids:
        print("User ID already exists.")
        return None

    password = input("Enter password: ").strip()
    confirm = input("Confirm password: ").strip()

    if password != confirm:
        print("Passwords don't match.")
        return None

    if len(password) < 6:
        print("Password must be at least 6 characters.")
        return None

    has_upper = has_lower = has_digit = has_symbol = False
    for c in password:  # looping through each character
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
        elif c in SYMBOLS:
            has_symbol = True

    if not (has_upper and has_lower and has_digit and has_symbol):
        print("Password must include uppercase, lowercase, digit, and symbol.")
        print(f"Allowed: {SYMBOLS}")
        return None
    # Hashed password(password + random salt). Decode converts bytes to string so it can be stored in CSV
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    # Append new user
    with open(filename, "a") as f:
        f.write(userid + "," + hashed + "\n")

    print("Account created.")
    return userid


# AUTHENTICATION

def authenticate():
    print("\n--- Login ---")
    user_file = "users.csv"

    users = []
    try:
        with open(user_file, "r") as f: # f is a variable name
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 2:
                    users.append(parts) # new row
    except:
        users = []

    if len(users) == 0:
        print("No users exist.")
        create = input("Create account? (y/n): ").lower()
        if create == "y":
            return sign_up()
        return None

    have = input("Do you have an account? (y/n): ").lower()
    if have != "y":
        return sign_up()

    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        userid = input("User ID: ").strip()
        password = input("Password: ").strip()

        found = False

        for row in users:
            if row[0] == userid:
                found = True
                stored_hash = row[1]

                # This takes users pswd converts to bytes, takes the stored hash converts to bytes, and compares the two
                if bcrypt.checkpw(password.encode(), stored_hash.encode()): # returns True or False based on if the pswd matches
                    print("Login successful.\n")
                    return userid

                print("Incorrect password.")
                break

        if not found: # user doesnt exist
            print("User not found.")

        attempts += 1 # Only after an unsuccessful login attempt does it increment attempts
        left = max_attempts - attempts
        if left > 0:
            print(f"{left} attempt(s) left.")

        print("Exceeded max attempts.")
        action = input("retry / signup / exit: ").lower().strip()

        if action == "retry":
            continue
        elif action == "signup":
            return sign_up()
        else:
            return None

# LOOKUP PRODUCTS

def lookup_products(products):
    items = products.split(",")
    items = [p.strip() for p in items]

    matched = []
    with open("products.csv", "r") as filename:
        lines = filename.readlines()

    for item in items:
        found = False

        for line in lines:
            if item.lower() in line.lower():
                parts = line.strip().split(",")
                name = parts[0].strip()
                try:
                    price = float(parts[1])
                except:
                    price = None
                matched.append([name, price])
                found = True
                break

        if not found:
            print("The product was not found in file")

    return matched


# PACK PRODUCTS

def pack_products(product_list):
    arm = QArmInterface(1)
    arm.home()

    for item in product_list:
        product_name = item[0]
        current = product_name.strip().lower()

        print(f"Packing {current}...")

        # SPONGE
        if 'sponge' in current:
            arm.rotate_gripper(180)
            arm.rotate_gripper(-35)

            arm.rotate_base(19)
            arm.rotate_elbow(-12)
            arm.rotate_shoulder(47)
            arm.rotate_gripper(80)
            arm.rotate_shoulder(-50)

            arm.home()
            arm.rotate_base(-52)
            sleep(1)
            arm.rotate_elbow(40)
            sleep(1)
            arm.rotate_shoulder(20)
            sleep(1)
            arm.rotate_gripper(-50)

            arm.home()

        elif 'bottle' in current:

            arm.rotate_gripper(180)
            arm.rotate_gripper(-20)

            arm.rotate_base(11)
            arm.rotate_elbow(-11)
            arm.rotate_shoulder(46)
            arm.rotate_gripper(80)
            arm.rotate_shoulder(-46)

            arm.home()
            arm.rotate_base(-52)
            sleep(1)
            arm.rotate_elbow(40)
            sleep(1)
            arm.rotate_shoulder(20)
            sleep(1)
            arm.rotate_gripper(-50)

            arm.home()

        elif 'rook' in current:
            arm.rotate_gripper(180)
            arm.rotate_gripper(-35)

            arm.rotate_base(5)
            arm.rotate_elbow(-8)
            arm.rotate_shoulder(46)
            arm.rotate_gripper(80)
            arm.rotate_shoulder(-46)

            arm.home()
            arm.rotate_base(-52)
            sleep(1)
            arm.rotate_elbow(40)
            sleep(1)
            arm.rotate_shoulder(20)
            sleep(1)
            arm.rotate_gripper(-50)

            arm.home()

        elif 'd12' in current:
            arm.rotate_gripper(180)
            arm.rotate_gripper(-30)

            arm.rotate_base(-4.6)
            arm.rotate_elbow(-7)
            arm.rotate_shoulder(47)
            arm.rotate_gripper(70)
            arm.rotate_shoulder(-45)

            arm.home()
            arm.rotate_base(-52)
            sleep(1)
            arm.rotate_elbow(40)
            sleep(1)
            arm.rotate_shoulder(20)
            sleep(1)
            arm.rotate_gripper(-50)

            arm.home()

        elif 'bowl' in current:
            arm.rotate_gripper(180)
            arm.rotate_gripper(-25)

            arm.rotate_base(0)
            arm.rotate_elbow(-10)
            arm.rotate_shoulder(45)
            arm.rotate_gripper(75)
            arm.rotate_shoulder(-43)

            arm.home()
            arm.rotate_base(-52)
            sleep(1)
            arm.rotate_elbow(40)
            sleep(1)
            arm.rotate_shoulder(20)
            sleep(1)
            arm.rotate_gripper(-50)

            arm.home()

        elif 'witch' in current or 'hat' in current:
            arm.rotate_gripper(180)
            arm.rotate_gripper(-30)

            arm.rotate_base(-11)
            arm.rotate_elbow(-5)
            arm.rotate_shoulder(49)
            arm.rotate_gripper(70)
            arm.rotate_shoulder(45)

            arm.rotate_base(-52)
            sleep(1)
            arm.rotate_elbow(40)
            sleep(1)
            arm.rotate_shoulder(20)
            sleep(1)
            arm.rotate_gripper(-50)

            arm.home()

        else:
            print(f"Warning: No packing sequence defined for '{product_name}'")
            continue

        print(f"{product_name} packed successfully")

    arm.end_arm_connection()
    print("\nAll products packed successfully")


# COMPLETE ORDER
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


# CUSTOMER SUMMARY

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

# MAIN

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

    pack_products(product_list)
    complete_order(userid, product_list)
    customer_summary(userid)

main()
