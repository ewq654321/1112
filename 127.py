import os

file1 = os.listdir(os.curdir)
type_dict = dict()
for each_file1 in file1:
    if os.path.isdir(each_file1):
        type_dict.setdefault('文件夹',0)
        type_dict['文件夹'] +=1
    else:
        a = os.path.splitext(each_file1)[1]
        type_dict.setdefault(a,0)
        type_dict[a] +=1

for type_name in type_dict.keys():
    print('这个目录中%s类型的文件有%s个'%(type_name,type_dict[type_name]))


