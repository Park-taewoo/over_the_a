for tc in range(1,11):
    N = int(input())
    arr =[list(map(int,input())) for _ in range(100)]
    visited=[[0]*100 for _ in range(100)]
 
    stack=[[1,1]]
    visited[1][1] = 1
 
    result = 0
    d1 = [-1,1,0,0]
    d2 = [0,0,-1,1] #상하좌우
    while True:
        if not stack:
            break
        r, c = stack[-1]
 
        if arr[r][c] == 3:
            result =1
            break
 
        for i in range(4):
            if arr[r+d1[i]][c+d2[i]] !=1 and not visited[r+d1[i]][c+d2[i]]:
                visited[r+d1[i]][c+d2[i]]=1
                stack.append([r+d1[i],c+d2[i]])
                break
        else:
            stack.pop()
 
    print(f'#{tc} {result}')