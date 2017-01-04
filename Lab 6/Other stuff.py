def sum_5_consecutive_v1(l):
    try:
        for i in range(len(l)-4):
            total=l[i]+l[i+1]+l[i+2]+l[i+3]+l[i+4]
            if total==0:
                return True

        return False

    except IndexError:
        return False
        

def sum_5_consecutive_v2(l):
    try:
        total = 1
        i=0
        while total!=0:
            total=l[i]+l[i+1]+l[i+2]+l[i+3]+l[i+4]

            if i==(len(l)-4):
                return False
            i=i+1

        return True

    except IndexError:
        return False



def fib(n):
    if n >= 2:
        a=[1,1]
        for i in range(2,n):
            x=a[i-1] + a[i-2]
            a.append(x)
    elif n==1:
        a=[1]
    print(a)


def inner_product(x,y):
    Total=0
    for i in range(len(x)):
        Total=Total+x[i]*y[i]

    print(Total)











    
    
