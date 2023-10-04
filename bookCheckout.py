#F223966
'''
This python module allows the librarian to checkout books using a member Id and book id 
'''


from tkinter import*
from tkinter import messagebox
from database import*



def check_Member(member_ID):
    '''
    Check the validity of a member Id
    '''
    if member_ID.isnumeric():
        member_ID=int(member_ID)
        if member_ID>=11000 and member_ID<=12000:
            return True
        else:
            messagebox.askretrycancel("Invalid Member ID","Try again?")
    else:
        messagebox.askretrycancel("Invalid Member ID","Try again?")
        


def check_BookID(book_ID):
    '''
    check the validity of book id
    '''
    if book_ID.isnumeric():
        book_ID=int(book_ID)
        if len(str(book_ID))==4:
            return True
        else:
            messagebox.askretrycancel("Invalid Book ID","Try again?")
    else:
        messagebox.askretrycancel("Invalid Book ID","Try again?")


def check(book_ID,member_ID):
    '''
    check validity of member and book id
    '''
    if check_BookID(book_ID)==True and check_Member(member_ID)==True:
        return True
    else:
        return False

    
def reserve(book_ID,member_ID):
    '''
    this function access the information in Book info to check whether if the book id given by the user is in the library it then passs that book if found into findlogs to get
    the log of the book and update it with the relevent information
    '''
    getBookRecords()
    logs1=log_transaction()
    found=findLogs1(logs1,book_ID)
    avail2=available2(book_ID)#checks if the book can be reserved or not
    if found== True and avail2==0:
        update=findLogs3(logs1,book_ID)#stores all the information that we want to retain from the original log and place it back in
        new_update=str(book_ID)+','+str(update[0])+','+str(member_ID)+','+str(update[1])+','+str(update[2])+','+str(update[3])+','+str(update[4])+"\n"#changes the log
        change(new_update)#updates the string through the database function change
        print("Your book has been reserved")
    else:
        messagebox.showinfo("Book availability","No copies available to reserve")





def reserve_book():
    '''
    this function checks the member id and book id and if they are valid it then calls on the reserve function above 
    '''
    member_ID=input("What is your member Id?")
    book_ID=input("What is your book Id?enter a 4 digit sequence please")
    print(check_BookID)
    print(check_Member)
    if check(book_ID,member_ID)==True:
        reserve(book_ID,member_ID) 
    else:
        messagebox.showinfo("Book availability","No copies available to reserve")


#this list stores all the months that have 31 days excluding december

thirty_one_days=[1,3,5,7,8,10]

#this list stores all the months that have 30 days 

thirty_days=[4,6,9,11]   



def return_date(book_ID,member_ID):
        '''
        the function accesses the bookinfo using getBookrecords and then accesses the log information and checks if the book ID is in library and then finds the log information and
        before it checks out the book it checks if it is available to check out and then stores it in a list which is updated with the return date and member Id 
        '''
        date=input("What is today's date? write it in the format dd/mm/yy,for all months that are not double digits only write the single digit number: ")
        d_m_y=date.split("/")#creates a list of integers with the 1st element being the day,second elemnet month and last element year
        day=int(d_m_y[0])
        month=int(d_m_y[1])
        year=int(d_m_y[2])
        getBookRecords()
        logs1=log_transaction()
        found=findLogs1(logs1,book_ID)
        avail=available(book_ID)
        if found== True and avail==1 :
            if month==12 and day>=18: #checks for books that are due in the next year so december is treated as a special case for this reason
                new_month=1
                new_day=(day+14)-31
                new_year=year+1
                print=("Return book by:%d/%d/%d "%(new_day,month,year))
            elif month==12 and day<18:
                new_month=month#checks if in Decemeber but not due in the new year
                new_day=day+14
                new_year=year
                print=("Return book by:%d/%d/%d "%(new_day,month,year))
            elif month==2: #checks if the month is february
                if (year%4)==0 and (year%100)!=0 : #checks if a leap year or not to determine whether 28 or 29 days 
                    leap_year_check=True
                    new_day=(day+14)
                    if new_day>29: #deals with books that are due in March when it is a leap year
                        new_day=(day+14)-29
                        month=month+1
                        year=year
                        print=("Return book by:%d/%d/%d "%(new_day,month,year))
                    else: #deals with books that are due in February when it is a leap year
                        new_day=day+14
                        month=month
                        year=year
                        print=("Return book by:%d/%d/%d "%(new_day,month,year))
                elif (year%100)==0 and (year%400)==0: #second condition to check if a leap year
                    leap_year_check=True
                    new_day=(day+14)
                    if new_day>29: #deals with books that are due in March when it is a leap year
                        new_day=(day+14)-29
                        month=month+1
                        year=year
                        print=("Return book by:%d/%d/%d "%(new_day,month,year))                    
                    else: #deals with books that are due in February when it is a leap year
                        new_day=day+14
                        month=month
                        year=year
                        print=("Return book by:%d/%d/%d "%(new_day,month,year))
                else: #deals with all due dates that are not in leap years so february has 28 days
                    new_day=(day+14)
                    if new_day>28: #deals with cases when due date is in March and year is not a leap year
                        new_day=(day+14)-28
                        month=month+1
                        year=year
                        print=("Return book by:%d/%d/%d "%(new_day,month,year))
                    else: #deals with cases due date is in february and not a leap year
                        new_day=day+14
                        month=month 
                        year=year
                        print=("Return book by:%d/%d/%d "%(new_day,month,year))
            elif month in thirty_days: #deals with all books that are due in months with 30 days
                day=day+14
                if (day>=30): #deals with books that are due in the next month given the month has 30 days
                    new_day=day-30
                    month=month+1
                    year=year
                    print=("Return book by:%d/%d/%d "%(new_day,month,year))
                else: #deals with books that are due in the same month given the month has 30 days
                    new_day=day+14
                    month=month
                    year=year
                    print=("Return book by:%d/%d/%d "%(new_day,month,year))
            elif month in thirty_one_days and (day+14)>=31: #deals with books that are due in months with 31 days excluding december which is an exception accounted for earlier on
                    new_day=(day+14)-31
                    month=month+1
                    year=year
                    print=("Return book by:%d/%d/%d "%(new_day,month,year))
            else: #deals with books that are due in the same month given the month has 31 days
                new_day=(day+14)
                month=month
                year=year
                print=("Return book by:%d/%d/%d "%(new_day,month,year))

            update=findLogs2(logs1,book_ID)
            new_update=str(book_ID)+','+str(update[0])+','+str(member_ID)+','+str(update[1])+','+str(date)+','+str(str(new_day)+"/"+str(month)+"/"+str(year))+','+str(update[2])+','+str(update[3])+"\n"
            change(new_update)
            print=("Return book by:%d/%d/%d "%(new_day,month,year)) 

        else:
            messagebox.showerror("Error","Book is not available or invalid details")





def checkout():
    '''
    The function first asks the user for their member id and book id and then checks using 2 function calls check_bookID and check_MemeberID if they are valid. if they are both valid
    it then runs the code for return date from above if not sends an error message
    '''
    member_ID=input("What is your member Id?")
    book_ID=input("What is your book Id?")
    print(check_BookID)
    print(check_Member)
    if check(book_ID,member_ID)==True:
        return_date(book_ID,member_ID)  
    else:
        messagebox.showerror("Error!","invalid details")  
     
    

