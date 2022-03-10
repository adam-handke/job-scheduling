# job-scheduling
A suite of Python algorithms for solving various <a href="https://en.wikipedia.org/wiki/Optimal_job_scheduling">job scheduling</a> problems:
* `1_rs_Lmax` (1 | r<sub>j</sub>, S<sub>ij</sub> | L<sub>max</sub>) - single machine; jobs with processing times *p*, ready times *r*, due times *d* and setup times *s*; objective: minimizing maximum lateness *L<sub>max</sub>*. 
* `Q4_r_wU` (Q4 | r<sub>j</sub> | Σw<sub>j</sub>U<sub>j</sub>) - four uniform machines with speed coefficients *b*; jobs with processing times *p*, ready times *r*, due times *d* and weights *w*; objective: minimizing weighted number of late jobs (*U* - lateness indicator).
* `F4_EwDw` (F4 | | E<sub>w</sub> + D<sub>w</sub>) - Flow-shop with four machines; jobs with processing times of tasks *p*, due times *d*, earliness weights *a* and tardiness weights *b*; objective: minimizing the sum of weighted earliness and weighted tardiness.

All algorithms `alg.py` are <a href="https://en.wikipedia.org/wiki/List_scheduling">greedy list algorithms</a> with carefully designed priority functions. They are bundled with custom-made instance generators `gen.py` which accept variable number of jobs *n* and random seed.
All `*.py` files are disjointed entities without interdependencies, so they can be used separately at will.

## Requirements
* Python 3

## Instance format
Note: All values except speed coefficients *b* must be integers.

### Filename:
```
in_N_seed.txt
```

### `1_rs_Lmax`:
```
n
p1 r1 d1
p2 r2 d2
...
pn rn dn
s11 ... s1n
...
sn1 ... snn
```
### `Q4_r_wU`:
```
n
b1 b2 b3 b4
p1 r1 d1 w1
p2 r2 d2 w2
...
pn rn dn wn
```
### `F4_EwDw`:
```
n
p11 p12 p13 p14 d1 a1 b1
p21 p22 p23 p24 d2 a2 b2
...
pn1 pn2 pn3 pn4 dn an bn
```

## Solution format
### Filename:
```
out_N_seed.txt
```

### `1_rs_Lmax`:
```
Lmax
J1 J2 ... Jn
```
### `Q4_r_wU`:
```
ΣwjUj
J11 J12 ...
J21 J22 ...
J31 J32 ...
J41 J42 ...
```
### `F4_EwDw`:
```
ΣajEj+bjDj
J1 J2 ... Jn
```

## Running examples

### Generate an instance with *100* jobs and seed *1234* for the `1_rs_Lmax` problem:
```bash
python 1_rs_Lmax/gen.py 100 1234
```

### Solve the instance `in_100_1234.txt` generated above:
```bash
python 1_rs_Lmax/alg.py 1_rs_Lmax/in_100_1234.txt
```