class Vector2:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return f"x轴的分量是{self.x},y轴的分量是{self.y}"

    def __sub__(self, other):
        if type(other) == Vector2:
            x=self.x-other.x
            y=self.y-other.y
        else:
            x=self.x-other
            y=self.y-other
        return Vector2(x,y)

v1=Vector2(2,3)
v2=Vector2(1,5)
v3=v1-v2
v4=v1-10
print(v3)
print(v4)
