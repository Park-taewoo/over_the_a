def solve(a,b):
    global min_num

    if a == N//2:
        print(visited)
        num,num1=0,0
        for k in range(N):
            for j in range(k, N):
                if visited[k] and visited[j]:
                    num += arr[k][j]
                    num += arr[j][k]
                elif not visited[k] and not visited[j]:
                    num1 += arr[k][j]
                    num1 += arr[j][k]
        max_num=abs(num1-num)
        if min_num>max_num:
            min_num=max_num
        return

    for i in range(b, N):
        if not visited[i]:
            visited[i]=1
            solve(a+1,i+1)
            visited[i]=0


N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]

visited=[0]*N

min_num=999999999999999999999999999999999
solve(0,0)
print(min_num)