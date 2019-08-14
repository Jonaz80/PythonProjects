from sys import argv


try:
    a, b = argv[1:]
    a = float(a)
    b = float(b)

    print(f"using input {len(argv)} values ...")
except:
    print("failed to use your numbers")
    a = 6
    b = 7

if a * b == 42:
    print(f"trying {a} * {b}!")
    print("DA rocks")
elif a + b == 42:
    print("trying {a} + {b}!")
    print("That sums it up micely, you are genius")
else:
    print("give up now :-p")
