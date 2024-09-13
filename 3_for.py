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
    
    total_sales_sum = 0
    mean_sales_sum = 0
    
    for j in range(len(products)):
        n = len(products[j]['items_sold'])
        total_sales = 0
        
        
        for i in range(n):
            total_sales = total_sales + products[j]['items_sold'][i]
            mean_sales = total_sales / n
                
        print(f'Продано {products[j]['product']} всего: {total_sales} штук.')
        print(f'Среднее количество продаж {products[j]['product']}: {int(mean_sales)} штук.')

        total_sales_sum = total_sales_sum + total_sales
        mean_sales_sum = mean_sales_sum + mean_sales
        mean_sales_all = mean_sales_sum  / int(len(products))
    

    print(f'Суммарное количество продаж: {total_sales_sum} штук.')
    print(f'Среднее количество продаж всех товаров: {mean_sales_all} штук.')

if __name__ == "__main__":
    main()
