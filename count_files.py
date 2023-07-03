import os
import sys

def count_files_in_directory(directory):
    try:
        file_count = 0
        file_list = []
        for _, _, files in os.walk(directory):
            file_count += len(files)
            file_list.extend(files)
        return file_count, file_list
    except Exception as e:
        print("Error:", e)

# Проверка наличия параметра
if len(sys.argv) > 1:
    target_directory = sys.argv[1]
    # Проверка на существование каталога и подсчет файлов
    if os.path.isdir(target_directory):
        file_count, file_list = count_files_in_directory(target_directory)
        if file_count is not None:
            print("Total files in directory:", file_count)
            for file in file_list:
                print(file)
    else:
        print("Error: The specified directory does not exist.")
else:
    print("Error: A directory path must be provided.")
