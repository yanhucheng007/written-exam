def reverse(s):
    index = 0
    str_new = ''
    def test(index,s):
        nonlocal str_new
        if index >= len(s):
            return str_new
        else:
            test(index+1,s)
            str_new += s[index]
    test(index,s)
    return str_new

if __name__ == '__main__':
    str_in = input('请输入需要倒置的字符串:\n')
    print(reverse(str_in))