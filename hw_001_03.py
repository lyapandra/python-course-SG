# Стрічки

# Заповнити код приведених нижче функцій. Функція main() вже
# налаштована для виклику функцій з декількома різними
# параметрами, і виводить 'OK' у випадку, якщо виклик функції
# коректний.
# Початковий код кожної функції містить 'return'
# і є просто заготовкою для вашого коду.


# A. Пончики
# Дано кількість пончиків (ціле число);
# Потрібно повернути стрічку наступного виду:
# 'Кількість пончиків: <count>', де <count> ця кількість,
# яка передана в функцію як параметр.
# Проте, якщо кількість 10 і більше - поьрібно використовувати слово
# 'багато', замість поточної кількості.
# Таким чином, donuts(5) поверне 'Кількість пончиків: 5'
# а donuts(23) - 'Кількість пончиків: багато'
def donuts(count):
    # +++ ваш код +++
    return


# B. Обидва кінці
# Дано стрічка s.
# Поверніть стрічку, яка складається з перших 2
# і останніх 2 символів початкової стрічки.
# Таким чином, з стрічки 'spring' отримається 'spng'.
# Проте, якщо довжина стрічки менше, ніж 2 -
# поверніть просто пусту стрічку.
def both_ends(s):
    # +++ ваш код +++
    return


# C. Крім першого
# Дано стрічка s.
# Поверніть стріку, в якій всі входження її першого символу
# замінені на '*', за винятком самого цього першого символу.
# Тобто, з 'babble' отримається 'ba**le'.
# Передбачається, що довжина стрічки 1 і більше.
# Підказка: s.replace(stra, strb) поверне версію стрічки,
# в якій всі входження stra будуть замінені на strb.
def fix_start(s):
    # +++ ваш код +++
    return


# D. Перемішування
# Дано стрічки a і b.
# Поверніть одну стрічку, в якій a і b відокремлені прогалиною '<a> <b>',
# і поміняйте місцями перші 2 символи кожної стрічки.
# Тобто:
#   'mix', 'pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Передбачається, що стрічки a і b мають довжину 2 і більше символів.
def mix_up(a, b):
    # +++ ваш код +++
    return


# E. Хороша
# Дана стрічка.
# Знайдіть першее входження підстрічок 'не' і 'погана'.
# Якщо 'погана' йде після 'не' - замініть всю підстрічку
# 'не'...'погана' на 'хороша'.
# Поверніть отриману стрічку
# Тобто, 'Ця вечеря не така вже й погана!' поверне:
# Ця вечеря хороша!
def not_bad(s):
    # +++ ваш код +++
    return


# F. Дві половини
# Розглянемо поділ стрічки на дві половини.
# Якщо довжина парна - обидві половини мають однакову довжину.
# Якщо довжина непарна — додатковий символ приєднується до першої половини.
# Тобто, 'abcde', перша половина 'abc', друга - 'de'.
# Дано 2 стрічки, a і b, поверніть стрічку виду:
# 1-половина-a + 1-половина-b + 2-половина-a + 2-половина-b
def front_back(a, b):
    # +++ ваш код +++
    return



# Проста функція test() використовується в main() для виведення
# порівняння того, що повертається з функції з тим, що вона повинна повертати.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Отримано: %s | Очікувалося: %s' % (prefix, repr(got), repr(expected)))


# Викликає фунції вище з тестовими параметрами.
def main():
    print('Пончики')
    # Кожна стрічка ввикликає donuts() і порівнює повернене значення з очікуваним.
    test(donuts(4), u'Кількість пончиків: 4')
    test(donuts(9), 'Кількість пончиків: 9')
    test(donuts(10), 'Кількість пончиків: багато')
    test(donuts(99), 'Кількість пончиків: багато')

    print()
    print('Обидва кінці')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print()
    print('Крім першого')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print('Перемішування')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')

    print()
    print('Хороша')
    test(not_bad('Ця картина не така вже погана'), 'Ця картина хороша')
    test(not_bad('А вечеря була не погана!'), 'А вечеря була хороша!')
    test(not_bad('Ця кава вже не гаряча'), 'Ця кава вже не гаряча')
    test(not_bad("Ця погана, але не зовсім"), "Ця погана, але не зовсім")

    print()
    print('Дві половини')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


# Стандартний шаблон для виклику функції main().
if __name__ == '__main__':
    main()
