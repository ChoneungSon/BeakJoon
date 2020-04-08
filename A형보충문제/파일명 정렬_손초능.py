class head_num:
    def __init__(self, string):
        self.string, flag = string, 0
        for i in range(string.__len__()):
            if flag == 0 and string[i].isdecimal():
                flag, cnt, start = 1, 1, i
            elif flag and string[i].isdecimal():
                cnt += 1
                if cnt == 5: break
            elif flag and not(string[i].isdecimal()):
                break
        if flag: self.hn = (string[:start] + '0'*(5-cnt) + string[start:start+cnt]).upper()
        else: self.hn = string.upper()

def solution(files):
    list_head_num = [0] * files.__len__()
    for i in range(files.__len__()):
        list_head_num[i] = head_num(files[i])
    for i in range(files.__len__()-1):
        idx = i
        for j in range(i+1, files.__len__()):
            if list_head_num[idx].hn > list_head_num[j].hn:
                idx = j
        list_head_num[idx], list_head_num[i] = list_head_num[i], list_head_num[idx]
    return [list_head_num[i].string for i in range(files.__len__())]

print(solution(['a4564848', 'a45648407']))
