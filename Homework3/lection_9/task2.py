# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчанию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.



import datetime


# Здесь пишем код

def func_log(file_log):
    """
    Декоратор, который записывает имя вызываемой функции, дату и время вызова в указанный файл.

    :param file_log (str): Путь до файла для записи логов.
    :return: function: Обернутая функция с логированием.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(file_log, 'a', encoding='utf-8') as log_file:
                log_file.write(f"{func.__name__} вызвана {datetime.datetime.now().strftime('%d.%m %H:%M:%S')}\n")
            return func(*args, **kwargs)

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper

    return decorator

# Пример использования декоратора
@func_log(file_log='func1.txt')
def func1():
    """Функция func1, которая делает паузу на 3 секунды."""
    import time
    time.sleep(3)

@func_log(file_log='func2.txt')
def func2():
    """Функция func2, которая делает паузу на 5 секунд."""
    import time
    time.sleep(5)

# Вызов функций для демонстрации логирования
func1()
func2()
func1()

# Проверка документации функции
help(func1)
