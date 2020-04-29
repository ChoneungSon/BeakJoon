for case in range(1, int(input())+1):
    n, hexa = input().split()
    nums = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    result = ''
    for i in range(int(n)):
        num = ''
        for j in range(4):
            if nums[hexa[i]] & 1<<j: num = '1' + num
            else: num = '0' + num
        result += num
    print('#{} {}'.format(case, result))