import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Calculator")


e = tk.Entry(mainWindow, width=60, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, "end")
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, "end")

def button_func(func):
    global function
    function = func
    first_number = e.get()
    e.insert(len(first_number), function)
    global f_num
    f_num = int(first_number)


def button_equal():
    second_number = e.get()[(len(str(f_num))+1):]
    global s_num
    s_num = int(second_number)
    e.insert(len(str(f_num))+len(str(s_num))+1, "=")
    e.delete(0, 'end')
    if function == "+":
        e.insert(0, f_num+s_num)
    if function == "-":
        e.insert(0, f_num-s_num)
    if function == "*":
        e.insert(0, f_num*s_num)
    if function == "/":
        e.insert(0, int(f_num/s_num) if (f_num/s_num)//s_num == 0 else f_num/s_num)


button1 = tk.Button(mainWindow, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = tk.Button(mainWindow, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = tk.Button(mainWindow, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = tk.Button(mainWindow, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = tk.Button(mainWindow, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = tk.Button(mainWindow, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = tk.Button(mainWindow, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = tk.Button(mainWindow, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = tk.Button(mainWindow, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = tk.Button(mainWindow, text="0", padx=40, pady=20, command=lambda: button_click(0))
buttonAdd = tk.Button(mainWindow, text="+", padx=47, pady=20, command=lambda: button_func("+"))
buttonSub = tk.Button(mainWindow, text="-", padx=48, pady=20, command=lambda: button_func("-"))
buttonMult = tk.Button(mainWindow, text="*", padx=40.5, pady=20, command=lambda: button_func("*"))
buttonDiv = tk.Button(mainWindow, text="/", padx=40.5, pady=20, command=lambda: button_func("/"))
buttonEq = tk.Button(mainWindow, text="=", padx=47, pady=20, command=button_equal)
buttonClear = tk.Button(mainWindow, text="Clear", padx=37, pady=20, command=button_clear)


button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
buttonClear.grid(row=1, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
buttonAdd.grid(row=2, column=3)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
buttonSub.grid(row=3, column=3)

button0.grid(row=4, column=0)
buttonMult.grid(row=4, column=1)
buttonDiv.grid(row=4, column=2)
buttonEq.grid(row=4, column=3)


mainWindow.mainloop()
