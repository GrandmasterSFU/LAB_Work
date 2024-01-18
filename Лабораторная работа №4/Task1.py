# TODO решите задачу
import json
def task() -> float:
    multiply = 0
    with open("input.json", "rt") as file:
        data = json.load(file)
        for i in data:
            multiply += i["score"] * i["weight"]
        return round(multiply, 3)


print(task())
