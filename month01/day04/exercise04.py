"""
    程序产生1个,1到100之间的随机数。
    让玩家重复猜测,直到猜对为止。
    每次提示：大了、小了、恭喜猜对了,总共猜了多少次。
    超过3次就失败
"""
import random #准备随机数工具
random_number=random.randint(1,100) #产生一个随机数
count=0
while count<3:
    count+=1
    num = int(input("请输入要猜的数字："))
    if num<random_number:
        print("小了")
    elif num>random_number:
        print("大了")
    else:
        print("恭喜猜对了,总共猜了"+str(count)+"次")
        break
else:#结束循环有两个可能的时候
    #循环条件不满足才执行（break结束的循环不执行）
    print("游戏失败")