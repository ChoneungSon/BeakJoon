def solution(food_times, k):
    i, length, pre, sort_time = 0, len(food_times), 0, sorted(food_times)
    # 정렬된 배열을 지정
    if sum(food_times) <= k: return -1
    # 만약 모든 음식을 먹는데 걸리는 시간보다 제시된 시간이 클 경우 -1을 출력
    while i < len(food_times):
        # 최솟값에서 시작해서 k에서 빼기 시작함
        if pre != sort_time[i]:
            # 최솟값이 겹치는 경우는 이미 빠졌기 때문에 고려하지 않음
            if k >= (sort_time[i] - pre) * length:
                # 이 조건에서는 k값만 줄여주면 됨
                k -= (sort_time[i] - pre) * length
                pre = sort_time[i]
            else: # 이 조건에서는 출력할 인덱스 값을 찾아야 함
                k, cnt = k%length+1, 0
                # 원하는 인덱스는 k를 아직 0이 아닌 음식의 갯수로 나눴을 때 나머지를 구하면 된다.
                for j in range(len(food_times)):
                    if food_times[j] > pre:
                        cnt += 1
                        if cnt == k: return j+1
        i += 1
        length -= 1

print(solution([5]*10, 15))