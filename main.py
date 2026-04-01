import argparse
from unittest import result
from tabulate import tabulate
from reader import read_files
from reports.median_coffee import MedianCoffeeReport

REPORTS = {
    'median_coffee': MedianCoffeeReport,
}

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--report", nargs="+", required=True)
    parser.add_argument("--report", required=True)

    args = parser.parse_args()


    if args.report not in REPORTS:
        raise ValueError(f"Неизвестный отчет {args.report}")
    
    data - read_files(args.files)

    report_class = REPORTS[args.report]
    report = report_class()

    result = report.generate(data)
    print(tabulate(result, headers=["student", "coffee"]))

if __name__ == "__main__":
    main()