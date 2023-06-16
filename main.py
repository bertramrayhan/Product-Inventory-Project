"""The "Product Inventory Project" aims to create an application that manages an inventory of products. It involves two main components: the Product class and the Inventory class.

Product Class:

The Product class represents an individual product in the inventory.
It typically has attributes such as price, ID, and quantity on hand.
You can define methods within the class to perform operations on the product, such as updating the quantity, calculating the total value, or displaying product information.
Inventory Class:

The Inventory class manages the collection of products in the inventory.
It keeps track of various products and their quantities.
You can define methods within the class to perform operations on the inventory, such as adding a new product, removing a product, calculating the total value of the inventory, or displaying the inventory status.
To implement the project, you would typically:

Define the Product class:

Include attributes to store information about the product, such as price, ID, and quantity.
Implement methods to perform operations on the product, such as updating quantity, calculating value, or displaying information.
Define the Inventory class:

Create a data structure (e.g., a list or dictionary) to store the products in the inventory.
Implement methods to add products to the inventory, remove products, calculate the total value of the inventory, or display inventory information.
By using these classes, you can create instances of products, add them to the inventory, and perform various operations on the inventory.

The purpose of this project is to simulate an inventory management system where you can keep track of products, update their quantities, calculate their values, and manage the overall inventory."""



class Product:
  def __init__(self, price : int, product_id : str, quantity : int):
    if not isinstance(price, int) or price < 0: #check if price is int or price is more than 0
      raise ValueError("Price must be a positive number")
    self.price = price
    self.product_id = product_id.lower()
    
    if not isinstance(quantity, int) or quantity < 0: #check if quantity is int or quantity is more than 0
      raise ValueError("quantity must be more than 0")
    self.quantity = quantity
    

  def store(self): #storing product info to put into Inventory class
    return {"product_id" : self.product_id, "price" : self.price, "quantity" : self.quantity}
    

  def __repr__(self): #makes the product info more readable
    return f"Product ID : {self.product_id}, Price : {self.price}, Quantity : {self.quantity}"


class Inventory: #storing product info
  products = []

  def add_product(self, product_info : list): #storing product to products
    Inventory.products.append(product_info)

  def remove_product(self, product : str):
    for item in Inventory.products:
      if item["product_id"] == product.lower():
        Inventory.products.remove(item)
        break
    else:
      print("Product not found")
  

  def change_quantity(self, product : str, quantity_change : int): #change the quantity of a product
    for item in Inventory.products:
      if item["product_id"] == product.lower():
        item["quantity"] += quantity_change
        break
    else:
      print("Product not found")

  def is_available(self, product : str): #check if a product available or not
    for item in Inventory.products:
      if item["product_id"] == product.lower():
        if item["quantity"] == 0:
          return f"Product {product} is Empty"
        elif item["quantity"] > 0:
          return f"Product {product} is Available"
        else:
          return "Product not found"

  def product_info(self, product : str):
    for item in Inventory.products:
      if item["product_id"] == product.lower():
        product_info = item
        break
    else:
      return "Product not found"
  
    return f"Product ID : {product_info['product_id']}, Price: {product_info['price']}, Quantity : {product_info['quantity']} "

  def calculate(self, product : str):
    for item in Inventory.products:
      if item["product_id"] == product.lower():
        return f'The price is {item["quantity"] * item["price"]}'
    else:
      return "Product not found"

# Testing the code

# Create an inventory
inventory = Inventory()

# Add some products
product1 = {"product_id": "p1", "price": 10, "quantity": 5}
product2 = {"product_id": "p2", "price": 20, "quantity": 3}
product3 = {"product_id": "p3", "price": 15, "quantity": 8}

inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)

# Display the inventory
print("Inventory:")
print(inventory.products)
print()
# Remove a product
inventory.remove_product("p2")
print()
# Display the updated inventory
print("Updated Inventory:")
print(inventory.products)
print()
# Change quantity of a product
inventory.change_quantity("p1", 2)
print()
print("Change quatity of a product")
print(Inventory.products)
print()
# Check product availability
print("Product Availability:")
print(inventory.is_available("p1"))  # Available
print(inventory.is_available("p2"))  # Empty
print(inventory.is_available("p3"))  # Available
print(inventory.is_available("p4"))  # Not found
print()
# Get product info
print("Product Info:")
print(inventory.product_info("p1"))  # Product ID: p1, Price: 10, Quantity: 7
print(inventory.product_info("p2"))  # Product not found
print(inventory.product_info("p3"))  # Product ID: p3, Price: 15, Quantity: 8