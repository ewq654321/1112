# import os
# import pickle
#
# file_name1 = input('请输入源文件地址：')
# str1 = input('请输入需要打印的对话者一名字：')
# str2 = input('请输入需要打印的对话者二名字：')
#
# def search_file(file_name1, str1, str2 ):
#     aa = []
#     bb = []
#     f1 = open(file_name1)
#     f2 = open('boy_1.txt','wb')
#     f3 = open('girl_1.txt','wb')
#     for each_line in f1:
#         if str1 in each_line:
#             each_line.replace(str1, '')
#             aa= each_line
#             pickle.dump(aa, f2)
#         if str2 in each_line:
#             each_line.replace(str2, '')
#             bb = each_line
#             pickle.dump(bb, f3)
#     f2.close()
#     f3.close()
#     f1.close()
#
#
#
# search_file(file_name1, str1, str2 )
# f4 = open('boy_1.txt','rb')
# f5 = pickle.load(f4)
# print(f5)


import pickle


def save_file(boy, girl, count):
    boy_file = 'boy_' + str(count) + '.txt'
    girl_file = 'girl' + str(count) + '.txt'

    boy_file1 = open(boy_file,'wb')
    girl_file2 = open(girl_file,'wb')

    pickle.dump(boy, boy_file1)
    pickle.dump(girl, girl_file2)

    boy_file1.close()
    girl_file2.close()




























