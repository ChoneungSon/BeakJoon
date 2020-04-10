class Node:
    def __init__(self, d):
        self.before = None
        self.next = None
        self.data = d

class LinkedList:
    def __init__(self, d=None):
        self.head = None
        self.tail = None
        self.size = 0

def addAt(lst, idx, new):
    pre, cur = None, lst.head
    for _ in range(idx):
        pre, cur = cur, cur.next
    cur.before, pre.next = new.tail, new.head
    new.head.before, new.tail.next = pre, cur
    lst.size += new.size

def addFirstList(lst, new):
    new.tail.next, lst.head.before = lst.head, new.tail
    lst.head = new.head

def addLast(lst, new):
    if lst.tail == None:
        lst.head = lst.tail = new
    else:
        lst.tail.next, new.before = new, lst.tail
        lst.tail = new

def addLastList(lst, new):
    new.head.before, lst.tail.next = lst.tail, new.head
    lst.tail = new.tail
    lst.size += 1

def printList(lst):
    global n, m
    cur, cnt = lst.tail, 0
    while cnt < 10:
        if cnt == 9: print(cur.data)
        else: print(cur.data, end=" ")
        cur = cur.before
        cnt += 1

def printlist(lst):
    cur, cnt = lst.head, 0
    while cur:
        print(cur.data, end=" ")
        cur = cur.next
        cnt += 1

for case in range(1, int(input())+1):
    n, m = map(int, input().split())
    result = LinkedList()
    for i in range(m):
        arr = list(map(int, input().split()))
        if i == 0:
            for j in range(n): addLast(result, Node(arr[j]))
        else:
            new = LinkedList()
            for j in range(n): addLast(new, Node(arr[j]))
            cur, idx = result.head, 0
            while cur:
                if cur.data > new.head.data:
                    if cur == result.head: addFirstList(result, new)
                    else: addAt(result, idx, new)
                    break
                cur = cur.next
                idx += 1
            if cur == None: addLastList(result, new)
    print('#{} '.format(case), end='')
    printList(result)