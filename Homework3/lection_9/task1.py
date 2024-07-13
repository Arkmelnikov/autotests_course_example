# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код

def remove_digits_from_file(input_file, output_file):
    """
    Удаляет все цифры из текста в файле и записывает результат в новый файл.

    Args:
        input_file (str): Путь к входному файлу, содержащему текст с цифрами.
        output_file (str): Путь к выходному файлу, в который будет записан текст без цифр.

    """
    # Открываем исходный файл для чтения
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Удаляем все цифры из текста
    cleaned_text = ''.join(char for char in text if not char.isdigit())

    # Записываем очищенный текст в новый файл
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')