"""

"""

def print_file(filename):
    file=open(filename)
    while True:
        data=file.read(1024)
        # if data=="":
        if not data:
            break
        #每次打印不换行 end=""
        print(data,end="")
    file.close()

print_file("3.txt")