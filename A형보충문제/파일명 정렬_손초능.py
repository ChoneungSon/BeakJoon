class head_num: # head 부분과 숫자 부분 나누는 클래스 설정
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
        if flag: self.h, self.n = string[:start].upper(), int(string[start:start+cnt])
        else: self.hn = string.upper()

def solution(files):
    list_head_num = [0] * files.__len__()
    for i in range(files.__len__()):
        list_head_num[i] = head_num(files[i])
    for i in range(1, files.__len__()): # 버블 정렬 구현
        j = i
        while j > 0:
            if list_head_num[j-1].h > list_head_num[j].h:
                list_head_num[j-1], list_head_num[j] = list_head_num[j], list_head_num[j-1]
            elif list_head_num[j-1].h == list_head_num[j].h:
                if list_head_num[j-1].n > list_head_num[j].n:
                    list_head_num[j - 1], list_head_num[j] = list_head_num[j], list_head_num[j-1]
            j -= 1
    return [list_head_num[i].string for i in range(files.__len__())]

print(solution(['c4d564848', 'c 45d648407', 'a4564f8407']))
