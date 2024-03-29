# -*- coding: utf-8 -*-
# --- самая верхняя строка для того,
# --- чтобы русские буквы читались правильно

# --- Встречая знак # в тексте программы на питоне, помни:
# --- Все, что начинается со значка # - это комментарий программиста
# --- и Python такие строки не рассматривает
# --- Многострочные комментарии достаточно заключить между 3-х кавычек
# --- одинарных или двойных, и весь текст между ними благополучно
# --- превратилтся в комментарий

"""
Например:
Тут тоже разместился комментарий и питон это пропускает
"""

'''
Или вот так, например:
Тут тоже разместился комментарий и питон это пропускает
'''

import sys
import math

def techinfo():
    print("__________________________")
    print("Сведения о платформе:")
    print(sys.version_info)
    print("version: ", sys.version)
    print("__________________________\n")

def selfdoc():
    print(
        ''' 
           ======================================================           
           Демонстрационная программа сумматор списка чисел
           Для этого списка чисел от 0 до 99 включительно
           найдем суммы: сначала этих чисел, а потом их квадратов
           Сами числа для списка получим с помощью цикла
           а потом произведем суммирование и печать результатов

           def selfdoc():       функция самодокументирования 
           def hi():            функция приветствия
           def CalcSumNumbers(A): Функ суммирования списка A
           def working():       Функция, где вся работа
           def main():          Основная функция программы
           ======================================================
                Программа представлена как пример структурирования
                и не предполагает, что начинающий Pythoner знает
                все, что тут написано, но стремится знать! 
           ======================================================
        '''
    )

# --- Функция приветствует с началом работы
# --- Желательно применять такое в своих программах
# --- "Привет!" и информация об авторе
def About():
    print(
    """
    Привет!
    ______________________________

    author: Anna Starmark
            class  8
            school 242
    e-mail: nn.starmark@gmail.com
    github: github.com/AnnaStarmark
    ______________________________
    """
    )

# --- Итеративная функция
# --- возвращает сумму чисел во входящем наборе
def CalcSumNumbers(A):
    if A == []:
        # если набор пуст, возвратить 0
        return 0
    else:
        # --- Пусть сначала
        summ = 0
        # --- Каждый элемент из списке A прибавляем к summ
        for elem in A:
            summ += elem
        # --- и вернем результат работы в вызывавшую функцию
        return summ


# --- Обычно в основную программу main() вписывают вызовы
# --- тех частей, которые лучше оформить в виде функций
# --- Вот например это будет наша первая функция-демонстратор
# --- работы арифметических функций-примеров
def working():
    # --- с помощью генератора списка []
    # --- для
    n = 100

    # --- Создаем 100 чисел от 0 до 99 включительно
    lst_arg0 = [x for x in range(0, n)]
    # --- Можно вывести к примеру первые 12 чисел ряда
    print("Вывод 12-ти целых чисел ряда от начала списка")
    for el in lst_arg0[:12]:
        print(el, end=' ')
    print("...")

    # --- Создаем 100 квадратов чисел от 0 до 99 включительно
    lst_arg1 = [x ** 2 for x in range(0, n)]
    # --- Можно вывести первые 12 квадратов чисел ряда
    print("Вывод 12-ти квадратов целых чисел ряда от начала списка")
    for el in lst_arg1[:12]:
        print(el, end=' ')
    print("...\n")

    # --- и затем
    # --- подставляем полученные списки со 100 аргументами
    # --- в функцию вычисления суммы этих чисел:
    # --- в CalcSumNumbers(list)
    # --- и полученные результаты работы функции
    # --- помещаем в переменную result
    # --- и после распечатываем
    result = CalcSumNumbers(lst_arg0)
    print("Сумма целых от 0 до 99 включительно  result = ", result)

    # --- А можно и короче записать, вот так:
    print("Сумма квадратов целых от 0 до 99   resultat = ", CalcSumNumbers(lst_arg1))

    print("\nКонец работы функции working\n")


def datastream():
    for el in [100*math.sin(16*math.pi*x/180) for x in range(0,360)]:
        print(el)

# --- main() - Это главная функция программы,
# --- в которой могут быть встроены разные
# --- другие функции, необходимые для решения задачи.
# --- В нашем случае этот пример показывает практику
# --- применения вложенных вункций для обеспечения наглядности
# --- всех зависимостей и чистоты кода для лучшего чтения.
def main():
    datastream()# --- Вывели график в цикле для опыта
    About()     # --- поприветствовали
    selfdoc()   # --- Описание программы
    techinfo()  # --- Версия питона
    working()   # --- поработали
    
    # --- правда, просто и красиво !?
    print("End program\n")


# --- И вот еще:
# --- При оформлении программы, которая в дальнейшем будет
# --- расширяться, ее надо отличить от библиотеки вот так:
if __name__ == "__main__":
    # --- Собственно сдесь и происходит вызов программы
    # --- которую выше обозначили как main()
    main()
