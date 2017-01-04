def indexes(word,let):
    display=[]
    counter=0
    for x in word:
        if x==let:
            display.append(counter)
        counter=counter+1
    return display

def doubles(l):
    for x in range(len(l)-1):
        if l[x+1]==(l[x]*2):
            print(l[x+1])

def four_letters(l):
    display=[]
    for x in l:
        if len(x)==4:
            display.append(x)
    return display

def inBoth(l1,l2):
    for x in l1:
        for y in l2:
            if x == y:
                return True
    return False

def intersect(l1,l2):
    display=[]

    for x in l1:
        for y in l2:
            if x==y:
                display.append(x)
    return display

def pair(l1,l2,n):

    for x in l1:
        for y in l2:
            if x+y==n:
                print(x," ", y)

def pairSum(l,n):
    for x in range(len(l)):
        for y in range(x+1,len(l)):
            if l[x]+l[y]==n:
                print(x,y)

def lastfirst(l):
    a=[]
    b=[]

    for x in range(len(l)):
        y=l[x].find(",")
        z=l[x][0:y]
        f=l[x][y+1:]
        a.append(f)
        b.append(z)

    print(a,b)












