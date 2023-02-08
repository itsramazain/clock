#clock app tells exactly the time rn and date <3
from tkinter import *
from time import *

from PIL import ImageTk, Image
window=Tk()

window.geometry('622x350')

window.title("clock")
window.iconphoto(True,ImageTk.PhotoImage(Image.open("clocklogo.ico")))
clockpic = ImageTk.PhotoImage(Image.open("digitalc.jpg"))
label=Label(window,image=clockpic)
label.pack()
timelable=Label(window,bg='#c4ced0',font=("Baskerville Old Face",55))
timelable.place(x=150,y=150)
daylable=Label(window,bg='#c4ced0',font=("Baskerville Old Face",14))
daylable.place(x=400,y=90)
datelable=Label(window,bg='#c4ced0',font=("Baskerville Old Face",40))
datelable.place(x=120,y=70)

while True:
    nowtime=strftime('%I:%M:%S %p')
    nowday=strftime('%A')
    nowdate=strftime('%m/%d/%Y')
    timelable.config(text=nowtime)
    daylable.config(text=nowday)
    datelable.config(text=nowdate)
    window.update()

window.mainloop()