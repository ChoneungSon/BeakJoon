def solution(word, pages): # 매칭점수는 포기 55%만 성공
    n = len(pages)
    html = [list(map(str, pages[i].split('\n'))) for i in range(n)]
    score = [[0]*4 for _ in range(n)]
    for i in range(n):
        flag, urls, count = 0, [], 0
        for j in range(len(html[i])):
            count += find(word, html[i][j])
            if html[i][j] == "</html>": break
            elif flag == 0:
                if html[i][j] == "<body>": flag = 1; continue
                elif 'meta' in html[i][j] and 'content' in html[i][j]:
                    front, back = html[i][j].split('content=\"')
                    score[i][2] = back[:-3]
            else:
                if "<a" in html[i][j]:
                    find_url = list(html[i][j].split('\"'))
                    urls.append(find_url[1])
        score[i][0], score[i][3] = count, urls[:]
        if score[i][3]: score[i][1] = count / len(urls)
    idx = 0
    for i in range(n):
        for j in range(n):
            if i != j and score[i][2] in score[j][3]: score[i][0] += score[j][1]
        if score[idx][0] < score[i][0]: idx = i
    return idx

def find(word, line):
    w, cnt = '', 0
    for i in range(len(line)):
        if line[i].isalpha():
            w += line[i]
        else:
            if w.lower() == word.lower(): cnt += 1
            w = ''
    if w.lower() == word.lower(): cnt += 1
    return cnt


print(solution('blind', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
))
print(solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
