
class Point:
    def reset(self):    # self = instance variable of the class
        print(f"Resetting Manually: {self}")
        self.x = 0      # object instance 
        self.y = 0      # object instance

def main():
    p = Point()

    p.reset()       # the instance p is passed implicitly by Python. The method is called on the object (bound). 
    Point.reset(p)  # the instance p is passed explicitly by you. The method is called on the class (unbound).

    print(p.x, p.y)

   
if __name__ == "__main__":
    main()