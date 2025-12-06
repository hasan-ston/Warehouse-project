# Warehouse Processing System

An automated warehouse management system made in Python.

## Overview

This system handles user authentication, product scanning, robotic arm packing operations, order processing, and customer order tracking. It integrates with a QArm robotic interface to physically pack orders scanned by users.

## Features

- **Secure Authentication**: User signup and login with bcrypt password encryption
- **Barcode Scanning**: User product barcodes to add items to orders
- **Automated Packing**: QArm robotic arm automatically performs a number of sequences to pick up different products.
- **Order Processing**: Calculates subtotals, discounts, tax, and generates a well formatted receipt
- **Customer Tracking**: View order history and product stats for every user

## System Workflow

1. User logs in or creates an account
2. Scan product barcodes to build order
3. System looks up products from inventory
4. QArm packs each item automatically
5. Receipt generated with discount and tax
6. Order saved to file
7. Customer summary displays order history

## Team

- Muhammad Hasan - Authentication, packing sequences
- Abdullah Makhdoom - Product lookup, packing sequences
- Ciara Doody - Customer summary, packing sequences
- Maggie Seto - Order completion, packing sequences

## File Structure

- `users.csv` - Stores user credentials (userid, hashed_password)
- `products.csv` - Product inventory (name, price)
- `orders.csv` - Order history (userid, total, products...)
