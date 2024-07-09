# Напишите класс PersonInfo
# Экземпляр класса создается из следующих атрибутов:
# 1. Строка - "Имя Фамилия"
# 2. Число - возраст сотрудника
# 3. Подразделения от головного до того, где работает сотрудник.
# Реализуйте методы класса:
# 1. short_name, который возвращает строку Фамилия И.
# 2. path_deps, возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
# 3. new_salary, Директор решил проиндексировать зарплаты, и новая зарплата теперь вычисляет по формуле:
# 1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
# (регистр имеет значение "А" и "а" - разные буквы)
# Например (Ввод --> Вывод) :
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').short_name() --> 'Шленский А.'
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').path_deps() -->
#            'Разработка --> УК --> Автотесты'
# PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты').new_salary() --> 385056 т.к.
# т.к. буква "т" встречается 4 раза, "а" 3 раза, 'о' 2 раза, остальные по одной. Сумма трёх самых частых букв 4+3+2 = 9.
# 1337*32*9 = 385056

# Здесь пишем код

class PersonInfo:
    """
    Класс для хранения информации о человеке и выполнения операций с этой информацией.
    """

    def __init__(self, full_name, age, *departments):
        """
        Инициализирует объект PersonInfo.

        Аргументы:
        full_name (str): Полное имя человека.
        age (int): Возраст человека.
        *departments (str): Переменное количество строк с названиями отделов.

        Пример использования:
        person = PersonInfo('Иван Иванов', 30, 'Отдел разработки', 'Отдел тестирования')
        """
        self.full_name = full_name
        self.age = age
        self.departments = departments

    def short_name(self):
        """
        Возвращает короткое представление имени в формате "Фамилия И.".

        Возвращает:
        str: Короткое представление имени.

        Пример использования:
        short_name = person.short_name()
        """
        first_name, last_name = self.full_name.split()
        return f"{last_name} {first_name[0]}."

    def path_deps(self):
        """
        Возвращает строку, представляющую путь отделов через знак" --> ".

        Возвращает:
        str: Строка с путем отделов.

        Пример использования:
        path = person.path_deps()
        """
        return ' --> '.join(self.departments)

    def new_salary(self):
        """
        Вычисляет новую зарплату на основе количества букв в названиях отделов.

        Возвращает:
        int: Новая зарплата.

        Пример использования:
        salary = person.new_salary()
        """
        letter_counts = {}
        for dep in self.departments:
            for char in dep:
                if char in letter_counts:
                    letter_counts[char] += 1
                else:
                    letter_counts[char] = 1
        sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
        total_count = sum(count for letter, count in sorted_letter_counts[:3])
        return 1337 * self.age * total_count


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


first_person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
fourth_person = PersonInfo('Иван Иванов', 26, 'Разработка')
second_person = PersonInfo('Пётр Валерьев', 47, 'Разработка', 'УК')
third_person = PersonInfo('Макар Артуров', 51, 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование')

data = [first_person.short_name,
        second_person.short_name,
        third_person.short_name,
        fourth_person.short_name,

        first_person.path_deps,
        second_person.path_deps,
        third_person.path_deps,
        fourth_person.path_deps,

        first_person.new_salary,
        second_person.new_salary,
        third_person.new_salary,
        fourth_person.new_salary
        ]

test_data = ['Шленский А.', 'Валерьев П.', 'Артуров М.', 'Иванов И.',

             'Разработка --> УК --> Автотесты',
             'Разработка --> УК',
             'Разработка --> УК --> Нефункциональное тестирование --> Автотестирование',
             'Разработка',
             385056, 314195, 1227366, 173810]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
