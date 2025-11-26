import csv
import os
import hashlib
import secrets


def sign_up():
    """
    Creates a new user with a unique ID and secure password.
    Updates users.csv with encrypted password.
    Returns: None
    """
    users_file = 'users.csv'

    # Initialize file if it doesn't exist
    if not os.path.exists(users_file):
        with open(users_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['userid', 'password_hash', 'salt'])

    print("\n=== User Registration ===")
    userid = input("Enter desired user ID: ").strip()

    # Check if userid already exists
    existing_ids = set()
    if os.path.exists(users_file):
        with open(users_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_ids.add(row['userid'])

    if userid in existing_ids:
        print(f"Error: User ID '{userid}' already exists.")
        return

    password = input("Enter password: ")
    confirm_pwd = input("Confirm password: ")

    if password != confirm_pwd:
        print("Error: Passwords do not match.")
        return

    # Generate salt and hash password
    salt = secrets.token_hex(16)
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000).hex()

    # Append to CSV
    with open(users_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([userid, pwd_hash, salt])

    print(f"User '{userid}' registered successfully!\n")