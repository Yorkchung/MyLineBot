# -*- coding: utf-8 -*-
"""
Created on Thu Jan  1 13:56:05 2019

@author: 佑崧
"""
def countBMI():
    if weight.get() == 0 or height.get() == 0:
        msg.set("身高及體重都不能為 0！")
    else:
        bmi = weight.get()/(height.get()*height.get())*10000
        getbmi.set(bmi)
        if bmi > 24:
            msg.set("太胖了，該減肥了！")
        elif bmi < 16:
            msg.set("太瘦了，多吃一點！")
        else:
            msg.set("恭喜，符合標準，繼續保持！")
    
import tkinter as tk

win = tk.Tk()
win.geometry("400x300")
win.title("BMI")

label1 = tk.Label(win,text="身高 (cm) :")
label1.place(x=80, y=30)
height = tk.IntVar()
txt1 = tk.Entry(win,textvariable=height)
txt1.place(x=150, y=30)

label2 = tk.Label(win,text="體重 (kg) :")
label2.place(x=80, y=60)
weight = tk.IntVar()
txt2 = tk.Entry(win,textvariable=weight)
txt2.place(x=150, y=60)

count = tk.Button(win, text="計算BMI", command=countBMI)
count.place(x=120, y=100)

msg = tk.StringVar()
showMsg = tk.Label(win,textvariable=msg,fg="red")
showMsg.place(x=120, y=160)

label3 = tk.Label(win,text="BMI :")
label3.place(x=90, y=130)
getbmi = tk.StringVar()
showBMI = tk.Label(win,textvariable=getbmi)
showBMI.place(x=120, y=130)

win.mainloop()