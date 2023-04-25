N = int(input())
M = int(input())
S = input()
ans = 0
target = 'IO' * N + 'I'
for i in range(M-len(target)):
    if S[i:i+len(target)] == target:
        ans += 1
print(ans)

# S2
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

