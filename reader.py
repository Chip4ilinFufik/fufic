import csv


def read_files(file_paths):
    date = []
    for path in file_paths:
        try:
            with open(path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row["coffee_spent"] = int(row["coffee_spent"])
                    date.append(row)
        except FileNotFoundError:
            print(f"Файл {path} не найден.")

    return date
