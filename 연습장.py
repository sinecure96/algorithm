'''
인덱스의 범위를 설정하고, 그 안에서 row, column 돌면서 
영역의 합 구하고, 최댓값과 비교/갱신
'''


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly_list = [list(map(int, input().split())) for _ in range(N)]
    
    max_value = 0
    for c in range(M):
        for r in range(M):
            max_value += fly_list[r][c]
                    
                    
    for r_index in range(N-M+1):
        for c_index in range(N-M+1):
            temp = 0
            
            for r in range(r_index, r_index+M):
                for c in range(c_index, c_index+M):                    
                    temp += fly_list[r][c]
            
            if temp > max_value:
                max_value = temp
        
    print(f'#{tc} {max_value}')
    
    
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    r1, c1, r2, c2, color = map(int, input().split())
    R1, C1, R2, C2, color2 = map(int, input().split())
    
    area = list([0] * 10 for _ in range(10))
    cnt = 0
    for r in range(r1, r2):
        for c in range(c1, c2):
            area[r][c] += 1
    for r in range(R1, R2):
        for c in range(C1, C2):
            area[r][c] += 1
            
    for r in range(10):
        for c in range(10):
            if area[r][c] == 2:
                cnt += 1
    print(f'#{tc} {cnt}')
    
    
    
for _ in range(1, 11):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    # 도착점 -> 출발점
    for i in range(100):
        # 도착지는 값이 2
        if matrix[99][i] == 2:
            # 도착지의 좌표를 저장
            x = 99
            y = i

    # delta 값
    # 좌 우 상 -> 도착지부터 올라가기 때문에 아래는 볼 필요 없음
    dx = [0, 0, -1]
    dy = [-1, 1, 0]

    # 가장 윗부분에 도달하면 끝내자
    while x != 0:
        # 주위를 둘러보고 왼쪽이나 오른쪽으로 갈 길이 있으면 가자
        # 우회전과 좌회전이 동시에 가능한 상황은 없음

        # 방향 델타로 이동
        for d in range(3):
            # 좌 -> 우 -> 상
            # 좌표 변경
            new_x = x + dx[d]
            new_y = y + dy[d]

            # 새로운 위치로 옮겼을 때 
            # 그 위치가 matrix 범위 내에서 안에 포함되는지 확인하고 (0 <= new_x < 100 and 0 <= new_y < 100)
            # 새로운 위치가 갈 수 있는 길이면 (matrix[new_x][new_y] == 1)
            if 0 <= new_x < 100 and 0 <= new_y < 100 and matrix[new_x][new_y] == 1:
                # 이전 자리 0으로 변경
                matrix[x][y] = 0
                # 현재 위치 갱신 -> 움직여야 할 곳으로 이동
                x += dx[d]
                y += dy[d]

    # 최종적으로 column값 출력
    print(f'#{tc} {y}')
    
    
T = 10
for tc in range(1, T+1):
    graph = [list(map(int, input().split())) for _ in range(100)]
    
    N = 99
    for i in range(100):
        if graph[N][i] == 2:
            x = N
            y = i
    
    dx = [0, 0, -1]
    dy = [-1, 1, 0]
    
    while x != 0:
        for d in range(3):
            new_x = x + dx[d]
            new_y = y + dy[d]
            if 0 <= new_x < 100 and 0 <= new_y < 100:
                if graph[new_x][new_y] == 1:
                    graph[x][y] = 0
                    x, y = new_x, new_y
    print(f'#{tc} {y}')
    
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if 0 < N < 13:
        ans = N
    if 14 < N < 113:
        ans = N-1
        
        
        
w, h = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(h)]




from collections import deque
import sys
read = sys.stdin.readline

# bfs를 상하좌우 대각선 8방향으로 돌림

def bfs(x, y):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    field[x][y] = 0
    q = deque()
    q.append([x, y])
    while q:
        a, b = q.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
        if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
            field[nx][ny] = 0
            q.append([nx, ny])

while True:
    w, h = map(int, read().split())
    if w == 0 and h == 0:
        break
    field = []
    count = 0
    for _ in range(h):
        field.append(list(map(int, read().split())))
    for i in range(h):
        for j in range(w):
            if field[i][j] == 1:
                bfs(i, j)
                count += 1
                
    if list(map(int, input().split())) == [0, 0]:
        break
                
                
    
    print(count)
    
    
n=int(input()) # 컴퓨터 개수
v=int(input()) # 연결선 개수
graph = [[] for i in range(n+1)] # 그래프 초기화
visited=[0]*(n+1) # 방문한 컴퓨터인지 표시
for i in range(v): # 그래프 생성
    a,b=map(int,input().split())
    graph[a]+=[b] # a에 b 연결
    graph[b]+=[a] # b에 a 연결 -> 양방향
def dfs(v):
    visited[v]=1
    for nx in graph[v]:
        if visited[nx]==0:
            dfs(nx)
dfs(1)
print(sum(visited)-1)

[[2 5] [1 3 5] [2] [7] [1 2 6] [5] [4]]
# 여기서 dfs 돌려서 감염된 점들 체크 후 시작점 빼고 센다
[1 2]
[2 3]
[1 5]
[5 2]
[5 6]
[4 7]

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = int(input())

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(t):
    cnt = 0
    n, m, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)

def find_right_zeros(n):
    zeros = 0
    while n >= 5:
        zeros += n // 5
        n //= 5
    return zeros

12
21 3
24
4 4
25 5 1 6
5 1
10 2 
15 3
20 4
25 6
50 10 2 12 

m = int(input())
left, right, result = 1, m * 5, 0

while left <= right:
    mid = (left + right) // 2

    # 메인 로직
    zero_count = find_right_zeros(mid)

    # 조건 분기
    if zero_count < m:
        left = mid + 1
    else:
        right = mid - 1
        result = mid

print(result if find_right_zeros(result) == m else -1)



N = int(input())
M = int(input())
S = input()

cursor, count, result = 0, 0, 0

while cursor < (M - 1):
    if S[cursor:cursor + 3] == 'IOI': #3칸
        count += 1
        cursor += 2
        if count == N:
            result += 1
            count -= 1
    else:
        cursor += 1
        count = 0

print(result)