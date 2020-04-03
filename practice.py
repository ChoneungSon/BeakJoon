def define(m):
    length = 0
    while m != 0:
        length += 1
        if m % 10 == 1:
            m //= 10
        else: return 0
    return length

def find(m):
    num = '1'
    while 1:
        if int(num+'1') > m:
            return int(num)
        num += '1'

print(find(110))