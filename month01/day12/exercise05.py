"""
    实现自定义
"""
class Color:
    def __init__(self, r, g, b):
        self.r=r
        self.g=g
        self.b=b

    def __str__(self):
        return f"{self.r},{self.g},{self.b}"

    def __gt__(self, other):
        return self.r+self.g+self.b>other.r+other.g+other.b

    def __eq__(self, other):
        return self.r==other.r

list_color=[
    Color(100,200,100),
    Color(200,100,150),
    Color(90,0,0),
]
print(max(list_color))
list_color.remove(Color(90,0,0))
# for item in list_color:
#     print(item)