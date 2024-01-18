
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    Array = []
    with open(INPUT_FILENAME, "rt") as file:
        data = [line for line in csv.DictReader(file)]
        for row in data:
            Array.append(row)
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as rr:
        rr.write(json.dumps(Array, indent=4))


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
