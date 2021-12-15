def get_field():
    pass

def checker(coords: tuple):
    if coords[0] not in range(10) or coords[1] not in range(10):
        print("You have not entered the allowed coordinates. Try again")
        return False
    return True

def print_field(field_player1: list, field_shoots: set):
    print('My field:')
    for line in field_player1:
        for poss in line:
            print(poss, end=' ')
        print()

    lst = [["_"]*10 for i in range(10)]
    print('Shoots field:')
    for move in field_shoots: 
        lst[move[1]][move[0]] = '*'
    
    for line in lst:
        for poss in line:
            print(poss, end=' ')
        print()

def near_ships(field: list, shot: tuple):
    horiz = shot[0]
    vert = shot[1]
    allow_vert = [field[i][horiz] for i in range(10)]
    allow_horiz = [field[vert][i] for i in range(10)]
    return bool(allow_horiz.count("O") + allow_vert.count("O"))
    

def checking_bullseye(field_enemy: list, field_shots: set, shot: tuple):
    horiz = shot[0]
    vert = shot[1]
    mark = field_enemy[vert][horiz]
    copy_shots = field_shots
    field_shots = copy_shots | set(shot)
    if len(field_shots) == len(copy_shots):
        print("You have shot the same square! Not nice")
    if mark == "O" or mark == "X":
        field_enemy[vert][horiz] = "_"
        if near_ships(field_enemy, shot):
            print("There are other ships on these lines")
        else:
            print("The ship was completly detroyed")
        quantity = 0
        for row in field_enemy:
            for elem in row:
                if elem in ("O", "X"):
                    quantity += 1
        if quantity == 0:
            print("WIN!")
            return None, None
    else:
        print("You didn't hit the target. Better luck next time")
    return field_enemy, field_shots


def make_move():
    move = input().split()
    return tuple(map(int, move))


def step():
    i = 0
    field_1 = get_field()
    field_2 = get_field()
    shots1 = set()
    shots2 = set()
    while True:
        if not i % 2:
            print_field(field_1, shots1)
            move = make_move # player1
            field_2, shots1 = checking_bullseye(field_2, shots1, move)
        else:
            print_field(field_2, shots2)
            move = make_move # player2
            field1, shots2 = checking_bullseye(field_1, shots2, move)
        i += 1
        if field_2 == None or field_1 == None:
            break
