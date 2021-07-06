from dataclasses import dataclass
from math import sin, cos, pi
@dataclass
class Point2D:
    x: float
    y: float
    def __eq__ (self, other):
        return (isinstance(other , Point2D) and
                self.x == other.x and self.y == other.y)

    def __add__(self, other: 'Point2D') -> 'Point2D':
        return Point2D(self.x + other.x, self.y + other.y)

    def turn(self, phi: float):
        self.x, self.y = (self.x * cos(phi) - self.y * sin(phi)
                        ,self.x * sin(phi) + self.y * cos(phi))

@dataclass
class Rectangle:
    """
    Inveriant: bottom_left x and y coords must be smaller than top_right x and y coords
    """
    __bottom_left : Point2D
    __top_right : Point2D

    def __post_init__(self):
        assert(self.__bottom_left.x < self.__top_right.x and self.__bottom_left.y < self.__top_right.y)
    @property
    def bottom_left(self):
        return self.__bottom_left

    @property
    def top_right(self):
        return self.__top_right

    def area(self):
        return float((self.top_right.x - self.__bottom_left.x) * (self.top_right.y - self.__bottom_left.y))

    def __eq__(self,other):
        return (isinstance,other, Point2D) and self.__bottom_left.x == other.__bottom_left and self.__bottom_left.y == other.__bottom_left.y and self.__top_right.x == other.__top_right.x and self.__top_right.y == other.__top_right.y

    def turn_center(self,phi:float):
        middle_x = (self.__bottom_left.x + self.__top_right.x)//2
        middle_y = (self.__bottom_left.y + self.__top_right.y)//2
        old_mid = Point2D(middle_x,middle_y)
        a = Point2D(middle_x,middle_y)
        a.turn(phi)
        old_bl = self.__bottom_left
        old_tr = self.__top_right
        new_bl_x = a.x - old_mid.x - old_bl.x
        new_bl_y = a.y - old_bl.y - old_mid.y
        print(a.y)
        print(old_mid.y)
        print(old_bl.y)
        new_tr_x = a.x - old_mid.x + old_tr.x
        new_tr_y = a.y - old_mid.y + old_tr.y
        self.__bottom_left.x,self.__bottom_left.y, self.__top_right.x,self.__top_right.y = new_bl_x,new_bl_y,new_tr_x,new_tr_y


rect = Rectangle(Point2D(0, -1), Point2D(2,1))
#print(rect.bottom_left)
#print(rect.area())
#rect2 = Rectangle(Point2D(0,-1), Point2D(2,2))
#print(rect == rect2)
rect.turn_center(pi/2)
print(rect.top_right)
print(rect.bottom_left)
