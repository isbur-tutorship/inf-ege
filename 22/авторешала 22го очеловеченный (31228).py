proc = {}
with open("22-31228.txt") as f:
    for row in f:
        row = row.split()
        i = int(row[0])
        dur = int(row[1])
        deps = [int(x) for x in row[2].split(";")]
        proc[i] = (dur, deps)

from functools import lru_cache
# import sys
# sys.setrecursionlimit(10000)

@lru_cache(maxsize=None)
def solve(pid):
    dur, deps = proc[pid]
    if deps == [0]:
        s = 1
    else:
        dep_ends = [solve(d)[1] for d in deps]
        s = max(dep_ends) + 1
    e = s + dur - 1
    return (s, e)

res = {pid: solve(pid) for pid in proc}

from collections import Counter
per_ms = Counter()
for pid, (s, e) in res.items():
    for t in range(s, e + 1):
        per_ms[t] += 1

print("\nМаксимум параллельных процессов:", max(per_ms.values()))
