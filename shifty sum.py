N = int(input())

K = int(input())

total = N

while K>0:
    total = total + (N*10**K)
    K = K - 1

print(total)
