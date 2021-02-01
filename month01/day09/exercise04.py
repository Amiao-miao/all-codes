
#创建类
class wife:
    """
    自定义类-老婆
    """

# 数据
    def __init__(self, name, face_score=0, money=0):
        self.name = name
        self.face_score = face_score
    # 创建参数快捷键：alt+回车
        self.money = money

#行为
    def play(self):
        print(self.name+"在玩")

jianning=wife("建宁",93,10000)
print(jianning.money)