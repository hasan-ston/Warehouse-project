import bcrypt

SYMBOLS = "!.@#$%^&*()_[]"

def sign_up():
    users_file = "users.csv"

    # Load all ID's
    existing_ids = []
    try:
        with open(users_file, "r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                if len(parts) >= 1:
                    existing_ids.append(parts[0])
    except:
        # file/users don't exist
        pass

    print("\n--- Create account ---")

    userid = input("Enter user ID: ").strip()
    if userid == "":
        print("Enter valid user ID")
        return None

    if userid in existing_ids:
        print("User ID already exists")
        return None

    password = input("Enter password: ").strip()
    confirm = input("Confirm password: ").strip()

    if password != confirm:
        print("Passwords don't match.")
        return None

    # Basic password checks
    if len(password) < 6:
        print("Password must be at least 6 characters.")
        return None

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for c in password:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
        elif c in SYMBOLS:
            has_symbol = True

    if not (has_upper and has_lower and has_digit and has_symbol):
        print("Password must have uppercase, lowercase, digit, and symbol.")
        print(f"Allowed symbols: {SYMBOLS}")
        return None

    # Hash password
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    # Append new user
    with open(users_file, "a") as f:
        f.write(userid + "," + hashed + "\n")

    print("Account creation successful.")
    return userid
