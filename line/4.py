class account:
    def __init__(self, name, money):
        self.name = name
        self.money = money

def solution(snapshots, transactions):
    arr = [0]*snapshots.__len__()
    for i in range(snapshots.__len__()):
        arr[i] = account(snapshots[i][0], int(snapshots[i][1]))
    visit = [0]*106
    for transaction in transactions:
        id_, act, count, money = transaction
        if visit[int(id_)] == 0:
            visit[int(id_)] = 1
            for i in range(snapshots.__len__()):
                if arr[i].name == count:
                    if act == 'SAVE': arr[i].money += int(money)
                    else: arr[i].money -= int(money)
                    break
            else:
                if act == 'SAVE': arr.append(account(count, int(money)))
                else: arr.append(account(count, -int(money)))
    for i in range(len(arr)-1):
        idx = i
        for j in range(i+1, len(arr)):
            if arr[idx].name > arr[j].name:
                idx = j
        arr[idx], arr[i] = arr[i], arr[idx]
    result = []
    for i in range(len(arr)):
        result.append([arr[i].name, str(arr[i].money)])
    return result

snap = [["ACCOUNT1", "100"], ["ACCOUNT2", "150"]]
trans = [
    ["1", "SAVE", "ACCOUNT2", "100"],
    ["2", "WITHDRAW", "ACCOUNT1", "50"],
    ["1", "SAVE", "ACCOUNT2", "100"],
    ["4", "SAVE", "ACCOUNT3", "500"],
    ["3", "WITHDRAW", "ACCOUNT2", "30"]
]
print(solution(snap, trans))