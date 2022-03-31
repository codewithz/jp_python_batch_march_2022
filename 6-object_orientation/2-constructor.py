class Point:
    color="Red"
    def __init__(self,x,y):
        print("Point Constructor")
        self.x=x;
        self.y=y;

    def draw(self):
        print(f"Point ({self.x} , {self.y})")

print(Point.color)

p1=Point(4,5)
p1.draw()
print(p1.color)
p1.color="Yellow"

Point.color='Green'

p2=Point(5,6)
p2.draw()
print(p2.color)
p2.color='Purple'
print(p2.color)


print(p1.color)

