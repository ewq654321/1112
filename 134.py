#读取文件，每三个字符打印一次，间隔1S
import time
with open(r'C:\Users\zheng\Desktop\record.txt','r')as f:
    t = f.read(3)
    print(t)
    while len(t):
        t = f.read(3)
        print(t)
        time.sleep(1)




    # print()

