arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
copy_arr = [[0]*3 for _ in range(3)]
copy_cross = [[0]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        copy_arr[i][j] = arr[2-j][i]
        copy_cross[i][j] = arr[j][2-i]
for i in range(3):
    print(''.join(map(str, copy_arr[i])))
print()
for i in range(3):
    print(''.join(map(str, copy_cross[i])))