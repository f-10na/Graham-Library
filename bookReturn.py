from tkinter import messagebox
from database import*
from bookCheckout import*
from datetime import datetime 



def return_book(book_ID,member_ID):
    '''
    takes readers book and then updates logfile.txt to remove it from it or renews a book that is due
    '''
    getBookRecords()
    logs1=log_transaction()
    found=findLogs1(logs1,book_ID)
    avail3=available3(book_ID)
    if found== True and avail3==0:
        update=findLogs4(logs1,book_ID)
        today_date=datetime.today().strftime("%d/%m/%Y")
        print(today_date)
        new_update=str(book_ID)+','+str(update[0])+','+str(member_ID)+','+str(update[1])+','+str(update[2])+','+today_date+','+str(update[3])+','+str(update[4])+','+"\n"
        print(new_update)
        change(new_update)
    else:
        messagebox.showerror("Not possible!","Book already returned!")




def bookreturn():
    '''
    this function reserves a book until it has been returned by the previous person
    '''
    member_ID=input("What is your member Id?")
    book_ID=input("What is your book Id?")
    print(check_BookID)
    print(check_Member)
    if check(book_ID,member_ID)==True:
        return_book(book_ID,member_ID) 
    else:
        messagebox.showerror("Not possible!","Book already returned!")


if __name__=="__main__":
    print("testing getBookRecords")
    records=getBookRecords()
    print(records)
    print("testing log_transaction")
    records=log_transaction()
    print(records)

