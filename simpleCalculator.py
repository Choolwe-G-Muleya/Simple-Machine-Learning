from tkinter import *


def add():
    num1 = entry1.get()
    num2 = entry2.get()
    value = num1 + num2
    return value

def sub():
    num1 = entry1.get()
    num2 = entry2.get()
    value = num1 - num2
    return value

def mult():
    num1 = entry1.get()
    num2 = entry2.get()
    value = num1 * num2
    return value

def divide():
    num1 = entry1.get()
    num2 = entry2.get()
    value = num1 / num2
    return value

def mod():
    num1 = entry1.get()
    num2 = entry2.get()
    value = num1 % num2
    return value


screen = Tk()
screen.geometry("300x300")
screen.title("Simple Calculator")
    
heading = Label(screen, text = "Simple Calculator", font = ("arial", 40, "bold"), fg = "steelblue")
    
entry1 = Entry(screen)
entry2 = Entry(screen)
    
answer = Label(screen, font = ("Arial", 12, "bold"), fg = "#00ffff")
    
    
addition = Button(screen, text = "+", font=('Comic Sans MS', 10, 'bold'), command =lambda: add)
subtraction = Button(screen, text = "+", font=('Comic Sans MS', 10, 'bold'), command = lambda: sub)
multiplication = Button(screen, text = "+", font=('Comic Sans MS', 10, 'bold'), command = lambda: mult)
division = Button(screen, text = "+", font=('Comic Sans MS', 10, 'bold'),command = lambda: divide)
modulus = Button(screen, text = "%", font =('Comic Sans MS', 10, 'bold'), command = lambda: mod )

entry1.grid(row=0)
entry2.grid(row=1)
answer.grid(row=0, column=1)

addition.grid(row=3)
subtraction.grid(row=3, column=2)
multiplication.grid(row=4)
division.grid(row=4, column=2)
modulus.grid(row=5)

screen.mainloop
    
    




	