# a program that calculatees the average student height from list of height

student_height = input("Input a list of student heights ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)
highest_score = 0
for score in student_height:
    if score > highest_score:
        highest_score = score
print(f"The highest score is {score}")