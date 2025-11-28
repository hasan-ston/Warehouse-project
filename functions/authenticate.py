import bcrypt
from .sign_up import sign_up


def authenticate():
    print("\n--- Login ---")

    user_file = "users.csv"

    # Try to load users
    users = []
    try:
        with open(user_file, "r") as f: # f is a variable name
            for line in f:
                line = line.strip() # remove '\n' and white spaces
                if line == "": # if there are empty lines, skip over them
                    continue
                parts = line.split(",") # split the line by commas
                if len(parts) >= 2:
                    users.append(parts) # new row
    except:
        # No users/files
        users = [] # remains empty

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
                    stored_hash = row[1] # 2nd column

                    #This takes users pswd converts to bytes, takes the stored hash converts to bytes, and compares the two
                    if bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8")): # returns True or False based on if the pswd matches
                        print("Login successful!\n")
                        return userid

                    print("Incorrect password.")
                    break

            attempts += 1 # Only after an unsuccessful login attempt does it increment attempts

            if not found: # user doesnt exist
                print("User not found.")

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
