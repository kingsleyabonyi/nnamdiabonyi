#a progrram that checks for leap year

year = int(input("WHat year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print("This is not a leap year")
    else:
        print(f"{year} is a leap year")

else:
    print("This is not a leap year!")
