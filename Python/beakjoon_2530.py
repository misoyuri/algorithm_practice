import sys

h, m, s = map(int, sys.stdin.readline().split())
s += int(sys.stdin.readline())

m += int(s / 60)
s = s % 60

h += int(m / 60)
m = m % 60

h = h % 24

print(h, m, s)
