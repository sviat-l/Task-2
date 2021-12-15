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
            if int(pos[1]) < 7 and int(pos[0]) < 10:
                pos = [int(element) for element in pos]
                return pos
            elif pos == "quit":
                return pos
    def current_list(field):
        number_of_boates = 0
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
        return field
    result = current_list(create_field())
    return result







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
        for i in range(3):
            if field_enemy[vert - 1 + i][horiz] in ("O", "X"):
                is_ship = True
            if field_enemy[vert][horiz - 1 + i] in ("O", "X"):
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
