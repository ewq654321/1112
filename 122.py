f1 = input('请输入需要打开的文件（c:\\tese.txt）:')
f2 = int(input('请输入需要显示该文件前几行：'))
def dakai(f1,f2):
    f3 = open(f1)
    count = 0
    for hang in f3:
        print(hang)
        count+=1
        if count >= f2:
            f3.close()
            break
dakai(f1,f2)


# def file_view(file_name, line_num):
#     print('\n文件%s的前%s的内容如下：\n' % (file_name, line_num))
#     f = open(file_name)
#     for i in range(int(line_num)):
#         print(f.readline(), end='')
#
#     f.close()
#
#
# file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
# line_num = input('请输入需要显示该文件前几行：')
# file_view(file_name, line_num)
