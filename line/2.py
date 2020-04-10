def solution(answer_sheet, sheets):
    n, max_value = answer_sheet.__len__(), 0
    for i in range(sheets.__len__()-1):
        for j in range(i+1, sheets.__len__()):
            i, j = 0, 2
            continue_str, cnt, length = 0, 0, 0
            for k in range(n):
                if sheets[i][k] == sheets[j][k] and sheets[i][k] != answer_sheet[k]:
                    cnt += 1
                    length += 1
                else:
                    if continue_str < length:
                        continue_str = length
                    length = 0
            continue_str = max(continue_str, length)
            value = cnt + continue_str**2
            if value > max_value:
                max_value = value
    return max_value

print(solution("4132315142", ["3241523133","4121314445","3243523133","4433325251","2412313253"]))
print(solution("53241",	["53241", "42133", "53241", "14354"]))
print(solution("24551",	["24553", "24553", "24553", "24553"]))