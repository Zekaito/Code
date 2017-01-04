def first_one(lst):
    check = True
    x=len(lst)
    a=0

    while check:
        i=(x+a)//2
        

        if lst[i]== 1 and lst[i-1]==0:
            check=False
        elif lst[i]== 1 and lst[i-1]==1:
            x=i
        else:
            a=i

    return i+1

        
def last_zero(lst):
    x=first_one(lst)
    return x-1
