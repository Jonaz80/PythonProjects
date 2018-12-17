# from https://projects.raspberrypi.org/en/projects/getting-started-with-guis/12
# requires pip3 install guizero

from guizero import App, Text, Combo, CheckBox, ButtonGroup, PushButton, info

def do_booking():
    info("Booking", "Thank you for your booking")
    print(film_choice.value)
    print(vip_seat.value)
    print(row_choice.value)

app = App(title='Cinema Gui', width=400, height=200, layout='grid', bg='lightblue')
film_description = Text(app, text='Which film?', grid=[0,0], align='left')
film_choice = Combo(app, options=['Star Wars', 'Star Trek', 'A Star is Born'],selected='Star Trek', grid=[1,0], align='left')
seat_desc = Text(app, text='Seat Type', grid=[0,1], align ='left')
vip_seat = CheckBox(app, text='VIP seat?', grid=[1,1], align='left')
row_description = Text(app, text='Seat Location?', grid=[0,2], align='left')
row_choice = ButtonGroup(app, options=[ ['Front', 'F'], ['Middle', 'M'], ['Back', 'B'] ],
                         selected='M', horizontal=True, grid=[1,2], align='left')
book_seats = PushButton(app, command=do_booking, text = 'Book Seats', grid=[1,3], align = 'left')

app.display()
