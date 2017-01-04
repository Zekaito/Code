def first_neg(l):
     i=0
     while i < len(l):
        if l[i] < 0:
            return l[i]
        i=i+1
     print('None')
