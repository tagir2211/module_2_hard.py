rock =int(input('Введите число то 3 до 20: '))

def rock_game(rock):
  lain = []
  #нати все множетели числа
  for i in range(3, rock + 1):
    if rock % i == 0:
      lain.append(i)
  #разложить множетели суммы натуральных чисел
  answer = ''
  for i in range(len(lain)):
    for j in range(lain[i]):
      for k in range(lain[i]):
        if j + k  == lain[i] and j != k and k > j:
          answer += str(j) + str(k)
  return(answer)
print('Правильный ответ:')
print(rock_game(rock))

answer = { 3 : 12,
  4 : 13,
  5 : 1423,
  6 : 121524,
  7 : 162534,
  8 : 13172635,
  9 : 1218273645,
  10 : 141923283746,
  11 : 11029384756,
  12 : 12131511124210394857,
  13 : 112211310495867,
  14 : 1611325212343114105968,
  15 : 1214114232133124115106978,
  16 : 1317115262143531341251161079,
  17 : 11621531441351261171089,
  18 : 12151811724272163631545414513612711810,
  19 : 118217316415514613712811910,
  20 : 13141911923282183731746416515614713812911}


print('Проверка:')
test = answer.get(rock)
test_str = str(test)
print(test_str)
if test_str == rock_game(rock):
  print('Все верно')
else:
  print('Прощай')