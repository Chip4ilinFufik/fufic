from collections import defaultdict
from statistics import median

from reports.base import BaseReport

class MedianCoffeeReport(BaseReport):
    def generate(self, data):
        grouped = defaultdict(list)

        for r in data:
            student = r['student']
            grouped[student].append(r['coffee_spent'])

        result = []
        for student, value in grouped.items():
            med = median(value)
            result.append((student, med))
        
        result.sort(key=lambda x: x[1], reverse=True)

        return result
