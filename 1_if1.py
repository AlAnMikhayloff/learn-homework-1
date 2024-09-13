"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age_user = input('What is your age? ')
    age_user = int(age_user)
    if 0 < age_user <= 6:
        activity_user = "Do you really go to kindergarten?"
    if 7 < age_user <= 18:
        activity_user = "Wow! You're going to school!"
    if 19 < age_user <= 24:
        activity_user = "Wow! You're going to college!"
    else:
        activity_user = "I hope you're not unemployed?"
    print(activity_user)

if __name__ == "__main__":
    main()
