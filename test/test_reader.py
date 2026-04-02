import os
from reader import read_files


def test_read_files(tmp_path):
    file = tmp_path / "math.csv"

    file.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Иван,2024-01-01,100,5,10,ok,math\n",
        encoding="utf-8"
    )

    data = read_files([str(file)])

    assert len(data) == 1
    assert data[0]["student"] == "Иван"
    assert data[0]["coffee_spent"] == 100