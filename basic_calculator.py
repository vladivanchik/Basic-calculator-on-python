ask1 = input("Привіт! Якщо ти хочеш вичислювати цілі числа то впиши \"Цілі числа\",якщо же ти хочеш використовувати  дії з дробовоми числами, то впиши \"Дробові числа\" ")
if ask1 == "Дробові числа":
    number1 = float(input("Введіть число: "))
    number2 = float(input("Введіть інше число: "))
    action = input("Введіть дію з числом : ")
if ask1 == "Цілі числа":
    number1 = int(input("Введіть число: "))
    number2 = int(input("Введіть інше число: "))
    action = input("Введіть дію з числом : ")
if action == "*":
    print(number1 * number2)
if action == "/":
    print(number1 / number2)
if action == "+":
    print(number1 + number2)
if action == "-":
    print(number1 - number2)


