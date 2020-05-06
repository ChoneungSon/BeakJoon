def solution(relation):
    r, c, cnt = len(relation), len(relation[0]), 0
    visited = [0] * c
    def select(cnt, candidate, start, length):
        nonlocal r, c, relation, visit, candidates
        if cnt == length: candidates.append(candidate[:])
        else:
            for i in range(start, c):
                if visit[i] == 0:
                    candidate[cnt] = i
                    select(cnt+1, candidate[:], i+1, length)
    for length in range(1, c+1):
        candidates, visit = [], visited[:]
        select(0, [0]*length, 0, length)
        print(candidates)
        for i in range(len(candidates)):
            find_dict = dict()
            for j in range(r):
                a = tuple(relation[j][candidates[i][k]] for k in range(length))
                if a not in find_dict: find_dict[a] = 1
                else: break;
            else:
                print(candidates[i])
                cnt += 1
                for j in range(length):
                    if visited[candidates[i][j]] == 0: visited[candidates[i][j]] = 1
    return cnt

import copy
def solution2(relation):
    r, c, cnt = len(relation), len(relation[0]), 0
    arr, visited = [[]], []
    while arr:
        visit = arr.pop(0)
        if visit: start = visit[-1]+1
        else: start = 0
        for i in range(start, c):
            find_dict, v = [], visit+[i]
            if v not in visited:
                for j in range(r):
                    value = tuple(relation[j][v[k]] for k in range(len(v)))
                    if value not in find_dict: find_dict.append(value[:])
                    else: arr.append(v[:]); break;
                else:
                    visited.append(v[:])
                    cnt += 1
    print(visited)
    return cnt

def solution5(relation):
    r, c, cnt = len(relation), len(relation[0]), 0
    arr = [[]]
    while arr:
        visit = arr.pop(0)
        if visit: start = visit[-1]+1
        else: start = 0
        for i in range(start, c):
            find_dict, v = dict(), visit+[i]
            for j in range(r):
                value = tuple(relation[j][v[k]] for k in range(len(v)))
                if value not in find_dict: find_dict[value] = 1
                else: arr.append(v[:]); break;
            else:
                print(v)
                cnt += 1
    return cnt

def solution4(relation):
    r, c, cnt = len(relation), len(relation[0]), 0
    arr = [[]]
    while arr:
        visit = arr.pop(0)
        if visit: start = visit[-1]+1
        else: start = 0
        for i in range(start, c):
            find_dict, v = dict(), visit+[i]
            arr.append(v[:])
            print(v)
    return cnt

def solution6(relation):
    r, c, cnt = len(relation), len(relation[0]), 0
    arr, visited = [set()], []
    while arr:
        visit = arr.pop(0)
        if visit: start = max(visit)+1
        else: start = 0
        for i in range(start, c):
            find_set, v = set(), copy.deepcopy(visit)
            v.add(i)
            for j in visited:
                if not(j - v): break
            else:
                print(v)
                for j in range(r):
                    value = set([relation[j][k] for k in v])
                    if value not in find_set: find_set.add(copy.copy(value))
                    else: arr.append(v[:]); break;
                else:
                    visited.append(v[:])
                    cnt += 1
    print(visited)
    return cnt

def solution7(relation):
    r, c, cnt = len(relation), len(relation[0]), 0
    arr, visited = [[]], []
    while arr:
        visit = arr.pop(0)
        if visit: start = max(visit)+1
        else: start = 0
        for i in range(start, c):
            v = visit + [i]
            if subset(v, visited): continue
            else:
                find_dict = dict()
                for j in range(r):
                    part = tuple(relation[j][k] for k in v)
                    if part not in find_dict: find_dict[part] = 1
                    else: arr.append(v[:]); break;
                else:
                    visited.append(v[:])
                    cnt += 1
    print(visited)
    return cnt

def subset(v, visited):
    if not(visited): return 0
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            if visited[i][j] not in v: break
        else: return 1
    return 0

print(solution7(
    [["100","ryan","music","2"],
     ["600","apeach","math","2"],
     ["300","tube","computer","3"],
     ["400","con","computer","4"],
     ["500","muzi","music","3"],
     ["600","apeach","music","2"]]))
print(solution7([['ab', 'c'], ['a', 'bc'], ['x', 'yz'], ['x', 'c']]))
print(solution7(
[['a','b','c'],
['1','b','c'],
['a','b','4'],
['a','5','c']]
))
print(solution7(
[['a','1','4'],
['2','1','5'],
['a','2','4']]
))