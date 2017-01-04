class BankAccount:
    
    def __init__(self, balance = 0.0):
        self.balance = balance 
        
    def withdraw(self, amt):
        self.balance = self.balance - amt

    def deposit(self, amt):
        self.balance = self.balance + amt
        
    def get_balance(self):
        return self.balance

    def __repr__(self):
        return 'BankAccount('+str(self.balance)+')'


class PingPong:

    def __init__(self,s="PONG"):
        self.s=s
        pass

    def next(self):
        if self.s == "PING":
            self.s = "PONG"
            return self.s
        else:
            self.s = "PING"
            return self.s


class Queue:

    def __init__(self, q=[]):
        self.queue = q

    def enqueue(self, s):
        self.queue.append(s)

    def dequeue(self):
        z=self.queue.pop(0)
        return z

    def isEmpty(self):
        return len(self.queue) == 0

    def __eq__(self, other):
        if len(self.queue) == len(other.queue):
            for i in range(len(self.queue)):
                if self.queue[i] != other.queue[i]:
                    return False
            return True
        else:
            return False

    def __repr__(self):
        return 'Queue({})'.format(self.queue)
        

    def __len__(self):
        return len(self.queue)


class Marsupial():

    def __init__(self,color="",pouch=[]):
        self.color=color
        self.pouch=pouch

    def put_in_pounch(self,s):
        self.pouch.append(s)

    def pouch_contents(self):
        return self.pouch[:]

    def __str__(self):
        return 'I am a' + ' ' + str(self.colour) + ' ' + 'Marsupial.'
        
class Kangaroo(Marsupial):
    def __init__(self, colour, xcoord=0, ycoord=0):
        self.lst = []
        self.colour = colour
        self.x = xcoord
        self.y = ycoord

    def jump(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return 'I am a' + ' ' + str(self.colour) + ' ' + 'Kangaroo located at coordinates' + ' ' + '({},{})'.format(self.x, self.y)




class Point():
    
    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point, float, float) -> None
        >>> p=Point(2,3)
        >>> p.x
        >>> 2
        >>> p.y
        >>> 3

        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,float)->None
        set x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,float)->None
        set y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        return a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,float,float)->None
        change the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        'self == other if they have the same coordinates'
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        'return canonical string representation Point(x, y)'
        return 'Point('+str(self.x)+','+str(self.y)+')'


class Points():
    def __init__(self, lst=[]):
        self.lst=lst

    def add(self,x,y):
        self.lst.append(Point(x,y))

    def left_most_point(self):
        if (len(self.lst) !=0):
            left = self.lst[0]
            for item in self.lst:
                if item.x == left.x and item.y < left.y:
                    left = item
                elif item.x < left.x:
                    left = item
            return left
        else:
            return None

    def __len__(self):
        return len(self.lst)

    def __repr__(self):
        return 'Points({})'.format(self.lst)







    
        
