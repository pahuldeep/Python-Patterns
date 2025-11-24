import math

class Point:
    def reset(self) -> None: #
        self.move(0, 0)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def calculate_distance(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y) # euclidean distance 

def main():

    p1 = Point()
    p2 = Point()

    p1.reset()

    p2.move(5, 0)
    print(p2.calculate_distance(p1))

    p1.move(3, 4)
    print(p1.calculate_distance(p2))

    print(p1.calculate_distance(p1))

if __name__ == "__main__":
    main()
