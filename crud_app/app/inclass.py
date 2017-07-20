menu = """
    Hi. Welcome.

    There are 100 products.

    Please choose an operation:

    'List', 'Show', 'Create', 'Update', 'Destroy' or 'Done'

"""

chosen_operation = input(menu)

if chosen_operation.title() == "List":
    print ("LISTING PRODUCTS")
elif chosen_operation.title() == "Show":
    print ("SHOWING A PRODUCT")
elif chosen_operation.title() == "Create":
    print ("CREATING A PRODUCT")
elif chosen_operation.title() == "Update":
    print ("UPDATING A PRODUCT")
elif chosen_operation.title() == "Destroy":
    print ("DESTROYING A PRODUCT")
else:
    ("Unrecognized Operation. Please choose one of: 'List', 'Show', 'Create', 'Update', or 'Destroy'")
