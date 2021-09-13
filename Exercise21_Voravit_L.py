from tkinter import *
import math

def leftClickButton(event):
    def BMI():
        BMI = (float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2))
        if BMI >= 30:
            labelResult.configure(text = "Very Fat")
        elif BMI >= 25:
            labelResult.configure(text = "Fat")
        elif BMI >= 23:
            labelResult.configure(text = "Overweight")
        elif BMI >= 18.6:
            labelResult.configure(text = "Standard")
        else:
            labelResult.configure(text = "Skinny")
    labelResult.configure(BMI())

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)

MainWindow.mainloop()