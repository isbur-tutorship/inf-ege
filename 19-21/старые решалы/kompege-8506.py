from functools import lru_cache

@lru_cache(None)
def f(a):
    if a >= 55:
        return 0
    turns = [a + 1, a + 4, 3 * a]
    if any(f(turn) == 0 for turn in turns):
        return 1
    if all(f(turn) == 1 for turn in turns):
        return 2
    if any(f(turn) == 2 for turn in turns):
        return 3
    if all(f(turn) in (1, 3) for turn in turns):
        return 4

for s in range(1, 55):
    if f(s) == 1:
        print(s)
        break