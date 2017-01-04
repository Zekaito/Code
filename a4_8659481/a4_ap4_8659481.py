#Tyler Tsang
#8659481
#ITI1120
#Assignment 4 part 1


def ap4(m):
    '''
    (list)-->list
    Returns a list of the indexes of where an arithmic system is inside
    of the matrix. If there is none then it returns an empty list



    '''
    flag = False
    scan = 0
    place = []
    
    #row
    for x in range(len(m)):
        for y in range(len(m[0])-3):
            num=m[x][y+1]-m[x][y]
            if m[x][y+3]-m[x][y+2]==num and m[x][y+2]-m[x][y+1]==num:
                flag = True

            if scan==0 and flag==True:
                scan=1
                for z in range(4):
                    place.append([x,(y+z)])


    #col
    for x in range(len(m[0])-1):
        for y in range(len(m)-3):
            num=m[y+1][x]-m[y][x]
            if m[y+3][x]-m[y+2][x]==num and m[y+2][x]-m[y+1][x]==num:
                flag = True

            if scan==0 and flag==True:
                scan=1
                for z in range(4):
                    place.append([(y+z),x])



    #\
    for x in range(len(m)-3):
        for y in range(len(m[0])-3):
            num=m[x+1][y+1]-m[x][y]
            if m[x+3][y+3]-m[x+2][y+2]==num and m[x+2][y+2]-m[x+1][y+1]==num:
                flag = True

            if scan==0 and flag==True:
                scan=1
                for z in range(4):
                    place.append([x+z,y+z])
            
    #/
    for x in range(len(m)-3):
        for y in range(-1,-(len(m[0])-3),-1):
            num= m[x+1][y-1]-m[x][y]
            if m[x+3][y-3]-m[x+2][y-2]==num and m[x+2][y-2]-m[x+1][y-1]==num:
                flag = True

            if scan==0 and flag==True:
                scan=1
                for z in range(4):
                    w=(len(m)+y)+1
                    place.append([x+z,w-z])
        
        

    return place


























    
