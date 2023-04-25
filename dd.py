M = int(input())
if M % 5 == 0:
    print(-1)
elif M < 5:
    print(M*5)
else:
    print((M-M//5)*5)