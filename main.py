# Задача с семинара: ✔Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔Каждая группа включает файлы с несколькими расширениями.
# ✔В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
import os
import shutil
from random import randint



def create_files(extentions, numbers):
    for i in range(len(numbers)):
        for j in range(numbers[i]):
            with open(f"file_{randint(0, 9)}.{extentions[i]}", 'w') as file:
                print(f'file {extentions[i]} {j} is ready')


def delete_files():
    files_list = os.listdir()
    print(files_list)
    for file in files_list:

        if os.path.isdir(file) and file in folder_for_format:
            shutil.rmtree(file)
        elif os.path.isfile(file) and file.split('.')[1] in formats:
            os.remove(file)

formats = ['txt', 'mp3', 'doc', 'docx', 'md', 'wav', "FLAC", 'bin', 'csv', 'xls', 'xlsx', 'jpg', 'png']
create_files(formats, [randint(0, 2) for _ in formats])
folder_for_format = {"Texts": ('txt', 'doc', 'docx'),
                     "Music": ('mp3', 'wav', "FLAC"),
                     "Tables": ('csv', 'xls', 'xlsx'),
                     "Pictures": ('jpg', 'png')}


def sort_files(dir):
    os.chdir(dir)

    for file in os.listdir():
        if os.path.isfile(file):
            for key, value in folder_for_format.items():
                if file.split('.')[1] in value:
                    if key not in os.listdir():
                        os.mkdir(key)
                        print(f'folder {key} is created')
                    os.replace(file, os.path.join(os.getcwd(), key, file))

if __name__ =="__main":
    sort_files('/Users/anastasiabuglakova/Documents/GEEK/Погружение в Python/HW7')
    delete_files()
# для удаления папок и файлов в форматах в них не вошедших

import os.path


# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

def rename_files(diapazon_of_origin_name, num_of_numbers, extension, desire_name="your_file"):
    n = 0
    if os.getcwd().split('/')[-1] != "HW7":
        os.chdir('HW7')
    files_list = os.listdir()
    for file in files_list:
        if os.path.isfile(file) and file.split('.')[1] == extension:
            new_name = desire_name + file[diapazon_of_origin_name[0]: diapazon_of_origin_name[0] + 1]
            new_name += '0' * (num_of_numbers - len(str(n))) + str(n) + '.' + extension
            n += 1
            os.rename(file, new_name)

if __name__ =="__main":
    rename_files((0, 3), 5, 'md', 'Nastya')

# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
