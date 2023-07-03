import sys

def concatenate(number):
    try:
        result = str(number) + "1"
        return result
    except Exception as e:
        print("Error:", e)

# Проверка наличия параметра
if len(sys.argv) > 1:
    # Передача параметра в функцию и печать результата
    concatenated_number = concatenate(sys.argv[1])
    if concatenated_number:
        print(concatenated_number)
else:
    print("Error: A parameter must be provided.")
