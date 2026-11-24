#SHOPPING CART WINDOW LAYER

import tkinter as tk

root = tk.Tk()              #main window
root.title("Shakes Shopping Cart")
root.geometry("300x150")


#SHOPPING CART LOGIC LAYER

def add_item(cart, name, price, qty):
    label.config(text="Button clicked!")

    for item in cart:
        if item["name"] == name:
            item["qty"] += qty
            return cart
    
    cart.append({"name": name, "price": price, "qty": qty})
    return cart
    
#widgets
label = tk.Label(root, texr="Hello, Tkinter!")
label.pack(pady=15)

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

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



#Test cases
cart = []
cart = add_item(cart, "Rice", 1500, 2)
cart = add_item(cart, "Beans", 800, 1)
cart = add_item(cart, "Rice", 1500, 1)

print(f"Total: {cart_total(cart)}")


cart = remove_item(cart, "Beans")
print(f"Total: {cart_total(cart)}")


final_total = apply_discount(cart_total(cart), 10)
print(f"Total after discount: {final_total}")



