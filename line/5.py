class tag_num:
    def __init__(self, name):
        self.name = name
        self.cnt = 0

def solution(dataSource, tags):
    arr = [0]*len(dataSource)
    for i in range(len(dataSource)):
        arr[i] = tag_num(dataSource[i][0])
        for j in range(1, len(dataSource[i])):
            if dataSource[i][j] in tags:
                arr[i].cnt += 1
    for i in range(min(len(dataSource), 10)):
        idx = i
        for j in range(i+1, len(dataSource)):
            if arr[idx].cnt < arr[j].cnt:
                idx = j
            elif arr[idx].cnt == arr[j].cnt:
                if arr[idx].name > arr[j].name:
                    idx = j
        arr[idx], arr[i] = arr[i], arr[idx]
    result = []
    for i in range(min(len(dataSource), 10)):
        if arr[i].cnt:
            result.append(arr[i].name)
    return result

data = [
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
]
tags = ["t1", "t2", "t3"]

print(solution(data, tags))