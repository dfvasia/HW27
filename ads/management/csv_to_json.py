import csv
import json


def open_files_0():
    file = 'categories.csv'
    response = []

    with open(file, encoding='utf-8') as csv_f:
        csv_reader = csv.DictReader(csv_f)
        for rows in csv_reader:
            print(rows)
            response.append(
                {
                    "pk": rows["id"],
                    "model": "ads.Characteristics",
                    "fields": {"name": rows["name"]}
                }
            )
    return response

def open_files_1():
    file = 'ads.csv'
    response = []

    with open(file, encoding='utf-8') as csv_f:
        csv_reader = csv.DictReader(csv_f)
        for rows in csv_reader:
            print(rows)
            response.append(
                {
                    "pk": rows["Id"],
                    "model": "ads.Advertisement",
                    "fields": {
                        "name": rows["name"],
                        "author": rows["author"],
                        "price": rows["price"],
                        "description": rows["description"],
                        "address": rows["address"],
                        "is_published": rows["is_published"],
                               }
                }
            )
    return response

def save_as(data, json_filename):
    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(data, ensure_ascii=False))


save_as(open_files_0(), '..\\fixtures\\categories.json')
save_as(open_files_1(), '..\\fixtures\\ads.json')
