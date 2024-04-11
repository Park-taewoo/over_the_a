import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

dp[0][0] = 1

# 2중포문으로 반복도는이유?
# 어차피 오른쪽이랑 아래로만가니까 순서대로 순회하면 다돌아짐
for i in range(N):
    for j in range(N):
        if dp[i][j] and arr[i][j]:
            if i + arr[i][j] < N:
                # 내가 다음에 도착할 지점에 현재 값을 더해줌
                # 현재값은 내가 현재위치까지 도달하는데 나올수 있는 경우의 수
                dp[i+arr[i][j]][j] += dp[i][j]
            if j + arr[i][j] < N:
                dp[i][j+arr[i][j]] += dp[i][j]

print(dp[N-1][N-1])