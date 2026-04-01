import argparse
from tabulate import tabulate
from reader import read_files
from reports.median_coffee import MedianCoffeeReport

REPORTS = {
    'median_coffee': MedianCoffeeReport,
}

