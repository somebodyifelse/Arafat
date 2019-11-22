from tkinter import*

cal = Tk()
cal.title("Calculator")
operator=""
text_Input = StringVar()
txtDisplay = Entry(cal,font=('arial',20,'bold'),textvariable=text_Input,bd=30, insertwidth=4,bg="powder blue", justify='right').grid(columnspan=4)

btn7=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="7", bg="powder blue").grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="8", bg="powder blue").grid(row=1,column=1)
btn9=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="9", bg="powder blue").grid(row=1,column=2)
Addition=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="+", bg="powder blue").grid(row=1,column=3)


cal.mainloop();