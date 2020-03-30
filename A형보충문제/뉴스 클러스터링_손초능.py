def solution(str1, str2):
    string1, string2 = change2str(str1), change2str(str2)
    total, cnt = len(string1) + len(string2), 0
    for i in range(len(string1)):
        for j in range(len(string2)):
            if string1[i] == string2[j]:
                string2.pop(j)
                total -= 1
                cnt += 1
                break
    if string1 or string2:
        return (cnt * 65536) // total
    else: return 65536

def change2str(string):
    n, list_str, i = len(string), [], -1
    for i in range(n-1):
        if string[i:i+2].isalpha():
            list_str.append(string[i:i+2].upper())
    return list_str

print(solution('FRANCE', 'french'))