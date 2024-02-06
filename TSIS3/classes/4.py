class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f"First point : {self.x}\nSecond point : {self.y}")
    def move(self,New_x,New_y):
        self.x=New_x
        self.y=New_y
    def dist(self):
        return abs(self.x-self.y)
Coord=Point(1,2)
Coord.show()
Coord.move(3,4)
Coord.show()
print(Coord.dist())