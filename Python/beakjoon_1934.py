import sys

def GCD(A, B):
    while B != 0:
        r = A % B
        A = B
        B = r
    
    return A


num = int(input())

for iter in range(num):
    A, B = map(int, sys.stdin.readline().split())
    print(int(A * B / GCD(A, B)))
