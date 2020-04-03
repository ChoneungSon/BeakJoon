string = list(map(ord, input()))
point, time = 0, 0
for i in range(len(string)):
    num = string[i] - 65
    if (num - point) % 26 < (point - num) % 26:
        time += (num - point) % 26
    else: time += (point - num) % 26
    point = num
print(time)