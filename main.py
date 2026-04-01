import argparse
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
