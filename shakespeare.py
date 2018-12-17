# From https://projects.raspberrypi.org/en/projects/shakespearean-insult-generator
# requires [sudo] pip3 install guizero


import random
from guizero import App, Text, TextBox, PushButton, Slider, Picture
from time import sleep


def insult():
    word_a = random.choice(list_a)
    word_b = random.choice(list_b)
    word_c = random.choice(list_c)
    insult = "Thou " + word_a + " " + word_b + " " + word_c + "!"
    return insult

def insult_me():
    new_insult = insult()
    welcome_message.value = my_name.value + "? \n" + new_insult

def change_text_size(slider_value):
    welcome_message.size = slider_value




list_a = []
list_b = []
list_c = []

with open('insults.csv', 'r') as f:
    for line in f:
        words = line.split(',')
        list_a.append(words[0])
        list_b.append(words[1])
        list_c.append(words[2].strip())

app = App(title="Shakespearean Greetings!", height=400, bg='white')
picture = Picture(app, image='Shakespeare.png', align='center')
welcome_message = Text(app, text="What is thy name syrah?", size=20, font="Times New Roman", color="#ff0000")
my_name = TextBox(app, width="20")
update_text = PushButton(app, command = insult_me, text="Meet Shakespeare")


#text_size = Slider(app, command=change_text_size, start=10, end=80)



app.display()
