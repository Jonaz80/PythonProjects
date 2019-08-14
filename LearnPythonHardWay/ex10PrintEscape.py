print("I am 6'2\" tall.") # double quote in a string
print('I am 6\'2" tall.') # single quotw escape

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat. /"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print("tab: ",tabby_cat)
print("split on line: ", persian_cat)
print("backslash: ", backslash_cat)
print("forward slash needs no exscape: /")
print("multi line list; using triple double quote (\"\"\") tabs and asterisks", fat_cat)
print(''' more
multiline text  with
single triple quote \'\'\'
''')

url_escape="https://learnpythonthehardway.org/python3/ex10.html"
#note the f-string!!
print(f"This is the URL of this lesson {url_escape} with a complete list of escape sequences")
