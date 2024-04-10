def solve(num):
    visited=[0] * N
    for i in range(N-1):
        if arr[num][i]==arr[num][i+1]:
            continue
        elif abs(arr[num][i]-arr[num][i+1]) >1:
            return False
        if arr[num][i] > arr[num][i+1]: #왼쪽이 더 큰경우
            high=arr[num][i+1]
            for j in range(i+1,i+1+L):
                if 0<=j<N:
                    if high != arr[num][j]:
                        return False
                    elif visited[j]:
                        return False
                    visited[j] = 1
                else:
                    return False
        elif arr[num][i] < arr[num][i+1]: #오른쪽이 더 큰경우
            high=arr[num][i]
            for j in range(i,i-L,-1):
                if 0<=j<N:
                    if high != arr[num][j]:
                        return False
                    elif visited[j]:
                        return False
                    visited[j] = 1
                else:
                    return False
    return True

#스핀 하자 
def spin90(arr):
    arr1=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr1[i][j] = arr[N-1-j][i]
    return arr1



N,L=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
cnt=0

#행검사
for i in range(N):
    a=solve(i)
    if a:
        cnt+=1

#열검사
arr = spin90(arr)
for i in range(N):
    a = solve(i)
    if a:
        cnt+=1
print(cnt)