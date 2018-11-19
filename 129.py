
import os
def search_file(start_dir,target):
    os.chdir(start_dir)

    for each_file in os.listdir(start_dir):
        if each_file == target:
            print(os.getcwd()+os.sep+each_file)
        if os.path.isdir(each_file):
            search_file(each_file,target)#####这里特别要注意对第一个参数进行调用时，是否会造成无限循环。
            os.chdir(os.pardir)

start_dir = input('请输入需要查询的目录：')
target = input('请输入查询的文件名：')
search_file(start_dir,target)

# import os


# def search_file(start_dir, target):
#     os.chdir(start_dir)
#
#     for each_file in os.listdir(os.curdir):
#         if each_file == target:
#             print(os.getcwd() + os.sep + each_file)  # 使用os.sep是程序更标准
#         if os.path.isdir(each_file):
#             search_file(each_file, target)  # 递归调用
#             os.chdir(os.pardir)  # 递归调用后切记返回上一层目录
#
#
# start_dir = input('请输入待查找的初始目录：')
# target = input('请输入需要查找的目标文件：')
# search_file(start_dir, target)
