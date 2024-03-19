import os
import csv

"""1 - Відкрити файл test_file.csv, прочитати його, зп співробітників у доларах перевести в гривні
на поточну дату  (курс задається окремою змінною). Результат зберегти новий файл salaries_uah.csv"""

UAH_USD_RATE = 38.5


def read_csv():
    file_path = os.path.abspath("test_file.csv")
    data = []

    with open(file=file_path, newline='', mode='r') as file:
        rows = csv.reader(file)
        for row in rows:
            data.append(row)
    return data


def _usd_to_uah(data):
    refined_data = [[int(item) if item.isdigit() else item for item in row] for row in data]
    converted_list = [[str(item * UAH_USD_RATE) if isinstance(item, int) else item for item in row] for row in
                      refined_data]
    return converted_list


def convert_to_uah():
    data = read_csv()
    data_with_converted_values = _usd_to_uah(data)
    new_file = os.getcwd() + "/salaries_uah.csv"

    with open(file=new_file, newline='', mode='w') as file:
        rows = csv.writer(file)
        rows.writerows(data_with_converted_values)


convert_to_uah()
