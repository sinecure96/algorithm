# 처음에는 예외처리 후에 현위치 기준으로 K 내의 범위에서 최대 station을 찾아서
# 찾으면 현위치 갱신하고 다시 탐색하려 했음 >> 조건 설정이 까다로움
# 그래서 방식을 바꿈 : 일단 이동 후에 이동한 자리부터 한칸씩 뒤로 가면서 충전소가 있는지 탐색,
# 있으면 그위치로 현위치 갱신 후 도착지점까지 반복
# 예외인 경우의 조건을 다 썼다가 그냥 마지막 else로 처리
# break 를 통한 시간낭비 감소
import sys
sys.stdin = open('4831input.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))
    stations_index = [0] * N
    for station in stations:
        stations_index[station] = 1
    
    # 첫 정류장이 K보다 크면 아예 안됨 
    if K < stations[0]:
        ans = 0
    # 충전소 간의 번호 차가 K보다 크면 x >>> 런타임 에러로 수정 : 예외처리로
    # l = len(stations)
    # for i in range(1, l+1):
    #     if stations[i] - stations[i-1] > K:
    #         print(f'#{tc} 0')
        
    # 시작부터 K 내의 범위 중 최대 station을 취하면 됨 > 바꿈
    # K만큼 이동 후에 충전기 있으면 설정, 없으면 뒤로 한칸
    
    cur = 0 # 현재 위치 설정
    ans = 0 # 충전 횟수 설정
    
    while cur < N: # 도착 전까지
        
        # break를 안써서 계속 잘못 돌거나 런타임 에러 떴음
        
        cur = cur + K
        
        if cur >= N:
            print(f'#{tc} {ans}')
            break
        
        for _ in range(K):
            if stations_index[cur]:
                ans += 1
                break
            else:
                cur = cur - 1
        else:
            print(f'#{tc} 0')
            break
            
    

