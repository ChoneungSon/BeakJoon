arr = []
for i in range(3):
    if i == 2:
        for j in range(5):
            arr.append(f'{i}'+f'{j}')
    else:
        for j in range(10):
            arr.append(f'{i}' + f'{j}')
# print(arr)
for i in range(25):
    print(float(arr[i]))