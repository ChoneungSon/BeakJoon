def solution(heights):
    answer = [0] * len(heights)
    for i in range(1, len(heights)):
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]: # 나보다 왼쪽에 있는 탑 중에 나보다 높은 것이 있으면 배열을 최신화
                answer[i] = j + 1
                break
    return answer