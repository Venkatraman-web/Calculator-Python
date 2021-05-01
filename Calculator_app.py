import tkinter
from tkinter.font import Font


tk = tkinter.Tk()
tk.title("Venkat 's Calculator")
tk.geometry('380x570')
# tk.maxsize(600, 450)
# tk.minsize(330, 330)

fontInput = Font(size=10, slant="italic")

myInput = tkinter.Entry(tk, width=50, borderwidth=5,
                        textvariable=1, font=fontInput)
myInput.grid(row=0, column=0, columnspan=3, padx=10, pady=10, ipady=10)


def nums(num):
    current = myInput.get()
    myInput.delete(0, 'end')
    myInput.insert(2, str(current) + str(num))


def clear():
    myInput.delete(0, 'end')


def button_add():
    fNumber = myInput.get()
    global fNum
    global operation
    operation = 'addition'
    fNum = int(fNumber)
    myInput.delete(0, 'end')


def subtract():
    fNumber = myInput.get()
    global fNum
    global operation
    operation = 'subtract'
    fNum = int(fNumber)
    myInput.delete(0, 'end')


def multiply():
    fNumber = myInput.get()
    global fNum
    global operation
    operation = 'multiply'
    fNum = int(fNumber)
    myInput.delete(0, 'end')


def divide():
    fNumber = myInput.get()
    global fNum
    global operation
    operation = 'divide'
    fNum = int(fNumber)
    myInput.delete(0, 'end')


def equal():
    second_number = myInput.get()
    myInput.delete(0, 'end')
    if operation is 'addition':
        myInput.insert(0, fNum + int(second_number))
    elif operation is 'subtract':
        myInput.insert(0, fNum - int(second_number))
    elif operation is 'multiply':
        myInput.insert(0, fNum * int(second_number))
    elif operation is 'divide':
        myInput.insert(0, fNum / int(second_number))


    # Code

    # Define Buttons
fontTuple = Font(size=16, slant="italic")

button1 = tkinter.Button(tk, text='1', padx=40, pady=20, command=lambda: nums(
    1), bg="red", borderwidth='3', relief="raised", font=fontTuple)
button2 = tkinter.Button(tk, text='2', padx=40, pady=20, command=lambda: nums(
    2), bg="blue", borderwidth='3', relief="raised", font=fontTuple)
button3 = tkinter.Button(tk, text='3', padx=40, pady=20, command=lambda: nums(
    3), bg="yellow", borderwidth='3', relief="raised", font=fontTuple)
button4 = tkinter.Button(tk, text='4', padx=40, pady=20, command=lambda: nums(
    4), bg="orange", borderwidth='3', relief="raised", font=fontTuple)
button5 = tkinter.Button(tk, text='5', padx=40, pady=20, command=lambda: nums(
    5), bg="tomato", borderwidth='3', relief="raised", font=fontTuple)
button6 = tkinter.Button(tk, text='6', padx=40, pady=20, command=lambda: nums(
    6), bg="greenyellow", borderwidth='3', relief="raised", font=fontTuple)
button7 = tkinter.Button(tk, text='7', padx=40, pady=20, command=lambda: nums(
    7), bg="green", borderwidth='3', relief="raised", font=fontTuple)
button8 = tkinter.Button(tk, text='8', padx=40, pady=20, command=lambda: nums(
    8), bg="violet", borderwidth='3', relief="raised", font=fontTuple)
button9 = tkinter.Button(tk, text='9', padx=40, pady=20, command=lambda: nums(
    9), bg="pink", borderwidth='3', relief="raised", font=fontTuple)
button0 = tkinter.Button(tk, text='0', padx=40, pady=20, command=lambda: nums(
    0), bg="magenta", borderwidth='3', relief="raised", font=fontTuple)
addBtn = tkinter.Button(tk, text='+', padx=39, pady=20, command=button_add,
                            bg="lightskyblue", borderwidth='3', relief="raised", font=fontTuple)
equalBtn = tkinter.Button(tk, text='=', padx=102, pady=20, command=equal,
                            bg="aqua", borderwidth='3', relief="raised", font=fontTuple)
clearBtn = tkinter.Button(tk, text='C', padx=102, pady=20, command=clear,
                            bg="lime", borderwidth='3', relief="raised", font=fontTuple)
subtractBtn = tkinter.Button(tk, text='-', padx=39, pady=20, command=subtract,
                            bg="blueviolet", borderwidth='3', relief="raised", font=fontTuple)
multiplyBtn = tkinter.Button(tk, text='*', padx=39, pady=20, command=multiply,
                            bg="lightcoral", borderwidth='3', relief="raised", font=fontTuple)
divideBtn = tkinter.Button(tk, text='/', padx=39, pady=20, command=divide,
                            bg="lightgreen", borderwidth='3', relief="raised", font=fontTuple)

# myFrame = tkinter.Frame(myInput, bg='grey', padx=90)
# myFrame.grid(row=1, column=3)

p1 = tkinter.PhotoImage(file='calc.png')
tk.iconphoto(False, p1)

# Put the buttons on the screen

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
clearBtn.grid(row=4, column=1, columnspan=2)
addBtn.grid(row=5, column=0)
equalBtn.grid(row=5, column=1, columnspan=2)

subtractBtn.grid(row=6, column=0)
multiplyBtn.grid(row=6, column=1)
divideBtn.grid(row=6, column=2)


tk.mainloop()

