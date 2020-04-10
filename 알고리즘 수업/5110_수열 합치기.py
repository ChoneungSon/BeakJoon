class LinkedList:
    def __init__(self, d=None):
        self.front = None
        self.data = d
        self.back = None

def append(node, add):
    front, back = node, node.back
    add_head = add
    while add.back:
        add = add.back
    add_tail = add
    add_head.front, back.front = front, add_tail
    front.back, add_tail.back = add_head, back

# for case in range(1, int(input())+1):
a = [1, 2, 3]
A = LinkedList()
A.head = A.tail = A
B = A.head
for i in range(3):

while A:
    if A.data: print(A.data)
    A = A.back