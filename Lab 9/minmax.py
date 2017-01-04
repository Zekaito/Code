def min_or_max(lst,check):
    num=lst[0]
    x=0
    if check:
         for i in range(len(lst)):
             if num>= lst[i]:
                 num=lst[i]
                 x=i

         ans=(num,x)
         return ans

    else:
         for i in range(len(lst)):
             if num<= lst[i]:
                 num=lst[i]
                 x=i

         ans=(num,x)
         return ans
