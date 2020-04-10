dir =[
    "/",
    "/hello",
    "/hello/tmp",
    "/root",
    "/root/abcd",
    "/root/abcd/etc",
    "/root/abcd/hello"
]

dic = {}
for i in range(1, len(dir)):
    lst = list(dir[i].split('/'))
    for j in range(len(lst)-1):
        dic[lst[j]]