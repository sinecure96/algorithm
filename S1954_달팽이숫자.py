'''
접근 방법 : 델타 탐색을 통해서 이동 방향을 바꾸어 보자!
 -> 한쪽 방향으로 쭉 가다가 벽(또는 숫자가 있는 칸)에 부딪힐 경우, 이동 방향을 (우 -> 하 -> 좌 -> 상) 순서로 바꾸어 보자!

1) input 처리
T : test case
N : 달팽이 집 num_list의 크기

2) 달팽이 집 num_list 선언 (0으로 이루어진)

3) 델타 리스트 선언 :
 달팽이 집의 이동 방향을 정하기 (우 -> 하 -> 좌 -> 상) 방향으로 이동
  -> k = (k+1) % 4 로 설정하면 상 이후에 우로 되돌아 올 수 있음!

4) 만일 달팽이 집을 이동하다 벽 혹은 채워진 칸을 만나면 이동 방향을 바꾸어 나감.

5) 숫자를 채워나가던 변수 cnt가 N ** 2가 될 경우 달팽이집을 멈춘다.

** join 구분자 사용 : '구분자'.join(리스트)
'''



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = [[0] * N for _ in range(N)]
    
    # 델타 리스트 만들기 (우 -> 하 -> 좌 -> 상 순서로)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    
    cnt = 1
    k = 0
    i, j = 0, 0
    
    num_list[i][j] = cnt
    
    while cnt < N**2:
        # 새로운 좌표 확인
        ni, nj = i + di[k], j + dj[k]
        # 새로운 좌표가 정상 위치인 경우
        if 0 <= ni < N and 0 <=nj < N and not(num_list[ni][nj]) :
            cnt += 1
            i, j = ni, nj
            num_list[ni][nj] = cnt

        # 정상 위치가 아닐 경우 (집 밖이거나 숫자가 있는 칸일 경우:
        else:
            k = (k + 1) % 4

    # 달팽이 집을 출력
    print(f'#{tc}')
    for i in range(N):
        result = list(map(str, num_list[i]))
        print(' '.join(result))
    


