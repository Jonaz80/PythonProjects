# From https://projects.raspberrypi.org/en/projects/getting-started-with-guis
# requires [sudo] pip3 install guizero


from guizero import App, Text, TextBox, PushButton, Slider, Picture

def say_myname():
    welcome_message.value = my_name.value

def change_text_size(slider_value):
    welcome_message.size = slider_value

app = App(title="Hello World")

welcome_message = Text(app, text="Welcome to my app!", size=40, font="Times New Roman", color="#ff0000")
my_name = TextBox(app, width="40")
update_text = PushButton(app, command = say_myname, text="Display my name")
text_size = Slider(app, command=change_text_size, start=10, end=80)
my_cat = Picture(app, image="Scratch_Cat_Brother.png")


app.display()
