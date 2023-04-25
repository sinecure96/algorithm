'''
접근 방법 : matrix의 index 범위 설정에 유의하여 총합을 구해보자!

1) input 정리하기
T : test case
N : table의 가로 세로 길이
M : 파리채의 가로 세로 길이
fly_list : 각 구역별 파리의 마릿수

2) 파리채의 좌측-상단을 기준으로 index 범위를 설정한다!
행 : (N - M + 1) / 열 : (N - M + 1)

3) range(index, index + M)의 가로 세로 수를 모두 더한다!
'''

T = int(input())
for tc in range (1, T+1):
    N, M = map(int, input().split())
    fly_list = [list(map(int,input().split())) for _ in range(N)]
    # 최댓값의 기준 설정하기 - 처음 값으로 우선 설정(좌상)
    max_value = 0
    for r in range(M):
        for c in range(M):
            max_value += fly_list[c][r]

    # 테이블 위의 파리채 위치 정하기!
    for r_index in range(N - M + 1):
        for c_index in range(N - M + 1):
            
    # 총 파리수를 임시 저장할 변수 temp 선언!
            temp = 0

    # 파리채 면적 내에 죽은 파리 수 더하기!
            for r in range(r_index, r_index + M):
                for c in range(c_index, c_index + M):
                    temp += fly_list[c][r]
            if temp > max_value:
                max_value = temp

    print(f'#{tc} {max_value}')


