def solution(record):
    answer = [0] * len(record)
    user = dict()
    for i in range(len(record)):
        doing = list(map(str, record[i].split()))
        if doing[0] == 'Enter' or doing[0] == 'Change':
            user[doing[1]] = doing[2]
            if doing[0] == 'Enter': answer[i] = [doing[1], 1]
        else:
            answer[i] = [doing[1], 0]
    result = []
    for i in range(len(record)):
        if answer[i]:
            if answer[i][1]: result.append(f'{user[answer[i][0]]}님이 들어왔습니다.')
            else: result.append(f'{user[answer[i][0]]}님이 나갔습니다.')
    return result

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))