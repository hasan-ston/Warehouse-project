import bcrypt
from .sign_up import sign_up


def authenticate():
    print("\n--- Login ---")

    user_file = "users.csv"

    # Try to load users
    users = []
    try:
        with open(user_file, "r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                if len(parts) >= 2:
                    users.append(parts)
    except:
        # No users/files
        users = []

    # No user account
    if len(users) == 0:
        print("No users registered.")
        make = input("Create account? (y/n): ").lower().strip()
        if make == "y":
            return sign_up()
        return None

    have = input("Do you have an account? (y/n): ").lower().strip()
    if have != "y":
        print("Redirecting to sign up...")
        return sign_up()

    attempts = 0
    max_attempts = 3

    while True:
        while attempts < max_attempts:
            userid = input("User ID: ").strip()
            password = input("Password: ").strip()

            found = False

            for row in users:
                if row[0] == userid:
                    found = True
                    stored_hash = row[1]

                    if bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8")):
                        print("Login successful!\n")
                        return userid
                    break

            attempts += 1

            if not found:
                print("User not found.")
            else:
                print("Password incorrect.")

            left = max_attempts - attempts
            if left > 0:
                print(f"{left} attempt(s) remaining.")

        print("Exceeded maximum attempts.")
        action = input("retry / signup / exit: ").lower().strip()

        if action == "retry":
            attempts = 0
        elif action == "signup":
            return sign_up()
        else:
            return None