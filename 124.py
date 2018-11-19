def fileduibi(file1,file2):
    file3 = open(file1,'a')
    file4 = open(file2,'a')
    count = 0
    nono = []
    for f1 in file3:
        f2 = file4.readline()
        count += 1
        if f1 != f2 :
            nono.append(count)

    file3.close()
    file4.close()
    return nono

file1 = input('请输入第一个文件的文件名：')
file2 = input('请输入第二个文件的文件名：')

nono = fileduibi(file1,file2)
if len(nono) ==0 :
    print('两个文件完全一样')
else:
    print('两个文件有%d处不同'%len(nono))
    for hang in nono:
        print('在第%d行不同'%hang)

  # print('不同的地方在%d行'%nono)

