import sys
import random

n = 50
seed = 42

if len(sys.argv) >= 2:
    n = int(sys.argv[1])
    if len(sys.argv) >= 3:
        seed = int(sys.argv[2])

random.seed(seed)

limit = 60 * 60 * 24 * 365
file = open(f"1_rs_Lmax/in_{n}_{seed}.txt", "w")

# generate p, r, d, s
p = [random.randint(1, limit // n * 2) for j in range(0, n)]
r = [random.randint(0, limit - 2 * p[j]) for j in range(0, n)]
d = [random.randint(r[j] + p[j], r[j] + 2 * p[j]) for j in range(0, n)]
s = [[random.randint(0, min(p[i], p[j])) if i != j else 0 for j in range(0, n)] for i in range(0, n)]

# write the number of tasks: n
file.write(str(n) + "\n")

# write processing time, ready time and due date of n tasks: p r d
for j in range(0, n):
    file.write(f"{p[j]} {r[j]} {d[j]}\n")

# write setup times of n x n tasks: s
for i in range(0, n):
    for j in range(0, n):
        file.write(f"{s[i][j]} ")
    file.write("\n")

file.close()
