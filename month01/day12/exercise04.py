class Vector2:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return f"x轴的分量是{self.x},y轴的分量是{self.y}"

    def __isub__(self, other):
        if type(other) == Vector2:
            self.x-=other.x
            self.y-=other.y
        else:
            self.x-=other
            self.y-=other
        return self

v1=Vector2(2,3)
v1-=Vector2(1,5)
print(v1)

