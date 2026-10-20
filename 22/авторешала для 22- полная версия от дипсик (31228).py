# -*- coding: utf-8 -*-
# Данные задачи 22 (из файла 22.ods). A=ID, B=длительность, C/D/E = ID процессов, от которых зависит процесс.
# Процесс 1 соответствует строке 2.


proc = {}
with open("22-31228.txt") as f:
    for row in f:
        row = row.split()
        i = int(row[0])
        dur = int(row[1])
        deps = [int(x) for x in row[2].split(";")]
        proc[i] = (dur, deps)

# proc = {
    # 1:  (4, [3, 25]),
    # 2:  (3, [8, 6, 15]),
    # 3:  (1, [15, 22]),
    # 4:  (4, [7, 14]),
    # 5:  (2, [15, 8]),
    # 6:  (1, [8, 13, 16]),
    # 7:  (6, [17]),
    # 8:  (1, [25, 3, 22]),
    # 9:  (3, [17, 19, 2]),
    # 10: (1, [19, 8]),
    # 11: (6, [25]),
    # 12: (6, [22]),
    # 13: (1, [25, 16, 15]),
    # 14: (1, [11, 19]),
    # 15: (3, [17, 25]),
    # 16: (4, [25]),
    # 17: (2, []),
    # 18: (6, [22]),
    # 19: (5, [22]),
    # 20: (3, [22, 10, 12]),
    # 21: (6, [17]),
    # 22: (4, []),
    # 23: (4, [18]),
    # 24: (4, [21, 22, 25]),
    # 25: (5, []),
# }

# Считаем по правилу: старт = max(конец зависимостей) + 1; если зависимостей нет, старт = 1 (нумерация мс с 1).
# Конец = старт + длительность - 1. Итерируем до стабилизации (граф ацикличный).
# start = {}
# end = {}
# for _ in range(30):
    # changed = False
    # for pid, (dur, deps) in proc.items():
        # if not deps:
            # s = 1
        # else:
            # s = max(end.get(d, 1) for d in deps) + 1  # d ещё не посчитан? берём минимум 1
        # e = s + dur - 1
        # if start.get(pid) != s or end.get(pid) != e:
            # start[pid], end[pid] = s, e
            # changed = True
    # if not changed:
        # break
    # при первом проходе часть end ещё не известна; повторяем

# Более надёжно: решаем в порядке топологической сортировки (по возрастанию ID после разрешения).
# Граф должен быть ацикличным; решаем функцией с мемоизацией.
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

# print("ID dur deps  -> start end")
# for pid in sorted(proc):
    # dur, deps = proc[pid]
    # s, e = res[pid]
    # print(f"{pid:>2} {dur:>3} {str(deps):<22} -> {s:>2} {e:>2}")

# Сколько процессов выполняется в каждую миллисекунду
from collections import Counter
per_ms = Counter()
for pid, (s, e) in res.items():
    for t in range(s, e + 1):
        per_ms[t] += 1

# max_t = max(per_ms)
print("\nМаксимум параллельных процессов:", max(per_ms.values()))
# print("Распределение по миллисекундам (мс: количество):")
# for t in sorted(per_ms):
    # print(f"  мс {t:>2}: {per_ms[t]}")

# Строка J (конец) и I (старт) как в таблице
# print("\nСоответствие столбцам (I=start, J=end):")
# for pid in sorted(proc):
    # s, e = res[pid]
    # print(f"  строка {pid+1}: process {pid}  start(I)={s}  end(J)={e}  J-B={e}")