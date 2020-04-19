def solution(n, arr1, arr2):
    def change2bi(num): # 이진수로 바꾸는 함수
        nonlocal n
        result = ''
        for i in range(n):
            if num & (1<<i): result = '1' + result
            else: result = '0' + result
        return result
    for i in range(n):
        arr1[i] = change2bi(arr1[i])
        arr2[i] = change2bi(arr2[i])
    answer = ['' for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1': answer[i] += '#' # 둘 중 하나가 벽일 때
            else: answer[i] += ' ' # 둘 다 벽이 아닐 때
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))