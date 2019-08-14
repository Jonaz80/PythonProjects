my_name = "Jon C Shaw"
my_age = -50
my_height = 1.9 # m
my_weight = 78 # Kg
my_eyes = 'Green'
my_teeth = 'White'
my_hair = 'Mousy brown'

#with substituted variables there is no padding front or back, hence spaces at front
print(f"Let's talk about {my_name}.")
print(f"He's {my_height}m tall.")
print(f"He's {my_weight}Kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")


# calculate BMI - a tricky line
BMI = round(my_weight / my_height**2,1)
print(f"{my_name} has a BMI of {BMI}. The normal range is 18.5 to 24.9.")
