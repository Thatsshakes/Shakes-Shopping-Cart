#SHOPPING CART LOGIC LAYER

import tkinter as tk

def add_item(cart, name, price, qty):
    for item in cart:
        if item["name"] == name:
            item["qty"] += qty
            return cart
    
    cart.append({"name": name, "price": price, "qty": qty})
    return cart


def remove_item(cart, name):
    for item in cart:
        if item["name"] == name:
            cart.remove(item)
            break

    return cart


def cart_total(cart):
    total = 0

    for item in cart:
        total += item["price"] * item["qty"]

    return total


def apply_discount(total, percent):
    discount = total * (percent/100)

    return total - discount


# print(apply_discount(4500, 10))


#Test cases
cart = []
cart = add_item(cart, "Rice", 1500, 2)
cart = add_item(cart, "Beans", 800, 1)
cart = add_item(cart, "Rice", 1500, 1)

print(f"Total: {cart_total(cart)}")


cart = remove_item(cart, "Beans")
print(f"Total: {cart_total(cart)}")



