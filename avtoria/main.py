# import csv
#
# import requests
# from bs4 import BeautifulSoup
#
#
# # base_url = 'https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&categories.main.id=1&country.import.usa.not=-1&price.currency=1&abroad.not=0&custom.not=1&page=0&size=10&scrollToAuto=35991108'
#
#
# def get_page_content(page: int, page_size: int = 100):
#     base_url = 'https://auto.ria.com/uk/search/'
#     query_params = {
#         'indexName': 'auto,order_auto,newauto_search',
#         'categories.main.id': '1',
#         'country.import.usa.not': '-1',
#         'price.currency': '1',
#         'abroad.not': '0',
#         'custom.not': '1',
#         'page': page,
#         'size': page_size,
#     }
#
#     response = requests.get(base_url, params=query_params)
#     response.raise_for_status()
#     return response.text
#
#
# class CSVWriter:
#     def __init__(self, file_name: str, headers: list):
#         self.file_name = file_name
#         with open(self.file_name, 'w') as file:
#             # headers = ['car_id', 'car_mark_details', 'car_model_name', 'car_year', 'car_link_to_view']
#             write = csv.writer(file)
#             write.writerow(headers)
#
#     def write_data(self, data):
#         with open(self.file_name, 'a') as file:
#             write = csv.writer(file)
#             write.writerow(data)
#
#
# class StdoutWriter:
#     def write_data(self, data):
#         print(data)
#
# def main():
#     page = 0
#     headers = ['id', 'mark', 'model', 'year', 'link']
#     writers = (
#         CSVWriter('cars1.csv', headers),
#         StdoutWriter(),
#     )
#
#     while True:
#         if page > 2:
#             break
#         #      В ДЗ убрать ограничение по парсингу
#
#         print(f"Processing page {page}!")
#         page_content = get_page_content(page)
#         # page += 1
#
#         soup = BeautifulSoup(page_content, 'html.parser')
#         search_results = soup.find('div', id="searchResults")
#         ticket_items = search_results.find_all("section", class_="ticket-item")
#
#         if not ticket_items:
#             print(f"Nomore items on page {page}!")
#             break
#
#         for ticket_item in ticket_items:
#             car_details = ticket_item.find("div", class_="hide")
#             car_id = car_details['data-id']
#             car_mark_details = car_details['data-mark-name']
#             car_model_name = car_details['data-model-name']
#             car_year = car_details['data-year']
#
#             car_link_to_view = car_details['data-link-to-view']  # Для ДЗ
#
#             data = [car_id, car_mark_details, car_model_name, car_year, car_link_to_view]
#
#             for writer in writers:
#                 writer.write_data(data)
#
#         page += 1
#
#
# if __name__ == '__main__':
#     main()


# Методы записи до создания класса
# def write_headers_to_csv():
#     with open('cars.csv', 'w') as file:
#         headers = ['car_id', 'car_mark_details', 'car_model_name', 'car_year', 'car_link_to_view']
#         write = csv.writer(file)
#         write.writerow(headers)
#
#
# def write_data_ta_csv(data):
#     with open('cars.csv', 'a') as file:
#         write = csv.writer(file)
#         write.writerow(data)


# import csv
# import requests
# from bs4 import BeautifulSoup
# import sqlite3
#
#
# def get_page_content(page: int, page_size: int = 100):
#     base_url = 'https://auto.ria.com/uk/search/'
#     query_params = {
#         'indexName': 'auto,order_auto,newauto_search',
#         'categories.main.id': '1',
#         'country.import.usa.not': '-1',
#         'price.currency': '1',
#         'abroad.not': '0',
#         'custom.not': '1',
#         'page': page,
#         'size': page_size,
#     }
#
#     response = requests.get(base_url, params=query_params)
#     response.raise_for_status()
#     return response.text
#
#
# class DataWriter:
#     """
#     класс отвечает за запись данных в CSV-файл и базу данных SQLite3
#     """
#     def __init__(self, csv_file: str, db_file: str, headers: list):
#         self.csv_file = csv_file
#         self.db_file = db_file
#         self.headers = headers
#
#         # Создание таблицы в базе данных SQLite3
#         self.conn = sqlite3.connect(self.db_file)
#         self.cursor = self.conn.cursor()
#         # создается таблица cars в базе данных SQLite3
#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS cars
#                              (id INTEGER PRIMARY KEY,
#                               car_id INTEGER,
#                               car_mark_details TEXT,
#                               car_model_name TEXT,
#                               car_year INTEGER,
#                               car_link_to_view TEXT)''')
#         self.conn.commit()
#
#         # Создание CSV-файла и запись заголовков
#         with open(self.csv_file, 'w') as file:
#             write = csv.writer(file)
#             write.writerow(self.headers)
#
#     def write_data(self, data):
#         """записывает данные в CSV-файл и базу данных SQLite3"""
#         with open(self.csv_file, 'a') as file:
#             write = csv.writer(file)
#             write.writerow(data)
#
#         # Запись данных в базу данных SQLite3 !!!!!!!!!!!!!!!
#         self.cursor.execute('''INSERT INTO cars (car_id, car_mark_details, car_model_name, car_year, car_link_to_view)
#                                VALUES (?, ?, ?, ?, ?)''', data)
#         self.conn.commit()
#
#
# def main():
#     page = 0
#     headers = ['id', 'mark', 'model', 'year', 'link']
#
#     # Инициализация объекта для записи данных
#     writer = DataWriter('cars.csv', 'cars.db', headers)
#
#     while True:
#         if page > 2:
#             break
#         #      В ДЗ убрать ограничение по парсингу
#
#         print(f"Processing page {page}!")
#         page_content = get_page_content(page)
#         # page += 1
#
#         soup = BeautifulSoup(page_content, 'html.parser')
#         search_results = soup.find('div', id="searchResults")
#         ticket_items = search_results.find_all("section", class_="ticket-item")
#
#         if not ticket_items:
#             print(f"No more items on page {page}!")
#             break
#
#         for ticket_item in ticket_items:
#             car_details = ticket_item.find("div", class_="hide")
#             car_id = car_details['data-id']
#             car_mark_details = car_details['data-mark-name']
#             car_model_name = car_details['data-model-name']
#             car_year = car_details['data-year']
#             car_link_to_view = car_details['data-link-to-view']
#
#             data = [car_id, car_mark_details, car_model_name, car_year, car_link_to_view]
#
#             # Запись данных
#             writer.write_data(data)
#
#         page += 1
#
#
# if __name__ == '__main__':
#     main()


