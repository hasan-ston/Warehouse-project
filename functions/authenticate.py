def authenticate():
    """
        Logs the user in by validating userid and password against users.csv.
        If user doesn't have an account, calls sign_up() first.

        Returns:
            userid (string): The authenticated user's ID
        """

    print("Login")

    # Check if user has an account
    has_account = input("Do you have an account? (y/n): ")

    if has_account.lower() != 'y':
        print("Redirecting to sign_up()")
        sign_up()

    # Authentication loop
    while True:
        userid = input("User ID: ")
        password = input("Password: ")

        # Check credentials
        authenticated = False

        with open('users.csv', 'r') as file:
            reader = csv.reader(file)

            for row in reader:

                if row[0] == userid:
                    # Decrypt and compare
                    stored_password = simple_decrypt(row[1])
                    if password == stored_password:
                        print("Login successful!")
                        return userid
