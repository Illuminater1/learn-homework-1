"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""


def main(str1, str2):
    if type(str1) != str or type(str2) != str:
        return 0
    elif str1 == str2:
        return 1
    elif  str1 != str2 and str2 == "learn":
        return 3
    elif len(str1) > len(str2):
        return 2
    else:
        return "hz"


if __name__ == "__main__":
    print(main("qwerty", 1))
    print(main(1, "qwerty"))
    print(main("qwerty", "qwerty"))
    print(main("qwerty", "qwer"))
    print(main("qwerty", "learn"))
    print(main("qwer", "qwerty"))

