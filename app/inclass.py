import csv

products = []

csv_file_path = "data\products.csv"
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

menu = """
    Hi. Welcome.

    There are {0} products.

    Please choose an operation:

    'List', 'Show', 'Create', 'Update', 'Destroy' or 'Done'

""".format(len(products))

other_path = "data\other_products.csv"
with open(other_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
    writer.writeheader()
    for product in products:
        writer.writerow(product)

chosen_operation = input(menu).title()

def list_products():
    print ("Listing products")
def show_products():
    print ("Showing a product")
def create_products():
    print ("Creating a product")
def update_products():
    print ("Updating a product")
def destroy_products():
    print ("Destroying a product")

if chosen_operation == "List":
    list_products()
elif chosen_operation == "Show":
    show_products()
elif chosen_operation == "Create":
    create_products()
elif chosen_operation == "Update":
    update_products()
elif chosen_operation == "Destroy":
    destroy_products()
else:
    print ("Unrecognized Operation. Please choose one of: 'List', 'Show', 'Create', 'Update', or 'Destroy'")
