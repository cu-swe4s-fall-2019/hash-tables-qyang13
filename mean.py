import sys
import statistics

# Simple line of command that calculate mean from stdin
V = []
for l in sys.stdin:
    V.append(float(l))
print(statistics.mean(V))
