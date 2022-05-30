MILK = 500/6
FLOUR = 1000/6
BUTTER = 200/6
SUGAR = 300/6
RAISIN = 275/6
YEAST = 12/6
man_name = input('Привет, как тебя зовут')
print(man_name, 'Сейчас мы будем печь куличи')
egg = int(input('Сколько у тебя есть яиц ?'))
milk = egg*MILK
flour = egg*FLOUR
butter = egg*BUTTER
sugar = egg*SUGAR
raisin = egg*RAISIN
yeast = egg*YEAST
print('Тебе понадобиться на это количество яиц''\nмолоко- мл', milk, '\nмука -гр', flour, '\nмасло сливочное -гр', butter, )
print('сахар -гр', sugar, '\nизюм -гр', raisin, '\nдрожжи сухие -гр', yeast, '\nПриятного аппетита')
