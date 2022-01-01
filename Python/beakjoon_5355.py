import sys

def solve(target, inputs):
    target = float(target)
    
    print
    for module in inputs:
        if(module == '@'):
            target *= 3
        elif module == "%":
            target += 5
        elif module == "#":
            target -= 7
    
    return target
    


num = int(input())

for val in range(num):
    inputs = sys.stdin.readline().split()
    print("{:.2f}".format(solve(inputs[0], inputs[1:])))
