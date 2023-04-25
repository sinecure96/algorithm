T = int(input())
for tc in range (1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    max_num = max(numbers)
    min_num = min(numbers)
    ans = max_num - min_num
    
    print(f'#{tc} {ans}')