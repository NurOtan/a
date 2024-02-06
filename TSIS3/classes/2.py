class shape:
    def area(self):
        print(0)
class Square(shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        print(self.length*self.length)
Sq1=shape()
Sq1.area()