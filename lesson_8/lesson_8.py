import os
import csv

"""1 - Відкрити файл test_file.csv, прочитати його, зп співробітників у доларах перевести в гривні
на поточну дату  (курс задається окремою змінною). Результат зберегти новий файл salaries_uah.csv"""

UAH_USD_RATE = 38.5


def read_csv():
    file_path = os.path.abspath("test_file.csv")

    with open(file=file_path, newline='', mode='r') as file:
        rows = csv.reader(file)
        data = list(rows)
    return data


def convert_to_uah():
    data = read_csv()
    new_file = os.getcwd() + "/salaries_uah.csv"

    for row in data[1:]:
        for item in range(1, len(row)):
            row[item] = round(int(row[item]) * UAH_USD_RATE)

    with open(file=new_file, newline='', mode='w') as file:
        rows = csv.writer(file)
        rows.writerows(data)


convert_to_uah()
