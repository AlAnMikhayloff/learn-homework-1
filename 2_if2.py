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

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def lines(line_one, line_two):
        if type(line_one) != str or type(line_two) != str:
            print(0)
        elif line_one == line_two:
            print(1)
        elif len(str(line_one)) > len(str(line_two)):
            print(2)
        elif line_one != line_two and line_two == 'learn':
            print(3)
        else:
            print('А вторая-то строка длиннее!')
    lines(2, 'hello')
    lines('help', 'help')
    lines('learn1', 'learn')
    lines('learn1', 'learn34')
    
if __name__ == "__main__":
    main()
