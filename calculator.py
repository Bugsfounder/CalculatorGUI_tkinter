from tkinter import *
import time

def calculate(event):
    text = event.widget.cget("text")
    if text == "=":
        if calculateValue.get().isdigit():
            value = int(calculateValue.get())
        else:
            try:
                value = eval(calculateValueEntry.get())
            except Exception as err:
                value = "Wrong Expression"
                calculateValue.set(value)   
                calculateValueEntry.update() 
                time.sleep(1)
                value  = ""
        calculateValue.set(value)   
        calculateValueEntry.update()         
    elif text=="C":
        calculateValue.set("")
        calculateValueEntry.update()
    elif text=="<<<<":
        val = calculateValue.get()
        setVal = val[: len(val)-1]
        calculateValue.set(setVal)
        calculateValueEntry.update()
    else:
        calculateValue.set(calculateValue.get()+text)
        calculateValueEntry.update()

# GUI STARTS HERE
root = Tk()
root.title("Jocefyneroot Personal - Calculator")
root.geometry("600x700")
root.minsize(400,400)
root.maxsize(500,610)

inputFrame = Frame(root)
inputFrame.grid(pady=10, padx=7)

calculateValue = StringVar()

calculateValueEntry = Entry(inputFrame, fg="white", bg="#e500b4", font="lucida 20 bold", width=32, textvariable=calculateValue)
calculateValueEntry.grid(row=1, column=1, ipady=10)

keyboard = Frame(root, bg="#e500b4")
keyboard.grid(row=2, column=0)

symbolBtns = ["C", "=", "/", "*", "-", "+", ".", "0", "<<<<"]
btnCount = len(symbolBtns) - 1
btn = 9

for row in range(6):
    for column in range(3):
        if btn not in symbolBtns and btn > 0:
            Btn = Button(keyboard, padx=27, text=f"{btn}", font="lucuda 25 bold", width=4, height=1, fg="white", bg="#640058")
            Btn.grid(row=row,column=column, padx=10, pady=10)
            Btn.bind("<Button-1>", calculate)
            btn = btn-1
        else:
            Btn = Button(keyboard, padx=27, text=f"{symbolBtns[btnCount]}", font="lucuda 25 bold", width=4, height=1, fg="white", bg="#640058")
            Btn.grid(row=row,column=column, padx=10, pady=10)
            Btn.bind("<Button-1>", calculate)
            btnCount = btnCount-1

root.mainloop()