import csv

products = []

csv_file_path = "data\products.csv"
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

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
    print(product)

def show_output(user_input_id):
    user_input_id = input("Okay. Please specify the product's identifier: ")
    matching_product = [product for product in products if product["id"] == user_input_id]
    return matching_product [0]
    product_show = show_output(user_input_id)
    print ("Showing a product")
    print (product_show)

def create_output():
    print ("Creating a product")
    product_name = input("Hey what do you want to name the new product")
    new_product = {
        "id": len(products) + 1,
        }

if user_input == "List":
    list_output()
elif user_input == "Show":
    show_output(user_input_id)
elif user_input == "Create":
    create_output()
elif user_input == "Update":
    print ("Updating a product")
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
