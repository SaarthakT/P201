from tkinter import *
window=Tk()

# add widgets here


window.title('BMI Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')


app_label=Label(window, text="BMI CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

app_label=Label(window, text="Height Label", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=90, y=40)
height=Entry(window, text="Height Entry", bd=2, width=22)
username.place(x=150, y=92)

app_label=Label(window, text="Weight Label", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=110, y=40)
weight=Entry(window, text="Weight Entry", bd=2, width=22)
username.place(x=150, y=92)

def BMICalculator():
    weight=int(weight.get())
    height=int(height.get())
    bmi=weight/(height*height)    
    bmi=round(bmi,1)
    name=username.get()
    result_label.destroy()
    if bmi<18.5:
        Message="You are Underweight"
    elif bmi>18.5 and  bmi<25:
        Message="You are Healthy"
    elif bmi>25 and bmi<30:
        Message="You are Overweight"
    elif bmi>30:
        Message="You are Obese"

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text="", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

