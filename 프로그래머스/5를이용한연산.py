def solution(N, number):
    mknums, cnt = [5], 1
    while cnt <= 8:
        cand = []
        for i in range(len(mknums)):
            if mknums[i] + 5 == number: return cnt
            elif mknums[i] + 5 in cand or mknums[i] + 5 in mknums: pass
            else: cand.append(mknums[i] + 5)
            if mknums[i] - 5 == number: return cnt
            elif mknums[i] - 5 in cand or mknums[i] - 5 in mknums or mknums[i] - 5 < 0 : pass
            else: cand.append(mknums[i] - 5)
            if mknums[i] * 5 == number: return cnt
            elif mknums[i] * 5 in cand or mknums[i] * 5 in mknums: pass
            else: cand.append(mknums[i] * 5)
            if mknums[i] // 5 == number: return cnt
            elif mknums[i] // 5 in cand or mknums[i] // 5 in mknums: pass
            else: cand.append(mknums[i] // 5)
        if int(f'{N}'*cnt) == number: return cnt
        else: cand.append(int(f'{N}'*cnt))
        mknums += cand
        cnt += 1
    return -1

print(solution(5, 12))