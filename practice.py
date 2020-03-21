def solution(strs, t):
    m, n = len(strs), len(t)
    nums, stack = [0] * m, []
    for i in range(m):
        nums[i] = len(strs[i])
    for i in range(m-1):
        for j in range(i+1, m):
            if nums[i] > nums[j]:
                strs[i], strs[j], nums[i], nums[j] = strs[j], strs[i], nums[j], nums[i]
    print(strs, nums)
    for i in range(m):
        if n > nums[i]:
            for j in range(nums[i]):
                if t[j] != strs[i][j]: break
            else: stack.append([t[nums[i]:], 1])
        elif n == nums[i]:
            if strs[i] == t:
                return 1
    while stack:
        text, cnt = stack.pop()
        for i in range(m):
            if len(text) > nums[i]:
                for j in range(nums[i]):
                    if text[j] != strs[i][j]: break
                else: stack.append([text[nums[i]:], cnt+1])
            elif len(text) == nums[i]:
                if text == strs[i]: return cnt+1
    return -1

list_str = ['app', 'ap', 'p', 'l', 'e', 'ple', 'pp']
find_str = 'apple'
print(solution(["ba", "an", "nan", "ban", "n"], "banana"))