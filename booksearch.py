#F223966
'''
this module looks through the Book_info.txt and sees if library has the book and then returns the book with its respective information so first the Book_info.txt information and 
after further prompting tells you the log informatiom fo the book

'''

from tkinter import*
from tkinter import messagebox
from database import *


def booksearch():
    '''
    the function below utilises getBookrecords which opens and reads Book_Info.txt and then splits it at each new line in the text file in order to generate a list of all the lines
    in you text file. It then takes an input from the user on what book they are looking for and then checks findBook to see if for any of the lines,if the index for book title 
    corresponds to the title which was given and either returns a message box if it doesn't or gives you the book_info and then asks if you would like the loginfo as well.
    '''
    getBookRecords()#access the book info for reading and searching through the lines by using split 
    b_title=input("Book?")
    findBook2(b_title)
    print(findBook2(b_title))
    if len(findBook2(b_title))!=0:
        logInfo=int(input("Do you want to see the log info for this book? 1 for Yes "))
        if logInfo==1:
            logs=log_transaction()
            print(findLogs(logs,b_title))
    else:
        messagebox.askquestion("New book?","Search again?")
        


