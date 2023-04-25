# 5의 배수의 팩토리얼마다 0이 하나씩 증가, 
# 25의 배수의 팩토리얼마다 0이 두개씩 증가,
# 함수 정의 후 이진탐색

def find_right_zeros(n):
    zeros = 0
    while n >= 5:
        zeros += n // 5
        n //= 5
    return zeros

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
        

