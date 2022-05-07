# to test git
import sys
from big_HI import *
if len(sys.argv) == 1:
    n = 4
else:
    n = int(sys.argv[1])

for _ in range(n):
    display_big_HI()
