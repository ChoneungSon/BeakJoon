n = int(input())
arr, rarr, remove_set, rremove_set = [0] * 501, [0] * 501, set(), set()
for _ in range(n):
    x, y = map(int, input().split())
    arr[x], rarr[y] = y, x
for i in range(1, 501):
    if arr[i]:
        for j in range(1, i):
            if arr[j] > arr[i]:
                remove_set.add(arr[j])
    if rarr[i]:
        for j in range(1, i):
            if rarr[j] > rarr[i]:
                rremove_set.add(rarr[j])
print(min(len(remove_set), len(rremove_set)))