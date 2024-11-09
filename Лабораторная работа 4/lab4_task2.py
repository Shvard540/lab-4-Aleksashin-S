import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    lst = []
    with open(INPUT_FILENAME, "r") as f1:
        csv_read = csv.DictReader(f1, delimiter=',', quotechar='\n')
        for row in csv_read:
            lst.append(row)
            data = json.dumps(lst, indent=4)

            with open(OUTPUT_FILENAME, "w") as f2:
                f2.write(f"{data}")


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
