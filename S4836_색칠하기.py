T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #print(arr)
    square = [[0]*10 for _ in range(10)]
    #print(square)
    for i in range(N):
        x1 = arr[i][0]
        x2 = arr[i][2]
        y1 = arr[i][1]
        y2 = arr[i][3]
        if x1 > x2:  # x, y값 순서는 바뀌어도 무관
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        if arr[i][4] == 1:
            for a in range(x1, x2+1):
                for b in range(y1, y2+1):
                    square[a][b] += 1

        if arr[i][4] == 2:
            for a in range(x1, x2+1):
                for b in range(y1, y2+1):
                    square[a][b] += 2

        cnt = 0
        for x in range(10):
            for y in range(10):
            
                if square[x][y] == 3:
                    cnt += 1
                    
    print(f'#{tc} {cnt}')