import sys

MAX_INT = 2**100

if len(sys.argv) >= 2 and sys.argv[1][-4:] == ".txt":
    # Load instance
    input_file = open(sys.argv[1], "r")
    n = int(input_file.readline())

    seed_index = sys.argv[1].find("_", sys.argv[1].find("_") + 1) + 1
    dot_index = sys.argv[1].find(".")
    seed = sys.argv[1][seed_index:dot_index]

    p = [[], [], [], []]
    d, a, b = [], [], []
    for j in range(n):
        line = input_file.readline().split()
        if len(line) != 7:
            sys.exit(f"ERROR in file {sys.argv[1]}: Wrong format at line {j + 2}.")
        p[0].append(int(line[0]))
        p[1].append(int(line[1]))
        p[2].append(int(line[2]))
        p[3].append(int(line[3]))
        d.append(int(line[4]))
        a.append(int(line[5]))
        b.append(int(line[6]))
    input_file.close()

    # Schedule jobs
    c = [-1] * n  # completion times
    schedule = []
    sum_ewdw = 0
    instant = [0] * 4

    while len(schedule) < n:
        schedule_goal = MAX_INT
        schedule_candidate = MAX_INT
        c_candidate = MAX_INT
        ewdw_candidate = MAX_INT
        instant_candidate = []

        for j in range(n):
            if c[j] == -1:  # job wasn't already scheduled
                tmp_instant = instant.copy()
                for m in range(4):
                    tmp_instant[m] = (max(tmp_instant[m], tmp_instant[m-1]) if m > 0 else tmp_instant[m]) + p[m][j]
                E = max(0, d[j] - tmp_instant[3])
                D = max(0, tmp_instant[3] - d[j])
                tmp_ewdw = E * a[j] + D * b[j]

                goal = (d[j] - tmp_instant[3]) * a[j]**3 + abs(tmp_instant[3] - d[j]) * b[j]**0.3

                if goal < schedule_goal\
                        or (goal == schedule_goal and tmp_ewdw < ewdw_candidate)\
                        or (schedule_goal == schedule_goal and tmp_ewdw == ewdw_candidate and d[j] < d[schedule_candidate])\
                        or (schedule_goal == schedule_goal and tmp_ewdw == ewdw_candidate and d[j] == d[schedule_candidate] and sum(tmp_instant) < sum(instant_candidate)):
                    schedule_goal = goal
                    schedule_candidate = j
                    c_candidate = tmp_instant[3]
                    ewdw_candidate = tmp_ewdw
                    instant_candidate = tmp_instant.copy()

        if schedule_candidate != MAX_INT:
            # job chosen - proceed
            c[schedule_candidate] = c_candidate
            sum_ewdw += ewdw_candidate
            instant = instant_candidate.copy()
            schedule.append(schedule_candidate)
        else:
            print("ERROR - no candidate found!")
            break

    # Save output to file
    output_file = open(f"F4_EwDw/out_{n}_{seed}.txt", "w")
    output_file.write(f"{sum_ewdw}\n")
    output_file.write(" ".join(map(str, schedule)))
    output_file.close()

else:
    sys.exit("Please run the algorithm with correctly named input file, e.g.:\n"
             + f"python {sys.argv[0]} F4_EwDw/in_50_42.txt")
