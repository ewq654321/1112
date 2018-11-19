# # f.readlines()
# #
# # str.count()
# # str.replace()
# ##########这个是29课的作业4练习题。
# def TH(file1,no1,no2):         #file1为文件名   no1为需要替换的旧字符    no2为需要替换的新字符
#
#
#     f = open(file1)
#     w = f.readlines()
#     w = str(w)######这里是把上一行文件输出的列表强制转换成字符串
#
#     S = w.count(no1)#####对旧的字符进行计数
#     print('文件%s中共有%s个【%s】'%(file1,S,no1))
#     print('您确定要把所有的%s替换为%s吗？'%(no1,no2))
#     Y = input('[yes/no]:')
#     if Y == 'yes':
#         f2 = open(file1,'w+')####这里看了‘小甲鱼’的代码很有启发，重新打开一遍，然后清除文件内容，在接着写入。
#         f2.write(w.replace(no1,no2))
#         f2.close()
#     else:
#         print('退出程序！')
#     f.close()
#
#
# file1=input('请输入文件名：')
# no1 = input('请输入需要替换的单词或字符：')
# no2 = input('请输入新的单词或字符：')
# TH(file1,no1,no2)


def file_TH(file_name,rep,new):
    f1 = open(file_name)

    content = []
    count = 0
    count1 = 0

    for line in f1:
        if rep in line:
            count = line.count(rep)
            line = line.replace(rep,new)
            count1 = count1 + count
        content.append(line)

    jieshou = input('文件%s中共有%s个【%s】您确定要把所有的【%s】替换为【%s】吗？yes/no:'%(file_name,count1,\
                                                             rep,rep,new))
    if jieshou in ['Yes','yes','YES']:
        f2 = open(file_name,'w')
        f2.writelines(content)
        f2.close()

    f1.close()

file_name = input('请输入文件名：')
rep = input('请输入需要替换的字：')
new = input('请输入新的单词或者字符：')
file_TH(file_name,rep,new)























