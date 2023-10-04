'''
this module stores all the functions that access the textfiles 
'''

from tkinter import messagebox


records=[]
def getBookRecords():  
    '''
    the function below creates an empty list which it stores the data by appending onto it the lines in your Book_info text file so access the data
    '''
    f = open("Book_info.txt","r") #opens the text file for reading
    for line in f:
        s=line.strip() # Strip off the \n
        record=s.split(",") # Split the string
        records.append(record)
    f.close()


def findBook(b_title):
    '''
    the function below gets a user input from the shell for the book title then checks through the second element of each line in the lists of lines in the text file in order to see
    if the library owns the book or not
    '''  
    for record in records:
        if record[1].lower()==b_title.lower():#checks the second element for each element and the .lower() ensures that whether upper or lowercase the book is still found 
            return record
    return ()#the function booksearch that uses this checks to see if something is returned or not before it runs the rest of the code which is why i return() if book not found

def findBook2(b_title):
    log_transaction()
    for record in records:
        if len(record)>1:
            if record[1].lower()==b_title.lower():#checks the second element for each element and the .lower() ensures that whether upper or lowercase the book is still found 
                print (record)
    return ()#the function booksearch that uses this checks to see if something is returned or not before it runs the rest of the code which is why i return() if book not found

#this function opens the text file to read and then stores its values within an empty list logs

def log_transaction():
    logs=[] 
    f = open("logfile.txt","r")
    for line in f:
        s=line.strip() # Strip off the \n
        log=s.split(",") # Split the string
        logs.append(log)
    f.close()
    return logs

#the function findLogs takes the book title fromm the user input and is called on in booksearch to return the log information of a book
   
def findLogs(logs,b_title):
    for log in logs:
        if log[1].lower()==b_title.lower():#checks the second element for each element and the .lower() ensures that whether upper or lowercase the book is still found 
             return log
    return "this book not in the system"   

#the function below opens logfile.txt to read and has a similar functionality to getBookrecords so is a means to access the data in logfile.txt

def log_details():
    logs1=[] 
    f = open("logfile.txt","r")
    for line in f:
        s=line.strip() # Strip off the \n
        log1=s.split(",") # Split the string
        logs1.append(log1)
    f.close()
    return logs1



def findLogs1(logs1,book_ID):
    '''
    findLogs1 is used in return_date in bookCheckout to return a boolean if a book id inputted by a user is in the logfile.txt or not in order to then check a boolean expression in an if 
    statement needed for return_date to continue running or otherwise returns a messagebox
    '''
    for log1 in logs1:#looops through the list logs1 by calling it as a parameter for the function 
        if log1[0]==book_ID: #checks if the first element of each line in logfile.txt is equal to the given book id by librarian or not
             return True
    return False 



def findLogs2(logs1,book_ID):
    '''
    findLogs2 is used in return_date in bookCheckout to return a list if a book id inputted by a user is in the logfile.txt or not.In order to then update the logfile with new  
    information by manipulating the values at the indices or otherwise returns False
    '''
    for log1 in logs1:
        if log1[0]==book_ID:
            title=log1[1] #assigns the 2nd element of the line log1 such that book id is in log1 to title as it corresponds to that position in text file
            genre=log1[3]#assigns the 4nd element of the line log1 such that book id is in log1 to genre as it corresponds to that position in text file
            copies=log1[6]#assigns the 7nd element of the line log1 such that book id is in log1 to copies as it corresponds to that position in text file
            reserved=log1[7]#assigns the 8nd element of the line log1 such that book id is in log1 to reserved as it corresponds to that position in text file
            list_info=[title,genre,copies,reserved]#creates a list that stores the new variables above to then be used based on their indices to update the logfile.txt in return_date
            return list_info
    return False


