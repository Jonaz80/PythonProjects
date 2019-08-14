print("counting chickens...")

print("Hens", 25+30/6)
# comment
"""
PEMDAS which stands for Parentheses Exponents Multiplication Division Addition Subtraction. That's the order Python follows as well. The mistake people make with PEMDAS is to think this is a strict order, as in "Do P, then E, then M, then D, then A, then S." The actual order is you do the multiplication and division (M&D) in one step, from left to right, then you do the addition and subtraction in one step from left to right. So, you could rewrite PEMDAS as PE(M&D)(A&S)
"""
print("Roosters", 100-25*3 % 4)
# % modulus - the remainder of the division is returned
# in this example order is 25*3=75, 75%4 = 3, 100-3=97

print("Now counting eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 +2 < 5 - 7?")
print(3 + 2 < 5 - 7)

print("What is  3 + 2?", 3+2)
print("What is 5-7?", 5-7)


print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
