import json

FILENAME = "input.json"


def task() -> float:
    summa = 0
    with open(FILENAME, "r") as f1:
        dct = json.load(f1)

    for i in dct:
        sc = i.get("score")
        we = i.get("weight")
        pr = sc * we
        summa += pr

    res = round(summa, 3)
    return res


print(task())
