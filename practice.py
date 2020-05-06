# import pprint
# def solution(relation):
#     answer, visit = 0, [[0]*len(relation[0]) for _ in range(len(relation))]
#     for i in range(len(relation[0])):
#         key, flag = dict(), 0
#         for j in range(len(relation)):
#             if key.get(relation[j][i], 0):
#                 visit[j][i] = visit[key[relation[j][i]]-1][i] = key[relation[j][i]]
#             else: key[relation[j][i]] = j + 1
#     pprint.pprint(visit)
#     return answer
#
# print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

