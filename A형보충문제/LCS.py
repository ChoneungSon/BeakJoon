string1, string2 = input(), input()
adj = [[0]*len(string1) for _ in range(len(string2))]
for i in range(len(string1)):
    flag = 1
    for j in range(len(string2)):
        result = 0
        if i > 0 and j > 0:
            result = max(result, adj[i-1][j], adj[i-1][j-1])
        if flag and string1[i] == string2[j]: result += 1
        adj[i][j] = result
print(adj[len(string1)-1][len(string2)-1])
