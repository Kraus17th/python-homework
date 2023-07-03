import os
import sys

def check_object_type(path):
    if os.path.isfile(path):
        return "File"
    elif os.path.isdir(path):
        return "Directory"
    else:
        return "Object does not exist"

# Проверка наличия параметра
if len(sys.argv) > 1:
    object_path = sys.argv[1]
    # Проверка типа объекта и печать результата
    object_type = check_object_type(object_path)
    print(object_type)
else:
    print("Error: A object path must be provided.")
