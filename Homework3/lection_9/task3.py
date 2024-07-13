# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

def find_three_most_expensive_purchases(file_path):
    """
    Читает файл с ценами товаров, разделяет покупки по пустым строкам,
    подсчитывает сумму каждой покупки и находит сумму трех самых дорогих покупок.

    Args:
        file_path (str): Путь к файлу с ценами товаров.

    Returns:
        int: Сумма трех самых дорогих покупок.
    """
    # Чтение файла и разделение на покупки
    with open(file_path, 'r') as file:
        data = file.read().strip().split('\n\n')

    # Подсчет суммы каждой покупки
    purchases = []
    for purchase in data:
        items = purchase.split()
        total = 0
        for item in items:
            total += int(item)
        purchases.append(total)

    # Нахождение трех самых дорогих покупок
    purchases.sort(reverse=True)
    three_most_expensive_purchases = sum(purchases[:3])

    return three_most_expensive_purchases

# Пример использования функции
file_path = 'test_file/task_3.txt'
three_most_expensive_purchases = find_three_most_expensive_purchases(file_path)
print(three_most_expensive_purchases)



assert three_most_expensive_purchases == 202346