def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    return True


num = '212-444-2343'
print(num + ' is a phone number: ' + str(isPhoneNumber(num)))

num = '01473 711436'
print(num + ' is a phone number: ' + str(isPhoneNumber(num)))

num = 'jonathan'
print(num + ' is a phone number: ' + str(isPhoneNumber(num)))
