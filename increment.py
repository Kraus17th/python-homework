import sys

def increment(number):
    try:
        # Преобразование параметра в число
        number = int(number)
        # Прибавление единицы
        result = number + 1
        return result
    except ValueError:
        print("Error: The parameter must be a number.")

# Проверка, передан ли параметр
if len(sys.argv) > 1:
    # Передача параметра в функцию и печать результата
    incremented_number = increment(sys.argv[1])
    print(incremented_number)
else:
    print("Error: A parameter must be provided.")
