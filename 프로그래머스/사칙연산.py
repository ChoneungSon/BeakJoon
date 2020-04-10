def calcul(num1, num2, op):
    if op == '+': return int(num1) + int(num2)
    else: return int(num1) - int(num2)

def solution(arr):
    result = arr[0]
    for i in range(1, arr.__len__()//2):
        if arr[2*i-1] == '+':
            result += int(arr[2*i])
        else:
            
    return result

print(solution(['5', '-', '3', '+', '1', '+', '2', '-', '4']))