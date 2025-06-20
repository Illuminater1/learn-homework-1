"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    phone_sales_sum = 0                 #всего телефонов продано
    phone_avg_sum = 0                   #в среднем телефонов продавалось

    for phone in phones:
        phones_sales = sum(phone['items_sold'])                            #телефонов одной марки продано всего
        avg_sales = round(phones_sales / (len(phone['items_sold'])), 2)    #продавалось в среднем
        phone_sales_sum += phones_sales
        phone_avg_sum += avg_sales

        print(f"Продано {phone['product']} - {phones_sales} шт. В среднем продавалось - {avg_sales} в месяц")
    print(f"Всего телефонов продано: {phone_sales_sum} шт")
    print(f"В среднем продавалось {phone_avg_sum} телефонов в месяц")


if __name__ == "__main__":
    main()
