import tkinter as tk
window = tk.Tk()
window.geometry('500x500')
window.title('Compound Interest')
p = tk.IntVar()
r = tk.IntVar()
n = tk.IntVar()
a = tk.DoubleVar()
ci = tk.DoubleVar()
lbl1 = tk.Label(window , text='Enter principle amount:')
lbl1.place(x=50,y=50)
ent1=tk.Entry(window,textvariable=p)
ent1.place(x=200,y=50)
lbl2=tk.Label(window,text='Enter rate of interest:')
lbl2.place(x=50,y=100)
ent2=tk.Entry(window,textvariable=r)
ent2.place(x=200,y=100)
lbl3=tk.Label(window,text="Enter no of year's")
lbl3.place(x=50,y=150)
ent3=tk.Entry(window,textvariable=n)
ent3.place(x=200,y=150)
lbl4=tk.Label(window,text="your amount is:")
lbl4.place(x=50,y=200)
ent4=tk.Entry(window,textvariable=a)
ent4.place(x=200,y=200)
lbl5=tk.Label(window,text="your compound interest is:")
lbl5.place(x=50,y=250)
ent5=tk.Entry(window,textvariable=ci)
ent5.place(x=200,y=250)
def annually():
    principle=p.get()
    rate=r.get()
    noofyear=n.get()
    annually=principle*pow((1+(rate/100)),noofyear)
    a.set(annually)
    amount=a.get()
    comp=amount-principle
    ci.set(comp)
def halfyearly():
    principle = p.get()
    rate = r.get()
    noofyear = n.get()
    halfyearly=principle*pow((1+(rate / 100)),2*noofyear)
    a.set(halfyearly)
    amount=a.get()
    comp=amount-principle
    ci.set(comp)
def cancel():
    p.set(' ')
    r.set(' ')
    n.set(' ')
    a.set(' ')
    ci.set(' ')
btn1=tk.Button(window,text='annually',command=annually)
btn1.place(x=100,y=300)
btn2=tk.Button(window,text='yearly',command=halfyearly)
btn2.place(x=180,y=300)
btn3=tk.Button(window,text='cancel',command=cancel)
btn3.place(x=250,y=300)
window.mainloop()
