def add_product(inventory, product, qty):
    inventory[product] = qty


def update_product(inventory, product, qty):
    if product in inventory:
        inventory[product] += qty
    else:
        print("Product not found")


def check_product(inventory, product):
    return inventory.get(product, "Not found")


def show_inventory(inventory):
    for product in inventory:
        print(product, ":", inventory[product])


# main program
inventory = {}

add_product(inventory, "apple", 10)
add_product(inventory, "banana", 5)

update_product(inventory, "apple", 5)

print(check_product(inventory, "apple"))
print(check_product(inventory, "mango"))

show_inventory(inventory)