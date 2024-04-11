import sys
from collections import deque


def bfs():
    global cnt
    queue = deque([[0, 0]])
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == n - 1:
            cnt+=1
            continue

        dx = [graph[x][y], 0]
        dy = [0, graph[x][y]]

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                queue.append([nx, ny])



n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt=0
bfs()
print(cnt)