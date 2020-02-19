n = int(input())
stack = []
stack_num = []
list_pop = [0]*n
for i in range(n):
    list_pop[i] = int(input())

k = 0
for i in range(1, n+1):
    if i <= list_pop[k]:
        stack_num.append(i)
        stack.append('+')
        if i == list_pop[k]:
            while len(stack_num) != 0 and stack_num[-1] >= list_pop[k]:
                stack_num.pop()
                stack.append('-')
                k += 1
    if k == n:
        break
if k == n:
    while len(stack_num) != 0:
        stack_num.pop()
        stack.append('-')
    for i in range(len(stack)):
        print(stack[i])
else:
    print('NO')