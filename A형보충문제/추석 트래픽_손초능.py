def solution(lines):
    n, max_cnt = len(lines), 1
    command = [[0]*2 for _ in range(n)]
    for i in range(n):
        command[i][0], command[i][1] = change_time(lines[i])
    for i in range(n-1):
        p, cnt, end = i, 1, command[i][1] + 999
        while p < n-1:
            p += 1
            if command[p][0] <= end:
                cnt += 1
        max_cnt = max(max_cnt, cnt)
    return max_cnt

def change_time(list_time):
    d, time, s = list_time.split()
    h, m, sec = map(float, time.split(':'))
    print(list_time, h, m, sec)
    time = int((h * 3600 + m * 60 + sec)*1000)
    s = int(float(s[:len(s) - 1])*1000)
    return time-s+1, time

print(solution([
'2016-09-15 20:59:57.421 0.351s',
'2016-09-15 20:59:58.233 1.181s',
'2016-09-15 20:59:58.299 0.8s',
'2016-09-15 20:59:58.688 1.041s',
'2016-09-15 20:59:59.591 1.412s',
'2016-09-15 21:00:00.464 1.466s',
'2016-09-15 21:00:00.741 1.581s',
'2016-09-15 21:00:00.748 2.31s',
'2016-09-15 21:00:00.966 0.381s',
'2016-09-15 21:00:02.066 2.62s'
]))