import os
from datetime import datetime
import re
import csv
import copy


def read_csv_file():
    """
    Функция находит в текущей директории .csv файл и парсит его
    :return: строчки файла в виде массива массивов
    """
    file_name = "-"
    for filename in os.listdir("."):
        if filename.endswith(".csv"):

            file_name = filename

    result = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:  # проверяем, что строка не пустая

                raw_mac = row[0].split(";")[0]
                number = row[0].split(";")[1]

                # дробление mac по 2 символа с точкой
                mac = ".".join([raw_mac[i:i + 2] for i in range(0, len(raw_mac), 2)])

                result.append([mac, number])

    return result[1:]  # слайс, чтобы не возвращать заголовки


def find_yaml_file():
    """
    Функция находит в текущей директории .yaml файл
    :return: название файла
    """

    for filename in os.listdir("."):
        if filename.endswith(".yaml"):

            return filename


def create_folder():
    """
    Функция создает папку с названием, равным текущему времени
    :return: название созданной папки
    """

    current_time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

    os.mkdir(current_time)

    return current_time


def config_yaml_files(file_name, data, folder_name):
    """
    Функция создает .yaml-файлы
    :param file_name: название файла-шаблона
    :param data: все данные для конфигурации файлов
    :param folder_name: название папки, куда загружать файл
    :return: True, если все получилось
    """

    yaml_template_data = ""  # заранее подготовленное место для шаблона, чтобы не открывать файл каждую итерацию

    # загрузка шаблона
    with open(file_name, 'r') as file:
        yaml_template_data = file.readlines()

    for element in data:
        raw_template = copy.deepcopy(yaml_template_data)  # полное копирование шаблона для редактирования

        mac = element[0]  # название файл
        new_value = element[1]  # новое значение для подставления

        line0_index = raw_template.index('        Line0:\n')  # элемент для ориентирования

        for i in range(line0_index+4, line0_index+8):
            # находим позиции двойных кавычек
            row = raw_template[i]
            a = row.index('"') + 1
            b = row.rindex('"')

            raw_template[i] = row[:a] + new_value + row[b:]

        file_path = os.path.join(folder_name, mac + '.yaml')
        with open(file_path, 'w') as f:
            for line in raw_template:
                f.write(line)

    return True
