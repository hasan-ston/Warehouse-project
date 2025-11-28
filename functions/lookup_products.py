def lookup_products(products):
    items = products.split(",")
    items = [p.strip() for p in items]

    matched = []
    with open("products.csv","r") as filename:
        lines = filename.readlines()

    for item in items:
        found = False

        for line in lines:
            if item.lower() in line.lower():
                parts = line.strip().split(",")
                name = parts[0]
                try:
                    price = float(parts[1])
                except:
                    price = None
                matched.append([name,price])
                found = True
                break

        if not found:
            print("The product was not found in file")

    return matched
