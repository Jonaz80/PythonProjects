def add(a,b):
    print(f"Adding {a} to {b}")
    return a + b

def subtract(a, b):
    print(f"subtracting {b} from {a}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some maths with custom functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

input("That becomes: what? Can you do it by hand?\n Press any key to get the answer.")
print(f"The answer is ...{what}!")

print("Add strings in a function :\n", add('Jon', ' Shaw') )
