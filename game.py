print('Здравствуйте!')
print('Ваше игровое поле:')
game = [[" ", 0, 1, 2],
        [0, " ", " ", " "],
        [1, " ", " ", " "],
        [2, " ", " ", " "]
]
print('\n'.join('\t'.join(map(str, row)) for row in game))
while True:
    count = 1
    if count % 2 == 1:
        print('Ваш ход! Куда вы поставите крестик?')
        row = int(input("Введите номер строки: "))
        column = int(input("Введите номер столбца: "))
        game[row + 1][column + 1] = "x"
        print('Обновленное игровое поле:')
        print('\n'.join('\t'.join(map(str, row)) for row in game))
        count = count + 1
    if count % 2 == 0:
        print('Ваш ход! Куда вы поставите нолик?')
        row = int(input("Введите номер строки: "))
        column = int(input("Введите номер столбца: "))
        game[row + 1][column +1] = 0
        print('Обновленное игровое поле:')
        print('\n'.join('\t'.join(map(str, row)) for row in game))
        count = count + 1
