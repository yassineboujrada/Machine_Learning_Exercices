from tkinter import *
from fct import linair

root = Tk()
root.geometry("300x400")
root.title("linaire regration simple")
root.config(bg="#000042")

# fonctions 
# def openNewWindow(L=0,x=0,y=0):
#     newWindow = Toplevel(root)
#     newWindow.title("New Window")
#     newWindow.geometry("700x400")
#     #mean of function is X : {}, y : {}".format(str(L.moy(x))
#     mean=Label(newWindow, text ="hhhh")
#     # var=Label(newWindow, text ="variance of function is X : {}, y : {}".format(str(L.variance(x)) , str(L.variance(y)) ))
#     # cov=Label(newWindow, text ="covariance of function is : {}".format(str(L.cov())))
#     ########################################################################
#     mean.place(x=5,y=25)
#     # var.place(x=15,y=45)
#     # cov.place(x=15,y=65)
#     # ###############################
#     mean.pack()

def raise_frame(frame):
    frame.tkraise()
    
f1 = Frame(root,bg="#000042",width = 300, height=400, pady=3)
f2 = Frame(root,bg="#000042",width = 300, height=400, pady=3)
f3 = Frame(root,bg="#000042",width = 300, height=400, pady=3)

for frame in (f1, f2,f3):
    frame.grid(row=0, column=0, sticky='news')
  

def printhi(*args):
    x_data=[int(i) for i in x_value.get().split(",")]
    y_data=[int(i) for i in y_value.get().split(",")]
    
    if (i.get() ==1):
        print("you picked option1")
        swith_window([1,2,3],[3,4,5],f2)
        # print(x_data,y_data,l.fct_lineaire_regression(8))
    else:
        print("you picked option2")

def swith_window(x,y,f=f2):
    raise_frame(f)
    l=linair(x,y)
    mean = Label(f, text="mean of x : {} and y : {}".format(l.moy(x),l.moy(y))).pack()
    var=Label(f, text="variance of \nx : {} \ny : {}".format(l.variance(x),l.variance(y))).pack()
    cov=Label(f, text="covariance is : {}".format(l.cov())).pack()
    l.show_graphe_lineaire()
# label of my app
label_warning=Label(f1, text="you should use ',' between numbers",bg="#000042")
x_label = Label(f1, text="x value")
y_label=Label(f1, text="y value")
x_label.pack()
y_label.pack()
label_warning.pack()
label_warning.configure(foreground="red")
label_warning.place(x=55,y=10)
x_label.place(x=20,y=50)
y_label.place(x=20,y=100)
# text area
x_value = Entry(f1, textvariable = "x_data", width = 30)
y_value = Entry(f1, textvariable = "y_data", width = 30)
x_value.pack()
x_value.place(x=70,y=50)
y_value.pack()
y_value.place(x=70,y=102)
#btn of my app
i=IntVar()
r1 = Radiobutton(f1, text="cost function", value=1,variable=i)
r2 = Radiobutton(f1, text="methode descente", value=2,variable=i)
r1.pack()
r2.pack()
r1.place(x=80,y=150)
r2.place(x=150,y=150)
calculat_btn=Button(f1, text="Click to print hi", command=printhi)
calculat_btn.place(x=95,y=185)

raise_frame(f1)
root.mainloop()