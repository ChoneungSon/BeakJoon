def solution(stones, k):
    stones_tuples = [(stones[i], i) for i in range(len(stones))]
    sorted_tuples = sorted(stones_tuples, key=lambda lst:lst[0], reverse=True)
    idx = 0
    for i in range(k-1, len(stones)):
        if stones[i] < sorted_tuples[idx][0]:
            if sorted_tuples[idx][1] < i-k+1:
                p = idx
                while p < len(stones)-1:
                    p += 1
                    if p > len(stones) - k - 1: break
                    elif i-k+1 <= sorted_tuples[p][1] <= i:
                        if p > idx: idx = p; break
    return sorted_tuples[idx][0]

def solution2(stones, k):
    if k == 1:
        min_maxvalue = min(stones)
    else:
        max_value, second_value = max12(stones[:k])
        min_maxvalue = max_value
        for i in range(1, k+1):
            if stones[i-1] == max_value and stones[i+k-1] > second_value:
                max_value, second_value = max12(stones[i:i+k])
                min_maxvalue = min(min_maxvalue, max_value)
    return min_maxvalue

def max12(arr):
    for i in range(2):
        idx = i
        for j in range(i+1, len(arr)):
            if arr[idx] < arr[j]: idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr[0], arr[1]

print(solution2([1,1,1,1, 2, 4, 5, 3, 2, 1, 4, 2, 5, 1,1,1,1,1,1,1,1,1,1,1,1], 3))
print(solution2([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],	3))
