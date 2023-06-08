print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

initial = input("Would you want to travel abroad? Yes or No ")
initial_small = initial.lower()
if initial == "Yes":
    print("congratulations!")
else:
    ("Keep trying")
second_prompt = input("How would you want to travel? Air or road ")
second_prompt_small = second_prompt.lower()
if second_prompt == "Air":
    print("You are on the right place, good to go!")
else:
    print("Check out for the available air plane.")
third_prompt = input("Where do you want do want to travel? Europe, America or Asia ")
third_prompt_small = third_prompt.lower()
if third_prompt == "europe":
    print("Welcome to the european world, You Win!")
elif third_prompt == "america":
    print("Welcome to the United States, You win!")
elif third_prompt == "asia":
    print("Welcome to Asian world, You win!")
else:
    print("Keep trying your are close!")