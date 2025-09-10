# A console based project
#Name, price, category
products  = [
    ("Apple", 200, "Fruits"),
    ("Banana", 100, "Fruit"),
    ("Bread", 250, "Bakery"),
    ("Milk", 500, "Dairy"),
    ("Cheese", 800, "Dairy"),
    ("Eggs", 600, "Protein"),
    ("Rice", 1200, "Grain"),
    ("Chicken", 2500, "Meat"),
] 
cart = {}
#function to display product
def show_product():
    print("\n Availiable Product")
    for index,(name, price,category) in enumerate (products, start=1):
        print(f"{index}-{name}- ₦{price}-({category})")
show_product()

#Add Item To Cart
def add_item():
    while True:
        int(input("\nEnter a product"))
        