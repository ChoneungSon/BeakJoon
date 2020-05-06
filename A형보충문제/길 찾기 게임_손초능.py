import sys
sys.setrecursionlimit(1001)
class Node:
    def __init__(self, idx, x, y):
        self.idx = idx
        self.left = None
        self.right = None
        self.point = [x, y]

def solution(nodeinfo):
    nodeinfo = [(y[0]+1, y[1][0], y[1][1]) for y in sorted(enumerate(nodeinfo), key=lambda x : (-x[1][1], x[1][0]))]
    head = Node(nodeinfo[0][0], nodeinfo[0][1], nodeinfo[0][2])
    answer, cnt_pre, cnt_post = [[0]*len(nodeinfo) for _ in range(2)], 0, 0
    for i in range(1, len(nodeinfo)):
        start = head
        while start:
            if nodeinfo[i][1] > start.point[0]:
                if start.left: start = start.left
                else: start.left = Node(nodeinfo[i][0], nodeinfo[i][1], nodeinfo[i][2]); break
            else:
                if start.right: start = start.right
                else: start.right = Node(nodeinfo[i][0], nodeinfo[i][1], nodeinfo[i][2]); break
    def print_sort(head):
        nonlocal answer, nodeinfo, cnt_pre, cnt_post
        if head:
            answer[0][cnt_pre] = head.idx
            cnt_pre += 1
            print_sort(head.right)
            print_sort(head.left)
            answer[1][cnt_post] = head.idx
            cnt_post += 1
    print_sort(head)
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))