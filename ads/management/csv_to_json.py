import csv
import json
import os
from pathlib import Path
from django.contrib.auth.hashers import make_password


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_URL = "fixtures"
JSON_ROOT = os.path.join(BASE_DIR, DATA_URL, 'JSON')
CSV_ROOT = os.path.join(BASE_DIR, DATA_URL, 'CSV')
list_files = os.listdir(CSV_ROOT)


def open_files_0():
    file = f'{CSV_ROOT}\category.csv'
    response = []

    with open(file, encoding='utf-8') as csv_f:
        csv_reader = csv.DictReader(csv_f)
        for rows in csv_reader:
            response.append(
                {
                    "pk": rows["id"],
                    "model": "ads.Characteristics",
                    "fields": {"name": rows["name"]}
                }
            )
    return response


def open_files_1():
    file = f'{CSV_ROOT}\\ad.csv'
    response = []

    with open(file, encoding='utf-8') as csv_f:
        csv_reader = csv.DictReader(csv_f)
        for rows in csv_reader:
            response.append(
                {
                    "pk": rows["Id"],
                    "model": "ads.Advertisement",
                    "fields": {
                        "name": rows["name"],
                        "author_id": rows["author_id"],
                        "price": rows["price"],
                        "description": rows["description"],
                        "image": rows["image"],
                        "is_published": rows["is_published"],
                        "category_id": rows["category_id"],
                               }
                }
            )
    return response


def open_files_2():
    file = f'{CSV_ROOT}\\location.csv'
    response = []

    with open(file, encoding='utf-8') as csv_f:
        csv_reader = csv.DictReader(csv_f)
        for rows in csv_reader:
            response.append(
                {
                    "pk": rows["id"],
                    "model": "ads.Location",
                    "fields": {
                        "name": rows["name"],
                        "lat": rows["lat"],
                        "lng": rows["lng"],
                               }
                }
            )
    return response

def open_files_3():
    file = f'{CSV_ROOT}\\user.csv'
    response = []

    with open(file, encoding='utf-8') as csv_f:
        csv_reader = csv.DictReader(csv_f)
        for rows in csv_reader:
            response.append(
                {
                    "pk": rows["id"],
                    "model": "auth.User",
                    "fields": {
                        "first_name": rows["first_name"],
                        "last_name": rows["last_name"],
                        "username": rows["username"],
                        "password": rows["password"],
                        "role": rows["role"],
                        "age": rows["age"],
                        "location_id": rows["location_id"],
                               }
                }
            )
    return response


def save_as(data, json_filename):
    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(data, ensure_ascii=False))


save_as(open_files_0(), f'{JSON_ROOT}\\category.json')
save_as(open_files_1(), f'{JSON_ROOT}\\ad.json')
save_as(open_files_2(), f'{JSON_ROOT}\\location.json')
save_as(open_files_3(), f'{JSON_ROOT}\\user.json')
