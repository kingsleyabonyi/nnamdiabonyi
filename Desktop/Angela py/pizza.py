#a program that orders for pizza according to customers demands

print("Welcome to python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M, or L  ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_small = 2
pepperoni_ML = 3
extra_cheese = 1
bill = 0

if size == "S":
    bill += small_pizza
elif size == "M":
    bill += medium_pizza
else:
    bill += large_pizza
if add_pepperoni == "Y":
    if size == "S":
        bill += pepperoni_small
    else:
        bill += pepperoni_ML
if extra_cheese == "Y":
    bill += extra_cheese
print(f"You total bill is ${bill}")

