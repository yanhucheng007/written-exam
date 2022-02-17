import sys

list_in = sys.argv[1:]
temp = []
for s in list_in:
    if s.isdigit():
        temp.insert(0,s)
    elif s in '+-*/':
        new = eval(temp[1]+s+temp[0])
        del temp[0]
        del temp[0]
        temp.insert(0, str(new))
    else:
        print('输入有误！')
        exit()
print(temp[0])