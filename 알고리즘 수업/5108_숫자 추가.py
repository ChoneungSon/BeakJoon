class LinkedList:
    def __init__(self, d, n=None):
        self.cur = id(self)
        self.data = d
        self.next = n

for case in range(1, int(input())+1):
    n, m, l = map(int, input().split())
    arr = list(map(int, input().split()))
    node = LinkedList(arr[0])
    head = node
    for i in range(1, n):
        node.next = LinkedList(arr[i])
        node = node.next
    for _ in range(m):
        idx, value = map(int, input().split())
        cnt, find_node = 0, head
        while cnt < idx-1:
            cnt += 1
            find_node = find_node.next
        append = LinkedList(value)
        append.next = find_node.next
        find_node.next = append
    cnt, find_node = 0, head
    while cnt < l:
        cnt += 1
        find_node = find_node.next
    print('#{} {}'.format(case, find_node.data))
