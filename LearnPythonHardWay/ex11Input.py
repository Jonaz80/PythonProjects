name = input("Hi, I will calculate your BMI, please enter your name? ")
print("how old are you?", end=' ')
age = input()
print("How tall are you in meters?", end=' ')
height = float(input())
print("How much do you weigh in kg?", end=' ')
weight = float(input())
BMI = round(weight / height**2 , 2)

print(f"{name} with a height of {height} and a weight of {weight} gives you a BMI of {BMI}")
