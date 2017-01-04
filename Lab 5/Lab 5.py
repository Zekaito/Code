def ah(l,x,y):
    count=0
    z=0
    for i in l:
        if i>x and i<y:
            count=count+1
            if z==0:
                z=i
            else:
                z=min(z,i)
    
    print('(',count,',',z,')')

def is_perfect(x):
    count=0
    for u in range(1,x):
        if x%u == 0:
            count=count + u
    if x==count:
        return True
    else:
        return False

def is_perfect35():
    count=0
    x=1
    while x<35000000:
        count=0
        for u in range(1,x):
            if x%u == 0:
                count=count + u
        if x==count:
            print(x)
        x=x+1

def arithmetic(l):
    Check=l[1]-l[0]
    for i in range(len(l)-1):
        v=l[i+1]-l[i]
        if v!=Check:
            return False
    return True

def is_sorted(l):
    for i in range(len(l)-1):
        if l[i+1]<l[i]:
            return False
    return True













        
            
