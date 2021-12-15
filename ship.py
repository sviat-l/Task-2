def get_field():
    def create_field():
        field = [['_' for i in range(10)] for _ in range(10)]
        return field
    def pos_lodka():
        """
        You give start pos for your LODKA (довжина - 3 по горизонталі)
        """
        while True:
            print('Print coordinate: ')
            pos = list(map(str, input().split()))
            if int(pos[1]) <= 7 and int(pos[0]) < 10:
                pos = [int(element) for element in pos]
                return pos
            elif pos == "quit":
                return pos
    def current_list(field):
        number_of_boates = -1
        print('\t')
        column = 0
        print(end='  ')
        for elements in range(10):
            column += 1
            if column == 10:
                print('{0:^5}'.format(elements))
                break
            print('{0:^5}'.format(elements), end='')
        row = 0
        for elements in field:
            print(f'{row} {elements}')
            row += 1
        while number_of_boates <= 3:
            pos = pos_lodka()
            if pos == "quit":
                return  None
            else:
                for _ in range(3):
                    field[pos[0]][pos[1]+_] = 'O'
                number_of_boates += 1
                print('\t')
                column = 0
                print(end='  ')
                for elements in range(10):
                    column += 1
                    if column == 10:
                        print('{0:^5}'.format(elements))
                        break
                    print('{0:^5}'.format(elements), end='')
                row = 0
                for elements in field:
                    print(f'{row} {elements}')
                    row += 1
                number_of_boates += 1
        return field
    result = current_list(create_field())
    return result



def print_field(field_player1: list, field_shoots: set):
    print('My field:')
    for line in field_player1:
        for poss in line:
            print(poss, end=' ')
        print()

    lst = [["_"]*10 for i in range(10)]
    print('Shots field:')
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
    copy_shots = len(field_shots)
    field_shots.add(shot)
    if len(field_shots) == copy_shots:
        print("You have shot the same square! Not nice")
    if mark == "O":
        hit = True
        field_enemy[vert][horiz] = "X"
        print("You got it!")
        if near_ships(field_enemy, shot):
            print("There are other ships on these lines")
        else:
            print("The ship was completly detroyed")
        quantity = 0
        for row in field_enemy:
            for elem in row:
                if elem in ("O"):
                    quantity += 1
        if quantity == 0:
            print("WIN!")
            return None, None
    else:
        hit = False
        print("You didn't hit the target. Better luck next time")
    return field_enemy, field_shots, hit


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
        to_cont = False
        if not i % 2:
            print_field(field_1, shots1)
            move = make_move() # player1
            field_2, shots1, to_cont = checking_bullseye(field_2, shots1, move)
        else:
            print_field(field_2, shots2)
            move = make_move() # player2
            field1, shots2, to_cont = checking_bullseye(field_1, shots2, move)
        i += 1 if not to_cont else 2
        if field_2 == None or field_1 == None:
            break

if __name__ == "__main__":
    step()
