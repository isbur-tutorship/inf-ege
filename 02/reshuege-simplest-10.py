import json

expressions = [
    "((x == (w or y)) or ((w <= z) and (y <= w)))",
    "((x and (not y)) or (y == z) or (not w))",
    "((x and (not y)) or (y == z) or w)",
    "(((x <= y) <= z) or (not w))",
    "(z or (z == w) or (not (y <= x)))",
    "((not (x <= w)) or (y == z) or y)",
    "(((x <= y) or (z <= w)) and ((z == y) <= (w == x)))",
    "((x and (not y)) or (x == z) or w)",
]

ids = [
    15814,
    18071,
    15970,
    69880,
    81468,
    45236,
    56502,
    59680
]

targets = [
    [
        [1, None, None, 1],
        [None, None, None, 1],
        [1, None, 1, None]
    ],
    [
        [0, None, None, 0],
        [0, 1, 0, 1],
        [None, 1, 0, None]
    ],
    [
        [None, None, None, 1],
        [1, 0, 0, 0],
        [1, 1, 0, None]
    ],
    [
        [None, 0, None, 0],
        [1, None, None, None],
        [0, 1, None, None]
    ],
    [
        [None, None, 0, 1],
        [None, 1, None, 0],
        [None, 0, None, None]
    ],
    [
        [None, 1, None, 0],
        [None, 0, 1, None],
        [None, None, 0, None]
    ],
    [
        [None, 1, 0, None],
        [0, 1, 0, 1],
        [None, 1, 0, None]
    ],
    [
        [None, None, 0, 1],
        [1, 0, None, 1],
        [1, 1, 0, None]
    ]
]

answers = [
    "yxzw",
    "xwzy",
    "yxwz",
    "xywz",
    "wxzy",
    "zxwy",
    "yxwz",
    "yxwz"
]


levels = []
for i, e in enumerate(expressions):
    id = "reshuege-" + str(ids[i])
    name = str(i+3).zfill(2)
    current = []
    for w in 0,1:
        for x in 0,1:
            for y in 0,1:
                for z in 0,1:
                    if eval(e) == 0:
                        current.append([w, x, y, z])
    target = targets[i]
    correctOrder = answers[i]
    level = {
        "id": id,
        "name": name,
        "current": current,
        "target": target,
        "correctOrder": correctOrder
    }
    levels.append(level)

with open("levels.json", "w", encoding="utf-8") as f:
    json.dump(levels, f, ensure_ascii=False, indent=2)
