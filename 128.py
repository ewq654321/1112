import os

file2 = os.listdir(os.curdir)

file_dict = dict()
for each_file2 in file2:
    # print(each_file2,os.path.getsize(each_file2))
    print('%s【%s Bytse】'%(each_file2,(os.path.getsize(each_file2))))
