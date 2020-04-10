# 단일(단순) 연결리스트
class Node:
    def __init__(self, d, b=None, n=None):
        self.before = b
        self.data = d
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

mylist = LinkedList()

def printList(lst): # lst: LinkedList 객체
    cur = lst.head
    while cur:
        print(cur.data)
        cur = cur.next

def addLast(lst, new):
    if lst.head == None:
        lst.head = lst.tail = new
    else:
        new.before = lst.tail
        lst.tail.next = new
        lst.tail = new
    lst.size += 1

def addFirst(lst, new):
    if lst.head == None:
        lst.head = lst.tail = new
    else:
        new.next = lst.head
        lst.head = new
    lst.size += 1

def addAt(lst, idx, new):
    if idx:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        pre.next, new.before = new, pre
        cur.before, new.next = new, cur
    else:
        new.next = lst.head
        lst.head.before = new
        lst.head = new
    lst.size += 1

def delLast(lst):
    if lst.head == lst.tail:
        lst.head = lst.tail = None
    else:
        lst.tail.before.next = None
        lst.tail = lst.tail.before
    lst.size -= 1

def delFirst(lst):
    if lst.head == lst.tail:
        lst.head = lst.tail = None
    else:
        lst.head.next.before = None
        lst.head = lst.head.next
    lst.size -= 1

def delAt(lst, idx):
    if idx != 0 and idx != lst.size-1:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        pre.next = cur.next
        cur.next.before = pre
    else:
        if idx == 0: delFirst()
        else: delLast()

addFirst(mylist, Node(3))
addFirst(mylist, Node(5))
addAt(mylist, mylist.size-1, Node(4))
delAt(mylist, 1)
printList(mylist)
print()
print(mylist.head.data, mylist.tail.data)