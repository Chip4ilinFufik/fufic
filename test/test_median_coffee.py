from reports.median_coffee import MedianCoffeeReport

def test_median_single_student():
    data =[
        {"student": "Alice", "coffee": 250},
        {"student": "Bob", "coffee": 300},
        {"student": "Charlie", "coffee": 200}
    ]
    report = MedianCoffeeReport()
    result = report.generate(data)

    assert ("alice", 250) in result