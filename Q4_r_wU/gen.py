import sys
import random
import math


def random_gauss_limits(mu, sigma, a, b):
    return min(b, max(a, round(random.gauss(mu=mu, sigma=sigma))))

n = 50
seed = 42

if len(sys.argv) >= 2:
    n = int(sys.argv[1])
    if len(sys.argv) >= 3:
        seed = int(sys.argv[2])

random.seed(seed)

file = open(f"Q4_r_wU/in_{n}_{seed}.txt", "w")

# generate b, p, r, d, w
e_core = 1.0
p_cores = [round(random.uniform(1.25, 2.0), 3) for m in range(3)]
b = [e_core, *p_cores]
random.shuffle(b)
p = [random.randint(1, 2**20) for j in range(0, n)]
r = [random.randint(0, math.ceil(sum(p) / sum(b)) - round(p[j] * 1.05)) for j in range(0, n)]
d = [random.randint(r[j] + math.ceil(p[j] / max(b)), r[j] + round(p[j] * 1.05)) for j in range(0, n)]
w = [random_gauss_limits(mu=20, sigma=5, a=1, b=40) for j in range(0, n)]

# write the number of tasks: n
file.write(str(n) + "\n")

# write b speeds
for proc in range(4):
    file.write(str(b[proc]))
    if proc < 3:
        file.write(" ")
    else:
        file.write("\n")

# write processing time, ready time, due date and weight of n tasks: p r d w
for j in range(0, n):
    file.write(f"{p[j]} {r[j]} {d[j]} {w[j]}\n")

file.close()
