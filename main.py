def main():
  print(f"Welcome!")
  userid=input("Enter your id: ")
  authenticate(userid) #do we need this
  while not authenticate(userid):
    userid=input("Enter your id: ")
    autheticate(userid)  

  while not lookup_products(scan_barcode()):
    lookup_products(scan_barcode())
  pack_products(lookup_products(scan_barcode())
  
  print(scan(barcode))
  print

# Other Team's Code
# !/usr/bin/env python3
# coding: utf-8
# --------------------------------------------------------------------------------

import sys

sys.path.append("../")

from time import sleep
from Common.qarm_interface_wrapper import *

GRIPPER_IMPLEMENTATION = 1
arm = QArmInterface(GRIPPER_IMPLEMENTATION)
scan_barcode = BarcodeScanner.scan_barcode

# --------------------------------------------------------------------------------
# STUDENT CODE BEGINS
# ---------------------------------------------------------------------------------

arm.home()
'''
##Level 1
arm.rotate_base(17)
sleep(1)
arm.rotate_elbow(-12)
sleep(1)
arm.rotate_shoulder(46)
sleep(5)

##Level 2
arm.home()
arm.rotate_base(9)
sleep(1)
arm.rotate_elbow(-12)
sleep(1)
arm.rotate_shoulder(46)
sleep(5)

##Level 3
arm.home()
arm.rotate_base(3)
sleep(1)
arm.rotate_elbow(-12)
sleep(1)
arm.rotate_shoulder(46)
sleep(5)

arm.home()
arm.rotate_base(-3)
sleep(1)
arm.rotate_elbow(-10)
sleep(1)
arm.rotate_shoulder(46)
sleep(5)

##Level 4
arm.home()
arm.rotate_base(-9)
sleep(1)
arm.rotate_elbow(-9)
sleep(1)
arm.rotate_shoulder(46)
sleep(5)

arm.home()
arm.rotate_base(-17)
sleep(1)
arm.rotate_elbow(-12)
sleep(1)
arm.rotate_shoulder(46)
sleep(5)

##Package
arm.home()
arm.rotate_base(-52)
sleep(1)
arm.rotate_elbow(40)
sleep(1)
arm.rotate_shoulder(20)
sleep(1)
'''

arm.rotate_gripper(30)
arm.rotate_gripper(-30)


##Code V1
"""arm.home()
arm.rotate_gripper(100)
sleep(2)

arm.rotate_base(16)
sleep(1)
arm.rotate_elbow(-12)
sleep(1)
arm.rotate_shoulder(30)

arm.rotate_shoulder(16)

arm.rotate_gripper(-80)
sleep(5)
arm.rotate_shoulder(-16)


arm.home()
arm.rotate_base(-52)
sleep(1)
arm.rotate_elbow(40)
sleep(1)
arm.rotate_shoulder(15)
arm.rotate_gripper(40)
sleep(1)
arm.rotate_gripper(-60)
sleep(1)"""

##V2
# !/usr/bin/env python3
# coding: utf-8
# --------------------------------------------------------------------------------

import sys

sys.path.append("../")

from time import sleep
from Common.qarm_interface_wrapper import *

GRIPPER_IMPLEMENTATION = 1
arm = QArmInterface(GRIPPER_IMPLEMENTATION)
scan_barcode = BarcodeScanner.scan_barcode

# --------------------------------------------------------------------------------
# STUDENT CODE BEGINS
# ---------------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox

def lookup_products(products):
    """Checks scanned products to ensure they exist in products.csv. Takes a comma-separated list of products, outputs warning message if product not found, and returns 2D list of products and prices found."""

    #products = products_input.get()
    file = open("products.csv")

    available_products = []
    for line in file:
        available_products.append(line.strip().split(","))
        available_products[len(available_products)-1][1] = float(available_products[len(available_products)-1][1])
    file.close()

    requested_products = products.split()
    ordered_products = []

    #products_input.set("")

    found = False
    for i in range(len(requested_products)):
        for j in range(len(available_products)):
            if requested_products[i].lower() == available_products[j][0].lower():
                ordered_products.append(available_products[j])
                found = True
                break
        if not found:
            print(f"Warning: {requested_products[i]} not found")
            #warning['text'] += f"\nWarning: {requested_products[i]} not found"
        found = False

    return ordered_products

def complete_order(userid, product_list):

    subtotal = 0
    for name, price in product_list:
        subtotal += price

    discount_percent = random.randint(5, 50)
    discount_amount = subtotal * (discount_percent / 100)
  
    tax_rate = 0.13
    tax_amount = (subtotal - discount_amount) * tax_rate

    total = subtotal - discount_amount + tax_amount

    # Print Reciept
    print("\n" + "="*40)
    print(f"USER ID: {userid}".ljust(30))
    print("-"*40)
    print("ITEMS".ljust(20) + "PRICE".rjust(20))
    print("-"*40)
    for name, price in product_list:
        print(f"{name.ljust(20)}${price:>19.2f}")
    print("-"*40)
    print(f"{'SUBTOTAL'.ljust(20)}${subtotal:>19.2f}")
    print(f"{'DISCOUNT ('+str(discount_percent)+'%)'.ljust(20)}-${discount_amount:>19.2f}")
    print(f"{'TAX (13%)'.ljust(20)}${tax_amount:>19.2f}")
    print(f"{'TOTAL'.ljust(20)}${total:>19.2f}")
    print("="*40)

    file = open("orders.csv", "a")
    line_to_write = userid + "," + "{:.2f}".format(total)
    for name, price in product_list:
        line_to_write += "," + name
    line_to_write += "\n"

    file.write(line_to_write)
    file.close()
    file = open("orders.csv", "r")
    lines = file.readlines()
    file.close()

    # Count orders for userid
    for line in lines:
        if line.strip() == "":
            continue
        parts = line.strip().split(",")
        if parts[0] == userid:
            orders_count += 1

    print(f"\nYou have placed {orders_count} order(s) so far.\n")

def pack_products(products):
    item = ""
    for i in range(len(products)):
        item = products[i][0].lower()
        if item == "sponge":
            arm.home()
            arm.rotate_gripper(100)
            sleep(2)

            arm.rotate_base(16)
            sleep(1)
            arm.rotate_elbow(-12)
            sleep(1)
            arm.rotate_shoulder(30)

            arm.rotate_shoulder(16)

            arm.rotate_gripper(-80)
            sleep(5)
            arm.rotate_shoulder(-16)
        elif item == "bottle":
            pass
            #grab bottle
        elif item == "rook":
            pass
            #grab rook
        elif item == "D12":
            pass
            #grab D12
        elif item == "witchhat":
            pass
            #grab witch hat
        else:
            pass
            #grab bowl

        item = products[i][0]

        print(f"{item} packed.")
        # drop item in box and go to home position
        arm.home()
        arm.set_arm_position([0.21161152424323046, -0.2666089332338263, 0.13969975241913885])
        arm.rotate_gripper(-60)
      
print("Welcome!")
#userid = authenticate()
keep_ordering = input("Enter N to quit. Enter anything else to make another order")
while keep_ordering.upper() != "N":
    product_list = BarcodeScanner.scan_barcode()
    products = lookup_products(product_list)
    pack_products(products)
    #complete_order(userid, products)
    keep_ordering = input("Enter N to quit. Enter anything else to make another order")
#customer_summary(userid)

arm.end_arm_connection()
arm.home()
sleep(1)
arm.rotate_base(30)
sleep(1)
arm.rotate_elbow(30)
sleep(1)
arm.rotate_shoulder(15)
arm.end_arm_connection()


