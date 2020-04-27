class node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next



def solution(k, room_number):
    head = node(value=room_number[0])
    pre, fro = None, head
    for i in range(1, len(room_number)):
        if fro.value > room_number[i]: pre, fro = None, head
        while fro:
            if fro.value > room_number[i]:
                new = node(value=room_number[i])
                if pre: pre.next = new; new.next = fro;
                else: head = new; new.next = fro;
                pre = new;
                break
            elif fro.value == room_number[i]:
                room_number[i] += 1
            pre = fro; fro = fro.next
        if fro == None:
            pre.next = node(value=room_number[i])
            pre, fro = None, head
    return room_number

def solution2(k, room_number):
    rooms = dict()
    for i in range(len(room_number)):
        num = room_number[i]
        while 1:
            if num not in rooms: # num 이 rooms에 존재하지 않는 경우
                rooms[num] = num + 1
                room_number[i] = num
                break
            temp = num # num 이 rooms에 존재하는 경우
            num = rooms[num]
            if rooms.get(num): rooms[temp] = rooms[num] + 1
    return room_number


import sys

sys.setrecursionlimit(10000000)  # 설정해주지 않으면 재귀가 많이 일어나면서 런타임에러 등이 나타날 수 있다.


def findEmptyRoom(number, rooms):  # 빈방을 찾는 함수
    if number not in rooms:
        rooms[number] = number + 1
        return number

    empty = findEmptyRoom(rooms[number], rooms)
    rooms[number] = empty + 1
    return empty


def solution3(k, room_number):
    answer = []
    rooms = dict()  # 몇번 방이 비어있는지 체크하는 딕셔너리

    for number in room_number:
        emptyRoom = findEmptyRoom(number, rooms)
        answer.append(emptyRoom)

    return answer

print(solution2(10, [1]*200000))