import csv
import json
import os
import datetime
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent

DATA_URL = "fixtures"
JSON_ROOT = os.path.join(BASE_DIR, DATA_URL, 'JSON')
CSV_ROOT = os.path.join(BASE_DIR, DATA_URL, 'CSV')
list_files = os.listdir(CSV_ROOT)
JSON_ROOT_2 = os.path.join(BASE_DIR, DATA_URL)

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
                        "author_id": int(rows["author_id"]),
                        "price": int(rows["price"]),
                        "description": rows["description"],
                        "image": rows["image"],
                        "is_published": True if rows["is_published"] == "TRUE" else False,
                        "category_id": int(rows["category_id"]),
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
                    "model": "authentication.LocationUser",
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
    response_u = []
    response_g = []
    response_g_t = []
    response_g_u = []

    with open(file, encoding='utf-8') as csv_f:
        csv_reader = csv.DictReader(csv_f)
        data = datetime.date.today()
        for rows in csv_reader:
            data_t = data
            if rows["role"] not in response_g_t:
                response_g_t.append(rows["role"])
                response_g.append(
                    {
                        "pk": response_g_t.index(rows["role"]) + 1,
                        "model": "auth.group",
                        "fields": {
                            "name": response_g_t[response_g_t.index(rows["role"])],
                        }
                    }

                )
            response_u.append(
                {
                    "pk": rows["id"],
                    "model": "authentication.user",
                    "fields": {
                        "first_name": rows["first_name"],
                        "last_name": rows["last_name"],
                        "username": rows["username"],
                        "email": f'{rows["username"]}@gmail.com',
                        "password": rows["password"],
                        "age": rows["age"],
                        "birth_date": str(data_t - datetime.timedelta(days=(365*int(rows["age"])))),
                        "location": rows["location_id"],
                            }
                    }
                )
            print(response_u)
            print(response_g_t.index(rows["role"]))

            response_g_u.append(
                {
                    "pk": rows["id"],
                    "model": "authentication.user_groups",
                    "fields": {
                        "user_id": int(rows["id"]),
                        "group_id": int(response_g_t.index(rows["role"])+1),
                    }
                }
            )

    with open(f'{JSON_ROOT_2}\\initial_data.json', 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(response_u, ensure_ascii=False))
    # with open(f'{JSON_ROOT}\\user_g.json', 'w', encoding='utf-8') as jsonfile:
    #     jsonfile.write(json.dumps(response_g, ensure_ascii=False))
    # with open(f'{JSON_ROOT}\\user_g_u.json', 'w', encoding='utf-8') as jsonfile:
    #     jsonfile.write(json.dumps(response_g_u, ensure_ascii=False))
    return f'OK'


def save_as(data, json_filename):
    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(data, ensure_ascii=False))


# save_as(open_files_0(), f'{JSON_ROOT}\\category.json' )
# save_as(open_files_1(), f'{JSON_ROOT}\\ad.json')
# save_as(open_files_2(), f'{JSON_ROOT}\\location.json')
print(open_files_3())
