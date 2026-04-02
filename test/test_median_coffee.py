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

def test_multiple_students():
    data = [
        {"student": "Ivan", "coffee_spent": 100},
        {"student": "Ivan", "coffee_spent": 200},
        {"student": "Anna", "coffee_spent": 300},
        {"student": "Anna", "coffee_spent": 500},
    ]

    report = MedianCoffeeReport()
    result = report.generate(data)

    assert ("Ivan", 150) in result
    assert ("Anna", 400) in result

def test_sorting_desc():
    data = [
        {"student": "A", "coffee_spent": 100},
        {"student": "A", "coffee_spent": 200},
        {"student": "B", "coffee_spent": 300},
        {"student": "B", "coffee_spent": 400},
    ]

    report = MedianCoffeeReport()
    result = report.generate(data)

    # B должен быть первым (медиана 350 > 150)
    assert result[0][0] == "B"
    assert result[1][0] == "A"