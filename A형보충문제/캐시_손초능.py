def solution(cacheSize, cities):
    list_cache, answer, n = [], 0, len(cities)
    if cacheSize:
        for i in range(n):
            for j in range(len(list_cache)):
                if capi(cities[i]) == list_cache[j]: # 도시가 cache 안에 있을 때
                    temp = list_cache.pop(j)
                    list_cache.append(temp)
                    answer += 1
                    break
            else: # 도시가 cache 안에 없을 때
                if capi(cities[i]) not in list_cache:
                    if len(list_cache) == cacheSize:
                        list_cache.pop(0)
                        list_cache.append(capi(cities[i]))
                    else:
                        list_cache.append(capi(cities[i]))
                    answer += 5
    else: return n * 5 # cache 크기가 0 일 때, 항상 cache miss 이므로
    return answer

def capi(string): # 대문자로 바꾸는 함수
    list_str = list(map(str, string))
    for i in range(len(string)):
        list_str[i] = list_str[i].capitalize()
    return ''.join(list_str)