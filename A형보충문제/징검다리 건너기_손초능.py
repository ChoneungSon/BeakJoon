def solution(stones, k):
    min_value = max(stones[:k])
    for i in range(k, len(stones)):
        min_value = min(min_value, max(stones[i:k+i]))
    return min_value