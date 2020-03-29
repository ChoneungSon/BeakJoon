def solution(n, t, m, timetable):
    length, sort_time, start, idx = len(timetable), [], 540, 0
    for i in range(length):
        hour, min = map(int, timetable[i].split(":"))
        sort_time.append(hour * 60 + min)
    sort_time.sort()
    for i in range(n):
        cnt = 0
        for j in range(m):
            if idx > length-1: break
            if sort_time[idx] <= start:
                idx += 1
                cnt += 1
        if i == n-1:
            if cnt == m:
                result = sort_time[idx-1]-1
            elif cnt < m:
                result = start
        start += t
    return '%02d:%02d'%(result//60, result%60)

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))