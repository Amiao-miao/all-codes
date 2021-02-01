"""
重写range函数，要求重写之后的myrange(5)输出结果为:5,4,3,2,1,0
"""
class Iterator:
    def __init__(self,start):
        self.start=start+1
    def __next__(self):
        self.start-=1
        if self.start<0:
            raise StopIteration
        return self.start


mr=MyRange(5)
iterator=mr.__iter__()
while True:
    try:
        i=iterator.__next__()
        print(i)
    except StopIteration:
        break
