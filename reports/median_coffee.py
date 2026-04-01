from collections import defaultdict
from statistics import median

from reports.base import BaseReport


class MedianCoffeeReport(BaseReport):
    def generate(self, data):
        grouped = defaultdict(list)

        # группируем по студентам
        for row in data:
            student = row["student"]
            grouped[student].append(row["coffee_spent"])

        # считаем медиану
        result = []
        for student, values in grouped.items():
            med = median(values)
            result.append((student, med))

        # сортируем по убыванию
        result.sort(key=lambda x: x[1], reverse=True)

        return result