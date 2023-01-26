class Points():

    def __init__(self, x, y):
        self.x=x
        self.y=y

x=int(input("x: "))
y=int(input("y: "))
p1 = Points(x,y)
print(p1.x)
print(p1.y)