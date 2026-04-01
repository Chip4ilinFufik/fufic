import argparse
from tabulate import tabulate

from reader import read_files
from reports.median_coffee import MedianCoffeeReport


REPORTS = {
    "median-coffee": MedianCoffeeReport,
}


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)

    args = parser.parse_args()

    # проверка отчёта
    if args.report not in REPORTS:
        raise ValueError(f"Неизвестный отчёт: {args.report}")

    # читаем данные
    data = read_files(args.files)

    # создаём отчёт
    report_class = REPORTS[args.report]
    report = report_class()

    result = report.generate(data)

    # вывод
    print(tabulate(result, headers=["Student", "Median coffee spent"]))


if __name__ == "__main__":
    main()