import csv
import requests
from bs4 import BeautifulSoup
import sqlite3


def get_page_content(page: int, page_size: int = 100):
    base_url = 'https://auto.ria.com/uk/search/'
    query_params = {
        'indexName': 'auto,order_auto,newauto_search',
        'categories.main.id': '1',
        'country.import.usa.not': '-1',
        'price.currency': '1',
        'abroad.not': '0',
        'custom.not': '1',
        'page': page,
        'size': page_size,
    }

    response = requests.get(base_url, params=query_params)
    response.raise_for_status()
    return response.text


class CSVWriter:
    """
    Класс отвечает за запись данных в CSV-файл
    """
    def __init__(self, file_name: str, headers: list):
        self.file_name = file_name
        with open(self.file_name, 'w') as file:
            write = csv.writer(file)
            write.writerow(headers)

    def write_data(self, data):
        """Записывает данные в CSV-файл"""
        with open(self.file_name, 'a') as file:
            write = csv.writer(file)
            write.writerow(data)


class SQLiteWriter:
    """
    Класс отвечает за запись данных в базу данных SQLite3
    """
    def __init__(self, db_file: str):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cars
                             (id INTEGER PRIMARY KEY,
                              car_id INTEGER,
                              car_mark_details TEXT,
                              car_model_name TEXT,
                              car_year INTEGER,
                              car_link_to_view TEXT,
                              data_main_price INTEGER)''')
        self.conn.commit()

    def write_data(self, data):
        """Записывает данные в базу данных SQLite3"""
        self.cursor.execute('''INSERT INTO cars (car_id, car_mark_details, car_model_name, car_year, car_link_to_view, data_main_price)
                               VALUES (?, ?, ?, ?, ?, ?)''', data)
        self.conn.commit()


def main():
    page = 0
    headers = ['id', 'mark', 'model', 'year', 'link']

    # Инициализация объектов для записи данных в CSV и SQLite3
    csv_writer = CSVWriter('cars.csv', headers)
    sqlite_writer = SQLiteWriter('cars.db')

    while True:
        #if page > 2:
        #    break

        print(f"Processing page {page}!")
        page_content = get_page_content(page)

        soup = BeautifulSoup(page_content, 'html.parser')
        search_results = soup.find('div', id="searchResults")
        ticket_items = search_results.find_all("section", class_="ticket-item")

        if not ticket_items:
            print(f"No more items on page {page}!")
            break

        for ticket_item in ticket_items:
            car_details = ticket_item.find("div", class_="hide")
            car_id = car_details['data-id']
            car_mark_details = car_details['data-mark-name']
            car_model_name = car_details['data-model-name']
            car_year = car_details['data-year']
            car_link_to_view = car_details['data-link-to-view']

            content_bar = ticket_item.find("div", class_="content-bar")
            price_ticket = content_bar.find("div", class_="price-ticket")
            data_main_price = price_ticket.get("data-main-price", None)

            data = [car_id, car_mark_details, car_model_name, car_year, car_link_to_view, data_main_price]

            # Запись данных в CSV и SQLite3
            csv_writer.write_data(data)
            sqlite_writer.write_data(data)

        page += 1


if __name__ == '__main__':
    main()