#Tyler Tsang
#8659481
#ITI1120
#Assignment 4 part 2

#Read text file
file = open("NYT-bestsellers.txt","r")
lines = file.readlines()
library=[]
for line in lines:
    library.append(line.split('\t'))

def check_first_answer(ans):
    '''
    (str)--> boolean
    Checks if the answer given is an appropriate answer

    '''
    
    try:
        ans=int(ans)
        if ans>0 and ans<7:
            return True

    except:
        if str(ans) in 'Qq':
            return True
    return False

def search_year(x,y):
    '''
    (int,int)-->None
    Prints all the books from the first year given year to the second given year

    '''
    
    a=[]
    for i in range(len(library)):
        num=library[i][3].split('/')
        if int(num[2])>=x and int(num[2])<=y:
            if int(num[1])<10:
                num[1]='0'+num[1]
            date=num[2]+'-'+num[0]+'-'+num[1]
            a.append([date,library[i][0],library[i][1]])
    a.sort()
    for i in range(len(a)):
        print(a[i][1],',by ', a[i][2],'(',a[i][0],')')

def search_month(x,y):
    '''
    (int,int)-->None
    Print all of the book that were best sellers in th given year and month

    '''
    a=[]
    for i in range(len(library)):
        num=library[i][3].split('/')
        if int(num[0])==x and int(num[2])==y:
            if int(num[1])<10:
                num[1]='0'+num[1]
            date=num[2]+'-'+num[0]+'-'+num[1]
            a.append([date,library[i][0],library[i][1]])
    a.sort()
    for i in range(len(a)):
        print(a[i][1],',by ', a[i][2],'(',a[i][0],')')

def search_author(word):
    '''
    (str)-->None
    Print all the books with the given letters in the authors name

    '''
    a=[]
    word=word.lower()
    for i in range(len(library)):
        num=library[i][3].split('/')
        author=library[i][1].lower()
        if word in author:
            if int(num[1])<10:
                num[1]='0'+num[1]
            date=num[2]+'-'+num[0]+'-'+num[1]
            a.append([date,library[i][0],library[i][1]])
    a.sort()
    for i in range(len(a)):
        print(a[i][1],',by ', a[i][2],'(',a[i][0],')')

def search_title(word):
    '''
    (str)-->None
    Print all the books with the given letters in the books title

    '''
    a=[]
    word=word.lower()
    for i in range(len(library)):
        num=library[i][3].split('/')
        title=library[i][0].lower()
        if word in title:
            if int(num[1])<10:
                num[1]='0'+num[1]
            date=num[2]+'-'+num[0]+'-'+num[1]
            a.append([date,library[i][0],library[i][1]])
    a.sort()
    for i in range(len(a)):
        print(a[i][1],',by ', a[i][2],'(',a[i][0],')')
        
def freq_title(x):
    '''
    (int)-->int
    Returns the number of authors with more than the given number of best selling books

    '''
    a=[]
    counter=0
    for i in range(len(library)):
        a.append(library[i][1])
    a=freq(a)

    for w in range(len(a)):
        if a[w][0]>=x:
            counter=counter+1
    return counter

def freq_author(x):
    '''
    (int)-->None
    Prints the top given number of authors with the most best selling books

    '''
    a=[]
    auth=[]
    for i in range(len(library)):
        a.append(library[i][1])
    a=freq(a)
    a.sort()
    for z in range(-1,-x-1,-1):
        auth.append(a[z][1])
    for y in range(x):
        print(auth[y])
    


def freq(x):
    '''
    (list)-->list
    Returns a list with the frequency of each item in the list

    '''
    f=[]
    for i in range(len(x)):
        flag=False
        for j in range(len(f)):
            if x[i]==f[j][1]:
                f[j][0]=f[j][0]+1
                flag=True
        if not flag:
            f.append([1,x[i]])
    return f




def best_seller():
    '''
    (None)-->None
    Runs the main program

    '''
    
    leave = 0
    while leave!=1:
        flag1 = False
        print('=================================================================')       
        print('''What would you like to do? Enter 1,2,3,4,5,6 or Q for answer.
        1: Look up year range
        2: Look up month/year
        3: Search for author
        4: Search for title
        5: Number of authors with at least x bestseller
        6: List y authors with the most best sellers
        Q; Quit
               ''')
        print('=================================================================') 
        while not flag1:
            ans = input("Answer (1,2,3,4,5,6,Q or q):")
            flag1=check_first_answer(ans)
            if flag1==False:
                try:
                    int(ans)
                    print("Please input a valid integer ")
                except:
                    print("Please input an integer or q to quit ")
                
                
        if str(ans) in ('Qq'):
            leave = 1
            pass
        else:
            ans=int(ans)
            if ans==1:
                year1=input('Enter a beginning year ')
                flag2=False
                while not flag2:
                    try:
                        year1=int(year1)
                        if year1>=1000 and year1<=9999:
                            flag2= True
                            year1=int(year1)
                        else:
                            year1=input("Please give a 4 digit integer for the year ")
                    except:
                        year1=input("Please give a 4 digit integer for the year ")

    
                year2=input('Enter the ending year ')
                flag3=False
                while not flag3:
                    try:
                        year2=int(year2)
                        if year2>=1000 and year2<=9999:
                            flag3= True
                            year2=int(year2)
                        else:
                            year2=input("Please give a 4 digit integer for the year ")
                    except:
                        year2=input("Please give a 4 digit integer for the year ")

                search_year(year1,year2)



            elif ans==2:
                year=input("Enter a year ")
                flag2=False
                while not flag2:
                    try:
                        year=int(year)
                        if year>=1000 and year<=9999:
                            flag2= True
                            year=int(year)
                        else:
                            year=input("Please give a 4 digit integer for the year ")
                    except:
                        year=input("Please give a 4 digit integer for the year ")

                month=input("Enter a month")
                flag3=False
                while not flag3:
                    try:
                        month=int(month)
                        if month>=1 and month<=12:
                            flag3=True
                            month=int(month)
                        else:
                            month=input('Please enter a number from 1-12 for the month ')
                    except:
                            month=input('Please enter a number from 1-12 for the month ')

                search_month(month,year)
                

            elif ans==3:
                word=input('Please enter what author you would like to search for ')
                search_author(word)
                


            elif ans==4:
                word=input('Please enter what title you would like to search for ')
                search_title(word)                           


            elif ans==5:
                x=input('Please enter the number of best sellers ')
                flag=False
                while not flag:
                    try:
                        x=int(x)
                        if x>=0:
                            flag=True
                        else:
                            x=input('Please enter a positive integer ')
                    except:
                        x=input('Please enter a positive integer ')
                
                print(freq_title(x))

            else:
                x=input('Please enter the number of most best selling authors ')
                
                flag=False
                while not flag:
                    try:
                        x=int(x)
                        if x>=0:
                            flag=True
                        else:
                            x=input('Please enter a positive integer ')
                    except:
                        x=input('Please enter a positive integer ')


                freq_author(x)















best_seller()
