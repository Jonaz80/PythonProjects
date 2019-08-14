
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# no args
def print_none():
    print("I got nothing.")

print_two('Jon','Shaw')
print_two_again('Jon','Shaw')
print_one('Melody')
print_none()
