from funcs import *
from datetime import datetime


errors = 0  # переменная для подсчета ошибок

try:
    print("Конфигурация файлов началась в ", datetime.now().strftime("%H:%M:%S"))
    template_file = find_yaml_file()  # шаблон файла

    data = read_csv_file()  # данные

    folder_name = create_folder()

    res = config_yaml_files(template_file, data, folder_name)

except Exception as e:
    print(str(e))
    errors += 1

print("Конфигурация файлов закончилась в ", datetime.now().strftime("%H:%M:%S"), "ошибок: ", errors)
