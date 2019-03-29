# Graphical elements
void = '   '
x   =  ' x '
o   =  ' o '
canvas = [void] * 9 # starting canvas
player_number = 0
win = False # if true then game ends

def check_win():
    global win
    rows = [canvas[:3], canvas[3:6], canvas[6:]]
    cols = [canvas[i::3] for i in range(3)]
    diagonals = [canvas[::4], canvas[2:8:2]]
    
    for array in [rows, cols, diagonals]:
        for row in array:
            if len(set(row)) == 1 and not void in set(row):
                win = True

def print_canvas():
    print('\n' * 100)
    print(' 1 | 2 | 3 ' + '       ' + '|'.join(canvas[:3]))
    print(' 4 | 5 | 6 ' + '       ' + '|'.join(canvas[3:6]))
    print(' 7 | 8 | 9 ' + '       ' + '|'.join(canvas[6:]))

def change_canvas(move):
    global canvas
    
    while canvas[move - 1] != void:
        move = int(input(f'This cell is not empty, please select another cell: \n'))
    
    if player_number == 1:
        canvas[move - 1] = o
    else:
        canvas[move - 1] = x

while True:
    move = int(input(f'Player`s #{player_number + 1} move. Select your cell: \n'))
    
    if not move in range(1, 10):
        print('Print correct number')
        continue
    
    change_canvas(move)
    print_canvas()
    check_win()
    
    # if win is True then someone win
    if win:
        print(f'Player #{player_number + 1} win')
        break
    
    # check if we have free cells
    if not void in canvas:
        print('No more moves!')
        break
    
    # change player
    player_number = abs(player_number - 1)