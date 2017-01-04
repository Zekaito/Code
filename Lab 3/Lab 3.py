def pay(p,h):

    '''
    Determines pay based on hours worked and pay per hour

    (int,int) --> Float
    

    >>>pay(10,45)
    475.0


    '''
    t = 0
    if h > 60:
        x = h-60
        t = x*(p*2)
        h = h-x

    if h > 40:
        x = h-40
        t = t+(x*(p*1.5))
        h = h-x

    t = t+(h*p)

    print(t)


def rps(x,y):
    '''
    Lets you play rock paper sissors and ell you the winner

    (Str,Str) --> Int

    >>>rps("R","S")
    -1

    '''

    
    score = 2

    if x == y:
        score = 0

    else:
        
        if x == "R":
            if y == "P":
                score = 1
            else:
                score = -1

        if x == "P":
            if y == "S":
                score = 1
            else:
                score = -1

        if x == "S":
            if y == "R":
                score = 1
            else:
                score = -1

    print(score)


def is_divisible():

    '''
    Tell you if n is divisible by m

    (int,int) --> Phrase

    >>>is_divisible(4,2)
    4  is divisible by  2

    '''
    n = int(input("Enter first number"))
    m = int(input("Enter second number"))


    
    k = n%m
    Answer = k == 0

    if Answer == True:
        print(n," is divisible by ",m)

    else:
        print(n," is not divisible by ",m)
    


    





















    
