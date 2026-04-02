from reports.median_coffee import MedianCoffeeReport

def test_median_single_student():
    data =[
        {"student": "Alice", "coffee_spent": 250},
        {"student": "Bob", "coffee_spent": 300},
        {"student": "Charlie", "coffee_spent": 200}
    ]
    report = MedianCoffeeReport()
    result = report.generate(data)
    

    assert ("Alice", 250) in result