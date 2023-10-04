#F223966
"""
this module generates a graph that shows the proportion of a a budget x to spend one each genre based on the log transactions
"""

import matplotlib.pyplot as plt
from database import*

#i create the empty list in order to then append all occurences of genre names in the logfile.txt in the lines
genre=[]


#i created five empty counts initially as global variables in order to then store the number of occurences of the five respective genres in the library - Romance, Mystery, Horror,Non-fiction and Fantasy

count1=0
count2=0
count3=0
count4=0
count5=0


def popular_books():
    '''
    first you open the logfile.txt and create a list of all the lines with each line being an element in the list hence the list can be said to be of type [[line]]
    then i append onto the empty list genre all the 4th elements in the line as the index of 3 corresponds to the genre for each of the lines
    '''
    log=log_transaction()
    with open("logfile.txt",'r')as f:
        look=f.readlines()
        for line in look:
            l=line.split(",")
            genre.append(l[3])
            
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    

    #use a for loop to increase by increments of one whenever a particular instance of a genre is met using iif-elif-else statements
    for i in genre:
        if i=="Romance":
            count1=count1+1
        elif i=="Horror":
            count2=count2+1
        elif i=="Mystery":
            count3=count3+1
        elif i=="Non-fiction":
            count4=count4+1
        elif i=="Fantasy":
            count5=count5+1
        else:
            ()

#genre1 and value behave as arrays and i assigned the values of the counts and genres respectively to provide the inputs for the bar chart
    genre1=["Romance","Horror","Mystery","Non-fiction","Fantasy"]
    values=[count1,count2,count3,count4,count5]
    
    plt.bar(genre1,values)
    plt.xlabel("Genres")
    plt.ylabel("Number of times loaned")
    plt.title("Popularity of Genres based on number of books loaned")
    plt.show()


def purchase():
    '''
    the purchase function calculates the proportions to spend on what by first adding up the counts to get the total number of books and then comparing the number of occurences 
    of a specific genre with respective to the total amount so if the specific count for a genre is less than half the total number of books then only allocate 10% else allocate 
    50% of the budget to purchasing the genre
    1=(count_a*0.1)+(count_b*0.1)+(count_c*0.1)+(count_d*0.1)+(count_d*0.5) this ensures the budget is used up
    '''
    budget=int(input("What is your budget?"))
    total=count1+count2+count3+count4+count5
    if count1<(total*0.5):
        r_budget=0.1*budget
    else:
        r_budget=0.6*budget
    if count2<(total*0.5):
        h_budget=0.1*budget
    else:
        h_budget=0.6*budget
    if count3<(total*0.5):
        m_budget=0.1*budget
    else:
        m_budget=0.6*budget
    if count4<(total*0.5):
        n_budget=0.1*budget
    else:
        n_budget=0.6*budget
    if count5<(total*0.5):
        f_budget=0.1*budget
    else:
        f_budget=0.6*budget
            
        
        genre1=["Romance","Horror","Mystery","Non-fiction","Fantasy"]
        values1=[r_budget,h_budget,m_budget,n_budget,f_budget]
        
        plt.bar(genre1,values1)
        plt.xlabel("Genres")
        plt.ylabel("Money to spend")
        plt.title("Purchase Advice")
        plt.show()
















