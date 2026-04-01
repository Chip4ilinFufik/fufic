from collections import defaultdict
from statistics import median

from report.base import BaseReport

class MedianCoffeeReport(BaseReport):
    def generate(self, date):

        for r in data:
            student = r['student']
            grouped[student].append(r['coffee_spent'])