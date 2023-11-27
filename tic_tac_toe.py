def decor(func):
    def check(lst, x, y, value):  # проверка занятости поля
        a = 'Эта клетка занята !'
        if lst[x][y] == '-':
            return func(lst, x, y, value)
        else:
            print(a)
    return check

@decor
def change(lst, x, y, value):  # изменение значения ячейки
    if value % 2 == 0:
        lst[x][y] = 'x'
    else: lst[x][y] = 'o'
    return lst

def printer(lst):  # выводит поле в консоль
    for i in range(4):
        print(*lst[i])


def coordinates():  # запрашивает координаты желаемой ячейки
    dct={'x': 0, 'y': 0}
    place = 'x'
    while dct.get('x')==0 or dct.get('y')==0:

        if place == 'x':
            n=input('Введите строку : ')
        else:
            n=input('Введите столбец : ')

        if len(n)==1 and n.isdigit()==True:
            if int(n)<=3 :
                dct[place] = int(n)
                place = 'y'
            else: print('Неприемлемая координата')
        else: print('Неприемлемая координата')
    lst=[dct.get('x'), dct.get('y')]
    return lst

def winner(lst):  # определение победителя
    line = ''
    for i in range(1, 4):
        for j in range(1, 4):
            line += lst[i][j]
    valet = ''
    for i in range(0, len(line)-2, 3):
        if line[i]==line[i+1]==line[i+2]=='x' or line[i]==line[i+1]==line[i+2]=='o': # проверка линий горизонтальных
            valet=line[i]
    for i in range(len(line)-6):
        if line[i]==line[i+3]==line[i+6]=='x' or line[i]==line[i+3]==line[i+6]=='o':  # проверка линий вертикальных
            valet=line[i]
    i=0
    if line[i]==line[i+4]==line[i+8]=='x' or line[i]==line[i+4]==line[i+8]=='o':  # проверка диагоналей
        valet=line[i]
    i=2
    if line[i]==line[i+2]==line[i+4]=='x' or line[i]==line[i+2]==line[i+4]=='o':
        valet=line[i]
    return valet
def tic_tac_toe(player_1, player_2):  # основная функция игры
    field = [[' ', 1, 2, 3],  # само поле
        [1, '-', '-', '-'],
        [2, '-', '-', '-'],
        [3, '-', '-', '-']]

    if player_1=='' and player_2=='':
        player_1, player_2='первый игрок', 'второй игрок'

    cnt_steps = 0  # количество поставленных фигур
    val = '' # фигура победителя

    printer(field)  # показывает поле

    while val == '' and cnt_steps < 9: # сама игра
        x, y = 0, 0
        if cnt_steps%2 == 0:
            print('Ход первого игрока.')
        else:
            print('Ход второго игрока.')

        lst = coordinates()
        x, y = lst[0], lst[1]

        a = change(field, x, y, cnt_steps)
        type(a)

        if type(a)==list:
            field = a

            cnt_steps += 1
            if cnt_steps>=5:
                val = winner(field)

            printer(field)


    if val == 'x':  # Кто победил ?
        print(f'Победил {player_1}!')
    elif val == 'o':
        print(f'Победил {player_2}!')
    elif cnt_steps > 8:
        print('Ничья !')

    yes_or_no = input('Играем ещё ? (Да/Нет) ')
    if yes_or_no.lower() == 'да':
            tic_tac_toe(player_1, player_2)
    else: print('Спасибо за игру !')

print('Добро пожаловать в крестики нолики ! Первый игрок играет крестиками, второй - ноликами.')
answer = input('Хотите выбрать имена для игроков ? (Да/Нет) ')
player_1, player_2 = '', ''

if answer.lower() == 'да':
    player_1 = input('Введите имя первого игрока: ')  # имена игроков
    print(f'Первый игрок - {player_1}. Фигура - x.')
    player_2 = input('Введите имя второго игрока: ')
    print(f'Второй игрок - {player_2}. Фигура - o.')

tic_tac_toe(player_1, player_2)