from copy import deepcopy
from collections import deque

def solve1():
    global max_num
    data=deepcopy(arr)
    rc_1 = deque()
    for i in range(N):
        for j in range(M):
            if data[i][j]==2:
                rc_1.append((i,j))
    while rc_1:
        c1,c2 = rc_1.popleft()
        for k,q in rc:
            ni = k + c1
            nj = q + c2
            if 0 <= ni < N and 0 <= nj < M:
                if data[ni][nj] == 0:
                   data[ni][nj] =2
                   rc_1.append((ni,nj)) 
                   
    min_num=0
    for w in range(N):
        for z in range(M):
            if data[w][z] ==0:
                min_num+=1
    if max_num<min_num:
        max_num=min_num       
    
    
def solve(num):
    if num == 3:
        solve1()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] ==0 and not visited[i][j]:
              visited[i][j]=1  
              arr[i][j] =1
              solve(num+1)
              visited[i][j]=0
              arr[i][j] = 0


N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]
max_num=0
rc=[[0,1],[1,0],[0,-1],[-1,0]]
solve(0)
print(max_num)