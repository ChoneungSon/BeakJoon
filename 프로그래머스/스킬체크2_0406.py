def solution(stones, k):
    n, min_value, i, cnt = len(stones), max(stones)+1, 0, 1
    while i <= n-k:
        for j in range(1, k):
            if stones[i+j] > stones[i]:
                i = i+j-1
                break
        else:
            if min_value > stones[i]:
                min_value = stones[i]
        i += 1
    return min_value


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))