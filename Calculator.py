from tkinter import *

"""
Tkinter python Calculator 

simple ui with usable buttons, including numbers, operators, equals, and clear buttons
still working on safer method not using eval, and decimal calculations
    
"""

#global output value
outputWindow = 0

#main function for inserting numbers into textbox
def calc(num):
    global outputWindow
    if(outputWindow == 0):
        outputWindow = num
        entry.delete(0, "end")
        entry.insert(0, outputWindow)

        return
    if(outputWindow != 0):
        outputWindow = (str(outputWindow) + str(num))
        entry.delete(0, "end")
        entry.insert(0, outputWindow)
        return

#main function for inserting operators into function
def arithmetic(symbol):
    global outputWindow
    newOutputWindow = outputWindow
    outputWindow = str(outputWindow) + str(symbol)
    entry.delete(0, "end")
    entry.insert(0, outputWindow)
    return

#equals button handeler
def equals():
    global outputWindow
    outputWindow = eval(outputWindow)
    entry.delete(0, "end")
    entry.insert(0, outputWindow)
    return
    
#clear button handeler 
def clear():
    global outputWindow
    outputWindow = 0
    entry.delete(0, "end")
    entry.insert(0, outputWindow)
        
#tkinter initialization
root = Tk()
root.title("Calculator")
root.geometry("300x370")  # set starting size of window


    
label = Label(root, text="Perform a calculation!")
label.grid(row=0, column=0, pady = 2, padx = 10, sticky = W, columnspan = 5)

entry = Entry(root, width=45)
entry.insert(0, outputWindow)
entry.grid(row=1, column=0, sticky = W, pady = 10, padx = 10, columnspan = 5)



button1 = Button(root, text=' 1 ', fg='black', bg='gray', height=2, width=7, command=lambda: calc(1))
button1.grid(row=2, column=1, padx = 8, pady = 10, sticky = W)
 
button2 = Button(root, text=' 2 ', fg='black', bg='gray', height=2, width=7, command=lambda: calc(2))
button2.grid(row=2, column=2, padx = 8, pady = 10, sticky = W)

button3 = Button(root, text=' 3 ', fg='black', bg='gray', height=2, width=7, command=lambda: calc(3))
button3.grid(row=2, column=3, padx = 8, pady = 10, sticky = W)

buttonp = Button(root, text=' + ', fg='black', bg='gray', height=2, width=7, command=lambda: arithmetic("+"))
buttonp.grid(row=2, column=4, padx = 8, pady = 10, sticky = W)
 
 
 
button4 = Button(root, text=' 4 ', fg='black', bg='gray', height=2, width=7, command=lambda: calc(4))
button4.grid(row=3, column=1, padx = 8, pady = 10, sticky = W)

button5 = Button(root, text=' 5 ', fg='black', bg='gray', height=2, width=7, command=lambda: calc(5))
button5.grid(row=3, column=2, padx = 8, pady = 10, sticky = W)
 
button6 = Button(root, text=' 6 ', fg='black', bg='gray', height=2, width=7, command=lambda: calc(6))
button6.grid(row=3, column=3, padx = 8, pady = 10, sticky = W)

buttonmi = Button(root, text=' - ', fg='black', bg='gray', height=2, width=7, command=lambda: arithmetic("-"))
buttonmi.grid(row=3, column=4, padx = 8, pady = 10, sticky = W)



button7 = Button(root, text=' 7 ', fg='black', bg='gray', height=2, width=7, command=lambda: calc(7))
button7.grid(row=4, column=1, padx = 8, pady = 10, sticky = W)

button8 = Button(root, text=' 8 ', fg='black', bg='gray', height=2, width=7, command=lambda: calc(8))
button8.grid(row=4, column=2, padx = 8, pady = 10, sticky = W)
 
button9 = Button(root, text=' 9 ', fg='black', bg='gray', height=2, width=7, command=lambda: calc(9))
button9.grid(row=4, column=3, padx = 8, pady = 10, sticky = W)

buttonmu = Button(root, text=' * ', fg='black', bg='gray', height=2, width=7, command=lambda: arithmetic("*"))
buttonmu.grid(row=4, column=4, padx = 8, pady = 10, sticky = W)



button0 = Button(root, text=' 0 ', fg='black', bg='gray', height=2, width=7, command=lambda: calc(0))
button0.grid(row=5, column=1, padx = 8, pady = 10, sticky = W)

buttondo = Button(root, text=' . ', fg='black', bg='gray', height=2, width=7)
buttondo.grid(row=5, column=2, padx = 8, pady = 10, sticky = W)

buttoneq = Button(root, text=' = ', fg='black', bg='gray', height=2, width=7, command=lambda: equals())
buttoneq.grid(row=5, column=3, padx = 8, pady = 10, sticky = W)

buttond = Button(root, text=' / ', fg='black', bg='gray', height=2, width=7,command=lambda: arithmetic("/"))
buttond.grid(row=5, column=4, padx = 8, pady = 10, sticky = W)

buttonc = Button(root, text=' clr ', fg='black', bg='gray', height=2, width=7, command=clear)
buttonc.grid(row=6, column=4, padx = 8, pady = 10, sticky = E)


root.mainloop()

