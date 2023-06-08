print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is her name? \n")

name1_lower = (name1.lower())
name2_lower = (name2.lower())

t1 = (name1.count("t"))
r1 = (name1.count("r"))
u1 = (name1.count("u"))
e1 = (name1.count("e"))
true_1 = t1 + r1 + u1 + e1 

t2 = (name2.count("t"))
r2 = (name2.count("r"))
u2 = (name2.count("u"))
e2 = (name2.count("e"))

true_2 = t2 + r2 + u2 + e2

total_true = true_1 + true_2

l1 = (name1.count("L"))
o1 = (name1.count("o"))
v1 = (name1.count("v"))
e3 = (name1.count("e"))

love_1 = l1 + o1 + v1 + e3

l2 = (name2.count("L"))
o1 = (name2.count("o"))
v1 = (name2.count("v"))
e4 = (name2.count("e"))
love_2 = l2 + o1 + v1 + e4
total_love = love_1 + love_2

True_love = int(str(total_true) + str(total_love))
if True_love < 10 and True_love > 90 :
    print(f"Your score is {True_love}, you go like coke and mentos")
elif True_love <= 40 or True_love >= 45 :
    print(f"Your score is {True_love}, you are alright together!")
else:
    print(f"Your score is {True_love}")





