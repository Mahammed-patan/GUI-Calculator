#1st Importing library
from tkinter import *

#2nd Define three functions
def button_press(num): #1st
  global equaltion_text
  equaltion_text += str(num)
  equation_label.set(equaltion_text)

def equals(): #2nd
  global equaltion_text
  try:
    total = str(eval(equaltion_text))
    equation_label.set(total)
    equaltion_text = total
  except ZeroDivisionError:
    equation_label.set('Arithmatic Error!')
    equaltion_text = ''

def clear(): #3rd
  global equaltion_text
  equation_label.set('')
  equaltion_text = ""

# Setup Display 
screen = Tk()
screen.title('GUI Calculator')
screen.geometry('500x650')

#create a variable with empty scring
equaltion_text = ""
equation_label = StringVar()
label = Label(screen, textvariable=equation_label, font=25,bg='white',width=30, height= 3)
label.pack()

#create Frame for buttons
frame = Frame(screen)
frame.pack()

#deffine buttons
button1 = Button(frame, text=1, font=20, width=10,height=4,command= lambda: button_press(1))
button1.grid(row=0,column=0)
button2 = Button(frame, text=2, font=20, width=10,height=4,command= lambda: button_press(2))
button2.grid(row=0,column=1)
button3 = Button(frame, text=3, font=20, width=10,height=4,command= lambda: button_press(3))
button3.grid(row=0,column=2)
mul = Button(frame, text='x', font=20, width=10,height=4,command= lambda: button_press('*'))
mul.grid(row=0,column=3)

button4 = Button(frame, text=4, font=20, width=10,height=4,command= lambda: button_press(4))
button4.grid(row=1,column=0)
button5 = Button(frame, text=5, font=20, width=10,height=4,command= lambda: button_press(5))
button5.grid(row=1,column=1)
button6 = Button(frame, text=6, font=20, width=10,height=4,command= lambda: button_press(6))
button6.grid(row=1,column=2)
plus = Button(frame, text='+', font=20, width=10,height=4,command= lambda: button_press('+'))
plus.grid(row=1,column=3)

button7 = Button(frame, text=7, font=20, width=10,height=4,command= lambda: button_press(7))
button7.grid(row=2,column=0)
button8 = Button(frame, text=8, font=20, width=10,height=4,command= lambda: button_press(8))
button8.grid(row=2,column=1)
button9 = Button(frame, text=9, font=20, width=10,height=4,command= lambda: button_press(9))
button9.grid(row=2,column=2)
minus = Button(frame, text='-', font=20, width=10,height=4,command= lambda: button_press('-'))
minus.grid(row=2,column=3)

decimal = Button(frame, text='.', font=20, width=10,height=4,command= lambda: button_press('.'))
decimal.grid(row=3,column=0)
button0 = Button(frame, text=0, font=20, width=10,height=4,command= lambda: button_press(0))
button0.grid(row=3,column=1)
div = Button(frame, text='/', font=20, width=10,height=4,command= lambda: button_press('/'))
div.grid(row=3,column=2)
equal = Button(frame, text='=', font=20, width=10,height=4,command= equals)
equal.grid(row=3,column=3)

clear = Button(screen, text='Clear', font=20, width=15,height=2,command= clear)
clear.pack()


screen.mainloop()