class Node:
    def __init__(self, d):
        self.prev = None
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def addLast(lst, new):
    if lst.head == None:
        lst.head = lst.tail = new
        new.prev = new.next = lst.tail
    else:
        lst.tail.next, new.prev = new, lst.tail
        lst.tail, new.next = new, lst.head

def printList(lst):
    cur, cnt = lst.tail, 0
    while cnt < 10:
        if cur == lst.head or cnt == 9: print(cur.data); break
        else: print(cur.data, end=" ")
        cur = cur.prev
        cnt += 1

for case in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = LinkedList()
    for i in range(n): addLast(result, Node(arr[i]))
    cnt, cur, pre = 0, result.head, result.tail
    while cnt < k:
        for _ in range(m):
            pre, cur = cur, cur.next
        cnt += 1
        new = Node(pre.data+cur.data)
        if cur == result.head:
            addLast(result, new)
            cur = result.tail
        else:
            pre.next = cur.prev = new
            new.prev, new.next = pre, cur
            cur = cur.prev
    print('#{} '.format(case), end="")
    printList(result)