'''
2차원 배열 인풋 받기
델타 이동(이동 후 좌표의 조건 추가)
이동 후에 직전 좌표 0으로 초기화 (안하면 되돌아갈수도 있음)
'''

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
    # 좌 우 상
    dx = [0, 0, -1]
    dy = [-1, 1, 0]

    # 가장 윗부분에 도달하면 끝
    while x != 0:

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

    # 최종적으로 y값 출력
    print(f'#{tc} {y}')