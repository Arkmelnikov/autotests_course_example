# Напишите функцию treatment_sum, использовав конструкцию try/except
# На вход поступает кортеж our_tuple

# Если в кортеже 2 элемента и их можно сложить,
# то функция возвращает получившийся результат

# Если в кортеже 2 элемента и их нельзя сложить,
# то функция обрабатывает исключение и возвращает строку 'Нельзя сложить эти данные'

# Если в кортеже меньше двух элементов,
# то функция обрабатывает исключение и возвращает строку 'Недостаточно данных'

# Если в кортеже больше двух элементов,
# то функция генерирует исключение Exception с текстом 'Много данных'


import unittest  # Не удалять


# Здесь пишем код


def treatment_sum(our_tuple):
    """
    Функция treatment_sum принимает кортеж our_tuple и возвращает сумму его элементов, если в кортеже ровно 2 элемента и их можно сложить.
    Если в кортеже меньше 2 элементов, функция возбуждает исключение и возвращает строку 'Недостаточно данных'.
    Если в кортеже больше 2 элементов, функция генерирует исключение Exception с текстом 'Много данных'.
    Если элементы кортежа не могут быть сложены (например, один из элементов - строка), функция возвращает 'Нельзя сложить эти данные'.

    Параметры:
    our_tuple (tuple): Кортеж, элементы которого будут складываться.

    Возвращает:
    int or str: Сумма элементов кортежа или сообщение об ошибке.
    """
    try:
        if len(our_tuple) == 2:
            if all(isinstance(item, (int, float)) for item in our_tuple):
                result = sum(our_tuple)
            elif all(isinstance(item, str) for item in our_tuple):
                result = ''.join(our_tuple)
            else:
                raise TypeError('Нельзя сложить эти данные')
            return result
        elif len(our_tuple) < 2:
            raise AssertionError('Недостаточно данных')
        else:
            raise Exception('Много данных')
    except TypeError as e:
        return str(e)
    except AssertionError as a:
        return str(a)


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


class MyTestCase(unittest.TestCase):

    def test(self):
        data = [(3, 5), (3, '7'), (3,), (), ('23', '32')]

        test_data = [8, 'Нельзя сложить эти данные', 'Недостаточно данных', 'Недостаточно данных', '2332']

        for i, d in enumerate(data):
            assert treatment_sum(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
            print(f'Тестовый набор {d} прошёл проверку')

        with self.assertRaises(Exception):
            treatment_sum((3, 4, 5))
        try:
            treatment_sum((3, 4, 5))
        except Exception as e:
            assert e.args[0] == 'Много данных', 'Исключение имеет неправильный текст'
        print('Всё ок')


if __name__ == '__main__':
    unittest.main()
