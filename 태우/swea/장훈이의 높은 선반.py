def subset(idx,sum_v):
    global result
 
    if sum_v >= H:
        if result >= sum_v:
            result = sum_v
        return
     
    if idx == N:
        return
    subset(idx+1,sum_v+hi[idx])
    subset(idx+1,sum_v)
 
 
 
for tc in range(1,int(input())+1):
    N,H =map(int,input().split())
    hi = list(map(int,input().split()))
    result=10000000000000
    subset(0,0)
    print(f'#{tc} {result-H}')