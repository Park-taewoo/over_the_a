def solve(start_a,start_b,cnt):
    global min_num
    
    if min_num < cnt:
        return
    
    if start_a == end_a and start_b == end_b :
        if min_num > cnt:
            min_num = cnt 
        return 
    
    for i in range(4):
        nc = start_a + c[i]
        nr = start_b + r[i]
        if 0<=nc<N and 0<= nr <N and not visited[nc][nr] and not arr[nc][nr]:
            cnt+=1
            visited[nc][nr] = 1
            solve(nc,nr,cnt)
            cnt-=1
            visited[nc][nr] = 0
            
        



for tc in range(1,int(input())+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    start_a,start_b=map(int,input().split())
    end_a,end_b=map(int,input().split())
    min_num=9999999999999999
    visited= [[0]*N for _ in range(N)]
    c=[-1,1,0,0]  #상하좌우
    r=[0,0,-1,1]
    visited[start_a][start_b]=1
    solve(start_a,start_b,0)
    if min_num == 9999999999999999:
        min_num = -1
    print(f'#{tc} {min_num}')