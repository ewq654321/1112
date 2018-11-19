
def type1(f1,f2):

    if f2.strip() == ':':
        begin = '1'
        end = '-1'

    (begin,end) = f2.split(':')

    if begin == '':
        bgein = '1'
    if end == '':
        end = '-1'


    if begin == '1' and end == '-1':
        prompt = '的全文'
    elif begin == '1':
        prompt = '从开始到%s'%end
    elif end == '-1':
        prompt = '从%s到结尾'%begin
    else:
        prompt = '从%s行到%s行'%(begin,end)

    print('\n文件%s%s的内容如下'%(f1,prompt))

    begin1 = int(begin)
    end1 = int(end)
    lines = (end1 - begin1)+1

    f = open(f1)

    for i in range(begin1):
        f.readline()

    if lines < 0 :
        print(f.read())
    else:
        for J in range(lines):
            print(f.readline(),end='')

    f.close()


f1 = input('请输入要打开的文件:')
f2 = input('请输入需要显示的行数【格式如13：21或者：21或21：】：')
print(f1)
print(f2)
type1(f1,f2)












