def linear_search_v1(lst,value):
    i=-1
    while -i != len(lst) and lst[i] != value:
          i=i-1

    if -i == len(lst):
          return -1
    else:
        z=(len(lst)+i)
        return z

def linear_search_v2(lst, value):

     for i in range(len(lst)):
          if lst[-i] == value:
               z=(len(lst)-i)
               return z
     return -1


def linear_search_v3(lst, value):

    lst.insert(0,value)
    i=-1

    while lst[i] != value:
          i=i-1

    lst.pop(0)

    if -i == len(lst):
          return -1
    else:
        z=(len(lst)+i)
        return z
