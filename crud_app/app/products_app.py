
print ("-" * 30)
print ("PRODUCT APPLICATION")
print ("-" * 30)
print ("Welcome Lee's CRUD Application!\n")
print ("There are " + str(len(products) + " products in the database. Please select an operation:\n")

print ("   operation | description")
print ("   --------- | ------------------------------------------------")
print ("   'list'    | Display a list of product identifiers and names.")
print ("   'show'    | Show information about a product.")
print ("   'Create'  | Add a new product.")
print ("   'Update'  | Edit an existing product.")
print ("   'Destroy' | Delete an existing product.")

menu = """
    Hi. Welcome.

    There are 100 products.

    Please choose an operation:

    'List', 'Show', 'Create', 'Update', 'Destroy' or 'Done'

"""

while True:
    user_input = input(menu) # withouth if statement, infinite loop
    if user_input.title() == "List":
        print ("Listing products")
        print (" + THERE ARE 20 PRODUCTS")
        print (products)
    elif user_input.title() == "Show":
        user_input_id = input("Okay. Please specify the product's identifier: ")
        print ("Showing a product")
    elif user_input.title() == "Create":
        print ("Createing a product")
    elif user_input.title() == "Update":
        print ("Updating a product")
    elif user_input.title() == "Destroy":
        print ("Destroying a product")
    elif user_input.title() == "Done":
        break
    else:
        print ("Unrecognized Operation. Please choose one of the recognized operations.")
