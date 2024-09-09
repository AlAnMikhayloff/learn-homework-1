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

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    products = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

    n_1 = len(products[0]['items_sold'])
    total_sales_1 = 0
    for i in range(n_1):
        total_sales_1 = total_sales_1 + products[0]['items_sold'][i]
    print(f'Продано {products[0]['product']} всего: {total_sales_1} штук.')

    n_2 = len(products[1]['items_sold'])
    total_sales_2 = 0
    for i in range(n_2):
        total_sales_2 = total_sales_2 + products[1]['items_sold'][i]
    print(f'Продано {products[1]['product']} всего: {total_sales_2} штук.')
    
    n_3 = len(products[0]['items_sold'])
    total_sales_3 = 0
    for i in range(n_3):
        total_sales_3 = total_sales_3 + products[2]['items_sold'][i]
    print(f'Продано {products[2]['product']} всего: {total_sales_3} штук.')

    mean_sales_1 = total_sales_1 / n_1
    mean_sales_2 = total_sales_2 / n_2
    mean_sales_3 = total_sales_3 / n_3
    print(f'Среднее количество продаж {products[0]['product']}: {int(mean_sales_1)} штук.')
    print(f'Среднее количество продаж {products[1]['product']}: {int(mean_sales_2)} штук.')
    print(f'Среднее количество продаж {products[2]['product']}: {int(mean_sales_3)} штук.')

    total_sales = total_sales_1 + total_sales_2 + total_sales_3
    print(f'Суммарное количество продаж: {total_sales} штук.')

    mean_sales = (mean_sales_1 + mean_sales_2 + mean_sales_3) / len(products)
    print(f'Среднее количество продаж всех товаров: {mean_sales} штук.')



if __name__ == "__main__":
    main()