def findLogs3(logs1,book_ID):

    '''
    findLogs3 is used in reserve_book in bookCheckout to return a list if a book id inputted by a user is in the logfile.txt or not. In order to then update the logfile with new  
    information by manipulating the values at the indices or otherwise returns False
    '''
    for log1 in logs1:
        if log1[0]==book_ID:
            title=log1[1]#assigns the 2nd element of the line log1 such that book id is in log1 to title as it corresponds to that position in text file
            genre=log1[3]#assigns the 4th element of the line log1 such that book id is in log1 to genre as it corresponds to that position in text file
            copies=log1[6]#assigns the 7th element of the line log1 such that book id is in log1 to number_of_copies as it corresponds to that position in text file
            reserved=int(log1[7])+1#assigns the 8nd element of the line log1 such that book id is in log1 to reserved as it corresponds to that position in text file but adds one on to the number of copies reserved
            return_info=logs1[5]#assigns the 8nd element of the line log1 such that book id is in log1 to reserved as it corresponds to that position in text file
            return_info='Reserved'
            checkout_old_date=log1[4]#assigns the 5th element of the line log1 such that book id is in log1 to checkout_old_date as it corresponds to that position in text file
            list_info=[title,genre,checkout_old_date,return_info,copies,reserved]#creates a list that stores the new variables above to then be used based on their indices to update the logfile.txt in return_date
            return list_info
    return False 
    
def findLogs4(logs1,book_ID):
    '''
    the 
    '''
    for log1 in logs1:
        if log1[0]==book_ID:
            title=log1[1]#assigns the 2nd element of the line log1 such that book id is in log1 to title as it corresponds to that position in text file
            genre=log1[3]#assigns the 4th element of the line log1 such that book id is in log1 to genre as it corresponds to that position in text file
            copies=log1[6]#assigns the 7th element of the line log1 such that book id is in log1 to number_of_copies as it corresponds to that position in text file
            reserved=log1[7]
            checkout_old_date=log1[4]#assigns the 5th element of the line log1 such that book id is in log1 to checkout_old_date as it corresponds to that position in text file
            list_info=[title,genre,checkout_old_date,copies,reserved]#creates a list that stores the new variables above to then be used based on their indices to update the logfile.txt in return_date
            return list_info
    return False 


def available(book):
    '''
    the function below checks the availability of a book to see if can be checked out or not by looking at whether the information on when it was returned is blank or not
    '''
    f=open("logfile.txt","r")
    avail= 1
    for line in f:
        s=line.strip()
        log=s.split(",")#generates a list of data based on logfile.txt
        if log[0] == book:
            if log[5] != "":#checks return dates and if not an empty string avail is assigned 1 and is used in return_date as a condition to running the checkout code 
                avail= 1
            else:
                avail= 0 #does not run the return_date code because book not yet returned as avail=0 does not satisfy return_date
        else:
            ()
    return avail


def available2(book):
    '''
    available2 is used in reserve_date in order to check the reservation info before allowing the librarian to reserve a book
    '''
    f=open("logfile.txt","r")
    avail2= 1
    for line in f:
        s=line.strip()
        log=s.split(",")#generates a list of data based on logfile.txt
        if log[0]==book:
            print(log)
            if int(log[7])<=int(log[6]): #checks if the copies of a book reserved is less than or equal to the number of copies the library has
                avail2= 0
            else:
                avail2= 1
        else:
            ()
    return avail2



#places the string from the checkout function and then appends it to the logfile after data has been updated

def change(str):
    '''
    this function appends new updates into the lists for book checkout,reserve and return
    '''
    f=open("logfile.txt","a")
    f.write(str)
    f.close()


#by calling function we open text file for logs to be read and data to be accessed for booksearch
log_details()

#by calling function we open text file for logs to be read and data accesed,log transaction is used within in booksearch,purchase,return_date and reserve_date functions
log_transaction()

def available3(book):
    '''
    checks if there is a returned data in the logfile to determine if it can be returned or not 
    '''
    f=open("logfile.txt","r")
    avail3= 1
    for line in f:
        s=line.strip()
        log=s.split(",")#generates a list of data based on logfile.txt
        if log[0]==book:
            if log[5]=="": #checks if the copies of a book reserved is less than or equal to the number of copies the library has
                avail3= 0
            else:
                avail3= 1
        else:
            ()
    return avail3




if __name__=="__main__":
    print("testing getBookRecords")
    records=getBookRecords()
    print(records)
    print("testing log_transaction")
    records=log_transaction()
    print(records)



 
