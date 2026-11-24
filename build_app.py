#SHOPPING CART LOGIC LAYER

import tkinter as tk

def add_item(cart, name, price, qty):
    output = {}
    

    for product, value in cart.items():
        output[product] = value


    if int(qty) > 0:
    
        if name in output:
            output[name]["qty"] *= int(qty)
            output[name]["price"] += price

        else:
            output[name] = {"price" : price, "qty" : int(qty)}

    # total = 0
    # for total_index in output.values():
    #     total += total_index["price"] * total_index["qty"]

    return output


cart = {"Rice" : {"price" : 1500,
    "qty" : 3
}}

print(add_item(cart, "Rice", 1500, 2))
print(add_item(cart, "Beans", 800, 1))
print(add_item(cart, "Rice", 1500, 1))



def remove_item(cart, name):
    output = {}

    for product, value in cart.items():
        if product != name:
            del output[name]

    return output

# print(remove_item(cart, "Beans"))