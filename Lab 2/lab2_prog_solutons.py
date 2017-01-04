import math

def repeater(s1,s2,n):
    print('_',(s1+s2)*n,'_')


def roots(a,b,c):
    print('The quadradic equation with coefficients a=',a,' b=',b,' c=',c)
    print('has the following solutions:')
    print((-b + math.sqrt(b**2-4*a*c))/2*a,(-b - math.sqrt(b**2-4*a*c))/2*a)
    
def real_roots(a1,b1,c1):
    x=b1**2-4*a1*c1
    y=x>=0
    return(y)

def reverse(z):
    p=z%10
    z=(z-p)//10
    
    p=str(p)
    z=str(z)
    m=p+z
    m=int(m)
    print(m)
