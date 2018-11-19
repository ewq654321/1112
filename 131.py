# file_str = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
# p = input('请问是否需要打印关键字【%s】在文件中的具体位置（yes/no）:'%file_str)
#
# import os
# n = len(file_str)
# t = ['.txt']
# def search_str(file_str,p):
#     f1 = os.listdir(os.curdir)#输出目录下文件
#
#     for each_file in f1:
#         ext = os.path.splitext(each_file)[1]
#         if ext in t:
#             q = str(os.getcwd()+os.sep+each_file)
#             f2 = open(os.getcwd()+os.sep+each_file)#打开。txt文件
#             print('在文件【{0}】中找到关键字【{1}】'.format(q,file_str))
#             count = 0
#             for each in f2:
#                 count += 1
#                 if file_str in each:
#                     a = []
#                     a = each.find(file_str)
#                     if p == 'yes':
#                         print('该字在第{0}行，第{1}处'.format(count,a))
#                         os.chdir(os.pardir)
#         if os.path.isdir(each_file):
#             search_str(file_str,p)
#
# search_str(file_str,p)
#
import os


def print_dict(key_dict):
    keys = key_dict.keys()
    keys = sorted(keys)
    for each_key in keys:
        print('关键字出现在第%s行，第%s个位置'%(each_key,str(key_dict[each_key])))


def p_in_line(line,key):
    p_p = []
    b = line.find(key)
    while b != -1 :
        p_p.append(b + 1)
        b =line.find(key, b + 1)

    return p_p


def search_in_file(file_name, key):
    f = open(file_name)
    count = 0
    key_dict = dict()

    for each_file in f:
        count += 1
        if key in each_file:
            p_p = p_in_line(each_file, key)
            key_dict[count] = p_p

    f.close()
    return key_dict


def search_file(key,datail):
    all_files = os.walk(os.getcwd())
    txt_files = []

    for i in all_files:
        for each_files in i[2]:
            if os.path.splitext(each_files)[1] == '.txt':
                each_files = os.path.join(i[0],each_files)
                txt_files.append(each_files)

    for each_txt_file in txt_files:
        key_dict = search_in_file(each_txt_file, key)

        if key_dict:
            print('------------')
            print('在文件【%s】中找到关键字【%s】'%(each_txt_file,key))
            if detail in ['yes','Yes','YES']:
                print_dict(key_dict)

key = input('请将该脚本放于待查找的文件夹内，请输入关键字:')
detail = input('请问是否需要打印关键字【%s】在文件中的具体位置【yes/no】'%key)
search_file(key, detail)

# import os
#
#
# def print_pos(key_dict):
#     keys = key_dict.keys()
#     keys = sorted(keys)  # 由于字典是无序的，我们这里对行数进行排序
#     for each_key in keys:
#         print('关键字出现在第 %s 行，第 %s 个位置。' % (each_key, str(key_dict[each_key])))
#
#
# def pos_in_line(line, key):
#     pos = []
#     begin = line.find(key)
#     while begin != -1:
#         pos.append(begin + 1)  # 用户的角度是从1开始数
#         begin = line.find(key, begin + 1)  # 从下一个位置继续查找
#
#     return pos
#
#
# def search_in_file(file_name, key):
#     f = open(file_name)
#     count = 0  # 记录行数
#     key_dict = dict()  # 字典，用户存放key所在具体行数对应具体位置
#
#     for each_line in f:
#         count += 1
#         if key in each_line:
#             pos = pos_in_line(each_line, key)  # key在每行对应的位置
#             key_dict[count] = pos
#
#     f.close()
#     return key_dict
#
#
# def search_files(key, detail):
#     all_files = os.walk(os.getcwd())
#     txt_files = []
#
#     for i in all_files:
#         for each_file in i[2]:
#             if os.path.splitext(each_file)[1] == '.txt':  # 根据后缀判断是否文本文件
#                 each_file = os.path.join(i[0], each_file)
#                 txt_files.append(each_file)
#
#     for each_txt_file in txt_files:
#         key_dict = search_in_file(each_txt_file, key)
#         if key_dict:
#             print('================================================================')
#             print('在文件【%s】中找到关键字【%s】' % (each_txt_file, key))
#             if detail in ['YES', 'Yes', 'yes']:
#                 print_pos(key_dict)
#
#
# key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
# detail = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：' % key)
# search_files(key, detail)
#

































