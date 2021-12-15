def get_field():
    pass

def print_field():
    pass

def analyse_field():
    pass

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
        is_ship = False
        for i in range(5):
            if field_enemy[vert - 2 + i][horiz] in ("O", "X"):
                is_ship = True
            if field_enemy[vert][horiz - 2 + i] in ("O", "X"):
                is_ship = True
        if is_ship:
            print("The ship was damaged")
        else:
            print("The ship was completly detroyed")
        quantity = 0
        for row in field_enemy:
            for elem in row:
                if elem in ("O", "X"):
                    quantity += 1
        if quantity == 0:
            print("WIN!")
            return None
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
            move = make_move # player1
            field2, shots1 = checking_bullseye(field_enemy, field_shots, move)
        else:
            move = make_move # player2
            field1, shots2 = checking_bullseye(field_enemy, field_shots, move)
        i += 1
        if field2 == None or field1 == None:
            break
