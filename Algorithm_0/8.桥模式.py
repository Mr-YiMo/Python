from abc import abstractmethod, ABCMeta


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass


class Shape(metaclass=ABCMeta):
    # 将形状和颜色进行组合
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    name = '长方形'
    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    name = '圆形'
    def draw(self):
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print('红色的%s' % shape.name)


class Green(Color):
    def paint(self, shape):
        print('绿色的%s' % shape.name)


shape = Rectangle(Red())
shape.draw()
