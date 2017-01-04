def is_divisible(n,m):

    '''
    Tell you if n is divisible by m

    (int,int) --> Phrase

    >>>is_divisible(4,2)
    4  is divisible by  2

    '''
    
    k = n%m
    Answer = k == 0
    return Answer


def is_divisible23n8():
    '''
    Tells you if x is divisible by 2 or 3 but not 8

    


    '''

    x = int(input("Enter an integer"))

    c = 2
    k = is_divisible(x,c)

    
    if k == False:
        c = 3
        k = is_divisible(x,c)

    if k == True:
        c = 8
        k = is_divisible(x,c)
        
        if k == False:
            print(x, " is divisible by 2 or 3 but not 8")
        else:
            print("It is not true that ",x," is divisible by 2 or 3 but not 8")
        
    elif k == False:
        print("It is not true that ",x," is divisible by 2 or 3 but not 8")
