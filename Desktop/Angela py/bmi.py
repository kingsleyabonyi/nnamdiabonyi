#a program that checks for a bmi calculator
weight = float(input("Enter a digit in m: "))
height = float(input("Enter a digit in kg: "))

bmi = round(weight/height**2)
if bmi < 18.5:
    print(f"your bmi is {bmi} you are underweight") 
elif bmi > 18.5:
    print(f"your bmi is {bmi} you have a normal weight")
elif bmi > 25:
    print(f"your bmi is {bmi} and you are over weight")
elif bmi < 30:
    print(f"your bmi is {bmi} and you are obssed")
elif bmi > 35:
    print(f"your bmi is {bmi} and you are clinically obese")
else:
    print("you do not match with any category")