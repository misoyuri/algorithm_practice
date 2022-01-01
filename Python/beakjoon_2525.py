import sys

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

B += C
A_ = int(B / 60)
B = B % 60

A += A_
if A >= 24:
    A -= 24
    
print(A, B)