import os
import time

directory = '.'

for root, dirs, files in os.walk(directory):
    if files:
        for file in files:
            filepath = os.path.join(root, file)
            filetime = os.path.getmtime(filepath)
            formatted_time = (time.strftime
                              ('%a,%d %b %Y %H:%M:%S', time.localtime(filetime)))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.dirname(filepath)

            print(f'Обнаружен файл: {file} Путь: {filepath}, Размер: {filesize} байт,'
                  f' Время  изменения: {formatted_time}, Родительская  директория:'
                  f' {parent_dir} ')
