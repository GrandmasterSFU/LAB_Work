money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
free_month = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while True:
    delta = spend - salary
    if delta > money_capital:
        break
    free_month += 1
    money_capital -= delta
    spend *= 1.05
print("Количество месяцев, которое можно протянуть без долгов:", free_month)
