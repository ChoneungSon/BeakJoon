def solution(nums):
    n = len(nums)
    m, visit, cnt = n//2, [0]*(max(nums)+1), 0
    for i in range(n):
        if visit[nums[i]] == 0: cnt += 1
        visit[nums[i]] += 1
    if cnt >= m: return m
    else: return cnt

print(solution([3,3,3,2,2,4]))