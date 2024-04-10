r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
front = 0
back = 0

# 청소기 위치
for i in range(r) :
    if room[i][0] == -1 :
        front = i
        back = i + 1
        break

# 감염 드가자~
def spread() :
    dx = [-1, 1, 0, 0]# 상 하 좌 우
    dy = [0, 0, -1, 1]

    temp = [[0] * c for _ in range(r)]
    for i in range(r) :
        for j in range(c) :
            if room[i][j] != 0 and room[i][j] != -1 :
                v = 0
                for k in range(4) :
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1 :
                        temp[nx][ny] += room[i][j] // 5
                        v += room[i][j] // 5
                room[i][j] -= v
    for i in range(r) :
        for j in range(c) :
            room[i][j] += temp[i][j]

# 위쪽 공기청정기 동작
def clean_up() :
    c1 = [0, -1, 0, 1] # 반시계 방향 (동 북 서 남)
    r1 = [1, 0, -1, 0]
    a = 0 #방향 인덱스
    b = 0 #이전값
    x, y = front, 1
    while 1 :
        nx = x + c1[a]
        ny = y + r1[a]
        if x == front and y == 0 : # 다돌았으면 break
            break
        if not 0 <= nx < r or not 0 <= ny < c : #범위 밖이라면
            a += 1
            continue
        room[x][y], b = b, room[x][y] #두 변수 값 바꾸기
        x, y = nx, ny #다음 위치 이동

# 아래쪽 공기청정기 동작
def clean_down() :
    c1 = [0, 1, 0, -1] # 시계 방향 (동 남 서 북)
    r1 = [1, 0, -1, 0]
    a = 0 #방향 인덱스
    b = 0 #이전값
    x, y = back, 1
    while 1 :
        nx = x + c1[a]
        ny = y + r1[a]
        if x == back and y == 0 : # 다돌았으면 break
            break
        if not 0 <= nx < r or not 0 <= ny < c :  #범위 밖이라면
            a += 1
            continue
        room[x][y], b = b, room[x][y] # 두 변수 값 바꾸기
        x, y = nx, ny #다음 위치 이동

for _ in range(t) :
    spread()
    clean_up()
    clean_down()

result = 0
for i in range(r) :
    for j in range(c) :
        if room[i][j] > 0 :
            result += room[i][j]

print(result)