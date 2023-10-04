from tkinter import *
from tkinter import messagebox
from booksearch import*
from bookSelect import*
from bookCheckout import*
from bookReturn import*

#the code below creates the parent window on which other widgets are then placed so is used a place to root widgets
root = Tk()
root.title("GRAHAM LIBRARY")
root.minsize(width=400,height=400)
root.geometry("910x710")
 
#this code designs the window's layout
#heading frame creates the orange block on the screen that the system title is then placed onto 
headingFrame1=Frame(root,bg="#FFBB01",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
#library_label is located within the headingFrame1 
library_label = Label(headingFrame1, text="GRAHAM LIBRARY SYSTEM",height=5,padx=27,fg="light blue",bg="dark orange")
library_label.place(relx=0.12,rely=0.2,relwidth=0.77,relheight=0.6)
font_tuple = ("Retro",23,"bold")
library_label.configure(font=font_tuple)


#The buttons serve as a link between the gui interface and the shell as the button triggers different functions through commands which are then interacted with through the shell
btn1 = Button(root,text="Checkout Books",bg='light blue',fg='orange',command=checkout)
btn2 = Button(root,text="Return Books",bg='light blue',fg='orange',command=bookreturn)
btn3 = Button(root,text="Search for Books",bg='light blue',fg='orange',command=booksearch)
btn4 = Button(root,text="Purchase Books",bg='light blue',fg='orange',command=purchase)
btn5 = Button(root,text="Reserve Books",bg='light blue',fg='orange',command=reserve_book)
btn6 = Button(root,text="Popular Books",bg='light blue',fg='orange',command=popular_books)

#i used btn.place rather than btn.pack() or btn.grid() to created more organised GUI that was clean and simple
btn1.place(relx=0.24,rely=0.3,relwidth=0.45,relheight=0.1)
btn2.place(relx=0.24,rely=0.4,relwidth=0.45,relheight=0.1)
btn3.place(relx=0.24,rely=0.5,relwidth=0.45,relheight=0.1)
btn4.place(relx=0.24,rely=0.6,relwidth=0.45,relheight=0.1)
btn5.place(relx=0.24,rely=0.7,relwidth=0.45,relheight=0.1)
btn6.place(relx=0.24,rely=0.8,relwidth=0.45,relheight=0.1)




root.mainloop()













