import sys, math

def make_tree(n, start, end):
    global arr, nodes
    if start == end:
        nodes[n] = arr[start]
        return nodes[n]
    else:
        mid = (start+end)//2
        nodes[n] = make_tree(n*2+1, start, mid) + make_tree(n*2+2, mid+1, end)
        return nodes[n]

def find_leaf(n, start, end, x, add):
    global nodes
    nodes[n] += add
    if start == end: return
    else:
        mid = (start+end)//2
        if x <= mid: find_leaf(n*2+1, start, mid, x, add)
        else: find_leaf(n*2+2, mid+1, end, x, add)

def find_sum(n, start, end, s, e):
    if start > e or end < s: return 0
    if start>=s and end<=e: return nodes[n]
    mid = (start+end)//2
    return find_sum(n*2+1, start, mid, s, e) + find_sum(n*2+2, mid+1, end, s, e)

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
nodes = [0]*(1 << math.ceil(math.log(n, 2))+1)
nodes[0] = make_tree(0, 0, n-1)
for _ in range(m):
    q, a, b = map(int, input().split())
    if q == 1: print(find_sum(0, 0, n-1, a-1, b-1))
    elif q == 2: find_leaf(0, 0, n-1, a-1, b)
    else: find_leaf(0, 0, n-1, a-1, -b)