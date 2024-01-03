from abc import abstractmethod,ABCMeta

class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

class Point(Graphic):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return '点(%s,%s)' % (self.x,self.y)

    def draw(self):
        print(str(self))

class Line(Graphic):
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return '线段[%s,%s]' % (self.p1,self.p2)

    def draw(self):
        print(str(self))

# realize a complicated object
class Picture(Graphic):
    def __init__(self,iterable):
        self.children = [] #record child node
        for g in iterable:
            self.add(g)

    def add(self,graphic):
        self.children.append(graphic)

    def draw(self):
        print('complicated graphic')
        for g in self.children:
            g.draw()
        print('complicated graphic')

l1 = Line(Point(3,4),Point(6,7))
l2 = Line(Point(1,5),Point(2,8))
pict1 = Picture([l1,l2])
pict1.draw()
