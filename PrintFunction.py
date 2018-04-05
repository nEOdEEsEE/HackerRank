from __future__ import print_function
import math
if __name__ == '__main__':
    n = int(raw_input())

solution = 0

for x in range (1, n + 1):
    m = int(math.log10(x)) + 1
    solution = (solution * (10 ** m)) + x

print(solution)
