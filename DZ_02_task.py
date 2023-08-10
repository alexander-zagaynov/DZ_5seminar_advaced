
#Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: \n
# имена str, ставка int, премия str с указанием процентов вида «10.25%». \n
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. \n
# Сумма рассчитывается как ставка умноженная на процент премии

names = ['Alexander', 'Sergei', 'Dmitriy']
rates = [44_000, 15_000, 34_000]
premiums = ['10.25%', '22.26%', '33.27%']

result_dict = {name : (rate * float(premium[:-1])/100) for name, rate, premium in zip(names, rates, premiums)}

print(result_dict)

