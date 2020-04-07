class musics():
    def __init__(self, melody, start=0, end=0):
        s_h, s_m = map(int, start.split(':'))
        e_h, e_m = map(int, end.split(':'))
        self.time = 60 * (e_h - s_h) + (e_m - s_m)
        self.melody = mkmelody(melody)

def mkmelody(string):
    list_m, s = [], string[0]
    for i in range(1, len(string)):
        if string[i] != '#':
            list_m.append(s)
            s = string[i]
        else:
            s += '#'
        if i == len(string) - 1:
            list_m.append(s)
    return list_m

def solution(m, musicinfos):
    M, name, runtime = mkmelody(m), '', 0
    for i in range(len(musicinfos)):
        start, end, title, melody = musicinfos[i].split(',')
        music, t = musics(melody, start, end), 0
        if len(M) > music.time: continue
        else:
            while t+len(M) <= music.time:
                for j in range(len(M)):
                    if music.melody[(t+j)%len(music.melody)] != M[j]: break
                else:
                    if runtime < music.time:
                        runtime = music.time
                        name = title
                        break
                t += 1
    if name: return name
    else: return '(None)'

print(solution("CC#BCC#BCC#BCC#B", ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']))