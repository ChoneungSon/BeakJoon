class Node:
    def __init__(self, d):
        self.before = None
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

def addLast(lst, new):
    if lst.head == None:
        lst.head = lst.tail = new
    else:
        new.before = lst.tail
        lst.tail.next = new
        lst.tail = new
    lst.size += 1

def addAt(lst, idx, new):
    if idx == 0:
        lst.head.before = new
        new.next = lst.head
        lst.head = new
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        pre.next, new.before = new, pre
        cur.before, new.next = new, cur
    lst.size += 1

def delAt(lst, idx):
    if idx == 0 or idx == lst.size-1:
        if idx == 0:
            lst.head = lst.head.next
            lst.head.before = None
        else:
            lst.tail = lst.tail.before
            lst.tail.next = None
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        pre.next = cur.next
        cur.next.before = pre
    lst.size -= 1

def change(lst, idx, value):
    cur = lst.head
    for i in range(idx):
        cur = cur.next
    cur.data = value

def printlist(lst):
    cur = lst.head
    while cur:
        print(cur.data, end=' ')
        cur = cur.next
    print()

for case in range(1, int(input())+1):
    n, m, l = map(int, input().split())
    arr = list(map(int, input().split()))
    mylist = LinkedList()
    for i in range(n):
        addLast(mylist, Node(arr[i]))
    for _ in range(m):
        c = list(input().split())
        if c[0] == 'I':
            if mylist.size <= int(c[1]):
                addLast(mylist, Node(int(c[2])))
            else:
                addAt(mylist, int(c[1]), Node(int(c[2])))
        elif c[0] == 'D':
            delAt(mylist, int(c[1]))
        else:
            change(mylist, int(c[1]), int(c[2]))
        printlist(mylist)
    if mylist.size <= l: result = -1
    else:
        cur = mylist.head
        for _ in range(l):
            cur = cur.next
        result = cur.data
    print('#{} {}'.format(case, result))