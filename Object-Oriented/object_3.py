# initializer and contructor are different 
# e.g. 
# __new__() = constructor
# __init__() = initializer

import math

class Point:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        """ Initialize position: 
        x: float x with default value
        y: float y with default value """
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        self.x = x  
        self.y = y
    
    def reset(self) -> None:
        self.move(0, 0)

    def calculate_distance(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)
    
p = Point(3, 4)
q = Point()

print(p.x, p.y)
print(p.calculate_distance(q))