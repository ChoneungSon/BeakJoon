import sys
n = int(sys.stdin.readline())
memo = [0] * (n+1) # 저장 리스트 만들기
for i in range(2, n+1):
    min_value = n + 1 # 가장 긴 값은 배열의 각 위치의 인덱스만큼 이므로 일단 최댓값보다 1 큰 수를 초기
    if i % 3 == 0:    # 최솟값으로 지정
        min_value = min(min_value, memo[i//3] + 1) # 해당 값이 3의 배수일 때, 3으로 나눈 수의 값을 비교
    if i % 2 == 0: # 해당 값이 2의 배수일 때, 2로 나눈 수의 값을 비교
        min_value = min(min_value, memo[i//2] + 1) # 해당 값 보다 1 작은 수의 값을 비교
    min_value = min(min_value, memo[i-1] + 1) # 위 3가지 경우에서 가장 작은 값을 리스트에 저장
    memo[i] = min_value
print(memo[n])
