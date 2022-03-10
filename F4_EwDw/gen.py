import sys
import random

def random_gauss_limits(mu, sigma, left, right):
    return min(right, max(left, round(random.gauss(mu=mu, sigma=sigma))))


n = 50
seed = 42

if len(sys.argv) >= 2:
    n = int(sys.argv[1])
    if len(sys.argv) >= 3:
        seed = int(sys.argv[2])

random.seed(seed)

file = open(f"F4_EwDw/in_{n}_{seed}.txt", "w")

# generate p, d, a, b
p = [[random_gauss_limits(100, 40, 10, 200) for j in range(n)] for op in range(4)]
sum_all_p_over4 = round(sum([sum(row) for row in p]) / 4)
d = [random_gauss_limits(round(sum_all_p_over4 / 2), round(sum_all_p_over4 / 5),
                         sum([row[j] for row in p]), sum_all_p_over4) for j in range(n)]
a, b = tuple([random_gauss_limits(5, 2, 1, 10) for j in range(n)] for w in range(2))


# write the number of tasks: n
file.write(str(n) + "\n")

# write processing times, due date and weights of n tasks: p1 p2 p3 p4 d a b
for j in range(n):
    file.write(f"{p[0][j]} {p[1][j]} {p[2][j]} {p[3][j]} {d[j]} {a[j]} {b[j]}\n")

file.close()
