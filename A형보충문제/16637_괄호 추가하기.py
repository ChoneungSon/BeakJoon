import sys
def cal(num1, num2, op):
    if op == '+': return num1 + num2
    elif op == '-': return num1 - num2
    else: return num1 * num2

def dfs(state, total):
    global n, eq, max_total
    if state == n-1: max_total = max(max_total, total)
    else:
        dfs(state+2, cal(total, int(eq[state+2]), eq[state+1]))
        if state + 4 <= n-1:
            dfs(state+4, cal(total, cal(int(eq[state+2]), int(eq[state+4]), eq[state+3]), eq[state+1]))

n = int(sys.stdin.readline())
eq = sys.stdin.readline()
max_total = -2**31
dfs(0, int(eq[0]))
print(max_total)