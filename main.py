import tkinter as tk
window=tk.Tk()
window.geometry("300x300")
def onclick():
    print(1)
btn1=tk.Button(text="включатель",command=onclick)
btn1.grid(row=0,column=0)
chkvar=tk.IntVar()
chkbtn=tk.Checkbutton(text="выбор лампочки",variable=chkvar,onvalue=1,offvalue=0)
chkbtn.grid(row=1,column=0)
scl=tk.Scale(label="яркость",from =1,to=100,orient=tk.HORIZONTAL,length=200,width=10)
scl.grid(row=2,column=0)
window.mainloop()