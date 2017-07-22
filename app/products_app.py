import csv

products = []

csv_file_path = "data\products.csv"
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(dict(row))

print ("-" * 30)
print ("PRODUCT APPLICATION")
print ("-" * 30)
print ("Welcome Lee's CRUD Application!\n")
print ("There are {0} products in the database. Please select an operation:".format(len(products)))
print ("")

print ("   operation | description")
print ("   --------- | ------------------------------------------------")
print ("   'List'    | Display a list of product identifiers and names.")
print ("   'Show'    | Show information about a product.")
print ("   'Create'  | Add a new product.")
print ("   'Update'  | Edit an existing product.")
print ("   'Destroy' | Delete an existing product.")
print (" ")

user_input = input()
user_input = user_input.title()

def list_output():
    print ("Listing products")
    print (" + THERE ARE " + str(len(products)) + " PRODUCTS")
    for product in products:
        print (" + " + str(product))

def show_output():
    show_input_id = input("Okay. Please specify the product's identifier: ")
    matching_product = [product for product in products if product["id"] == show_input_id][0]
    print ("Showing a product")
    print (matching_product)

def create_output():
    print ("Creating a product")
    product_name = input("What is the name?: ")
    product_aisle = input("What is the aisle?: ")
    product_department = input("what is the department?: ")
    product_price = input("What is the price? (just write the number): ")
    new_product = {
        "id": len(products) + 1,
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price
        }
    print("New product is: ", new_product)
    products.append(new_product)

def update_output ():
    update_input_id = input("Okay, Please specify the product's identifier: ")
    product = [product for product in products if product["id"] == update_input_id][0]
    print ("The product is: " + str(product))
    update_product_name = input ("Change its name from " + product["name"] + " to: ")
    update_product_aisle = input ("Change its aisle from " + product["aisle"] + " to: ")
    update_product_department = input ("Change its name from " + product["department"] + " to: ")
    update_product_price = input ("Change its name from " + product["price"] + " to: ")
    updated_product = {
        "id": int(product["id"]),
        "name": update_product_name,
        "aisle": update_product_aisle,
        "department": update_product_department,
        "price": update_product_price
    }
    product.update(updated_product)
    print ("Updating product here!")
    print (product)


if user_input == "List":
    list_output()
elif user_input == "Show":
    show_output()
elif user_input == "Create":
    create_output()
elif user_input == "Update":
    update_output()
elif user_input == "Destroy":
    print ("Destroying a product")
else:
    print ("Unrecognized Operation. Please choose one of the recognized operations.")


other_path = "data\other_products.csv"
with open(other_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
    writer.writeheader()
    for product in products:
        writer.writerow(product)
