def is_eligible(age,citizenship,prison):
    if age >= 18 and (citizenship=="canada" or citizenship=="canadian") and prison=='no' :
        return True
    else :
        return False


age=int(input('What is your age'))
citizenship=input('What is your citizenship')
citizenship=citizenship.strip().lower()
prison=input('Have you ever been in prsion for a criminal offense?')
prison=prison.strip().lower()

is_eligible(age,citizenship,prison)

if is_eligible(age,citizenship,prison):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

def mess(zzz):
    redone=""
    
    for i in zzz:
        if i in "rstvwxyz":
            i=i.upper()
        elif i == " ":
            i="-"
        redone=redone+i
    return redone

def half(x,y):

    for i in range(1,y+1):
        print(x*i)


def divisible(x):
    for i in range(1,x+1):
        Check = x%i
        if Check==0:
            print(i)




def prime(x):
    m=False
    for i in range(2,x):
        n=x%i
        if n == 0:
            return False
    return True
            






        
    
