# to test git
import sys
if len(sys.argv) == 1:
    n = 4
else:
    n = int(sys.argv[1])

for _ in range(n):
    print('Hi')
