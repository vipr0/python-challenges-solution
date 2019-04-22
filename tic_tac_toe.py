'''
A console version of a Tic-Tac-Toe game written on Pyton
'''
# Graphical elements
void = '   '
x = ' x '
o = ' o '
canvas = [void] * 9 # starting canvas
player_number = 0
win = False # if true then game ends

def check_win():
    '''
    Check if player win.
    If at least one of rows, cols or diagonals is completely filled
    by one player the game is over
    '''
    global win
    rows = [canvas[:3], canvas[3:6], canvas[6:]]
    cols = [canvas[i::3] for i in range(3)]
    diagonals = [canvas[::4], canvas[2:8:2]]

    for array in [rows, cols, diagonals]:
        for row in array:
            if len(set(row)) == 1 and not void in set(row):
                win = True

def print_canvas():
    '''
    Prints canvas
    '''
    print('\n' * 100)
    print(' 1 | 2 | 3 ' + '       ' + '|'.join(canvas[:3]))
    print(' 4 | 5 | 6 ' + '       ' + '|'.join(canvas[3:6]))
    print(' 7 | 8 | 9 ' + '       ' + '|'.join(canvas[6:]))

def change_canvas(move):
    '''
    Fill the cell in canvas by players marker.
    Input : number of cell to fill
    '''
    while canvas[move - 1] != void:
        move = int(input(f'This cell is not empty, please select another cell: \n'))

    if player_number == 1:
        canvas[move - 1] = o
    else:
        canvas[move - 1] = x

while True:
    try:
        move = int(input(f'Player`s #{player_number + 1} move. Select your cell: \n'))

        if move not in range(1, 10):
            raise ValueError
    
    except ValueError:
        print('Please enter number from 1 to 9!!! \n')
        continue
    
    else:
        change_canvas(move)
        print_canvas()
        check_win()

        # if win is True then someone win
        if win:
            print(f'Player #{player_number + 1} win')
            break

        # check if we have free cells
        if void not in canvas:
            print('No more moves!')
            break

        # change player
        player_number = abs(player_number - 1)
