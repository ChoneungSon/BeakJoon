# 이분 탐색 이용
# n = int(input())
# arr = list(map(int, input().split()))
import time
t = time.time()
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
maxlen_arr = [1000000001] + [0]*n
front = 0
for i in range(n):
    if maxlen_arr[front] < arr[i]:
        front += 1
        maxlen_arr[front] = arr[i]
    else:
        left, right = 0, front
        while left != right:
            mid = (right+left)//2
            if maxlen_arr[mid] < arr[i]: left=mid+1
            else: right=mid
        maxlen_arr[right] = arr[i]
    print(maxlen_arr)
print(n - front-1)
print(time.time()-t)

# 세그먼트 트리
# class Node:
#     def __init__(self):
#         self.child = []
#         self.sum = 0
#
# def make_tree(start, end):
#     global arr
#     if start == end:
#         leaf = Node()
#         leaf.sum = arr[start]
#         return leaf
#     else:
#         mid = (start+end)//2
#         leaf = Node()
#         leaf.child.append(make_tree(start, mid))
#         leaf.child.append(make_tree(mid+1, end))
#         leaf.sum = leaf.child[0].sum + leaf.child[0].sum
#         return leaf
#
# n = int(input())
# arr = list(map(int, input().split()))
# head = make_tree(0, len(arr)-1)