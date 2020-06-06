string1, string2 = input(), input()
adj = [[0]*len(string1) for _ in range(len(string2))]
flag = 0
for i in range(len(string2)):
    for j in range(len(string1)):
        if string1[j] == string2[i]:
            if i > 0 and j > 0: adj[i][j] = adj[i-1][j-1] + 1
            else: adj[i][j] = 1
        else:
            result = 0
            if i > 0: result = max(result, adj[i-1][j])
            if j > 0: result = max(result, adj[i][j-1])
            adj[i][j] = result
print(adj[len(string2)-1][len(string1)-1])
