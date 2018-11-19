import os


def search_file(start_dir,target):
    os.chdir(start_dir)
    f1 = os.listdir(os.curdir)

    for each_file in f1:
        tt = str(os.path.splitext(each_file)[1])
        if tt in target:
            vedio_list.append(os.getcwd()+os.sep+each_file)
        if os.path.isdir(each_file):
            search_file(each_file,target)
            os.chdir(os.pardir)


start_dir = input('请输入需要查找的目录：')
aa = os.getcwd()
target = ['.mp4','.avi','.rmvb','.3gp']
vedio_list = []

search_file(start_dir,target)

f2 = open(aa+os.sep+'vedio_list.txt','w')
f2.writelines(vedio_list)
f2.close()
