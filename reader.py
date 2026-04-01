import csv


def read_files(file_paths):
    data = []

    for path in file_paths:
        try:
            with open(path, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row["coffee_spent"] = int(row["coffee_spent"])
                    data.append(row)
        except FileNotFoundError:
            raise ValueError(f"Файл не найден: {path}")

    return data