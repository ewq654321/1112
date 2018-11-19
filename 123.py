def file1(file_name):
    f = open(file_name,'a')
    print('输入:w时，结束文本输入。')

    while True:
        sr = input()
        if ':w'in sr:
            break
        else:
            f.write('%s\n'% sr)
    f.close()
    print('文件已关闭，并保存。')


file_name = input('请输入文件名：')
file1(file_name)