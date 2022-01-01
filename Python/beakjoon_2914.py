import sys

num, means = map(int, sys.stdin.readline().split())

print(num * (means - 1) + 1)