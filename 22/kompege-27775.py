# kompege-27775
from dataclasses import dataclass
from itertools import product

@dataclass
class Process:
    duration: int
    deps: list[int]

A = [s.split() for s in open("22_27775.txt")]

proc = {}
for s in A[1:]:
    proc[int(s[0])] = Process(
        duration = int(s[1]),
        deps = [int(x) for x in s[2].replace('"', '').split(";")]
    )

def f(n):
    if proc[n].deps == [0]:
        return proc[n].duration + displacement[n]
    return max(f(x) for x in proc[n].deps) + proc[n].duration

L = []
for d in product(range(30), repeat = 3):
    displacement = dict(zip(
        [101, 102, 109, 110],
        [0] + list(d)
    ))
    
    T = {}
    for i, p in proc.items():
        finish = f(i)
        start = finish - p.duration
        T[start] = T.get(start, 0) + 1
        T[finish] = T.get(finish, 0) - 1

    times = sorted(T.keys())

    n = 0
    start = None

    for t in times:
        old = n
        n += T[t]
        if old != 5 and n == 5:
            start = t
        
        if old == 5 and n != 5:
            L.append(t - start)


print(max(L))
