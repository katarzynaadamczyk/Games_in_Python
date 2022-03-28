''' functions to implement on a lab in python essentials course by cisco '''

from random import randrange


def display_board(board):
    # Funkcja, ktora przyjmuje jeden parametr zawierajacy biezacy stan tablicy
    # i wyswietla go w oknie konsoli.
    for row in board:
        print('+-------+-------+-------+')
        print()
        print('|       |       |       |')
        print()
        print('|', end='')
        for sign in row:
            print('   ', end='')
            print(sign, end='')
            print('   |', end='')
        print()
        print()
        print('|       |       |       |')
        print()
    print('+-------+-------+-------+')

def make_list_of_free_fields(board):
    # Funkcja, ktora przeglada tablice i tworzy liste wszystkich wolnych pol; 
    # lista sklada sie z krotek, a kazda krotka zawiera pare liczb odzwierciedlajacych rzad i kolumne.
    lst = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] != 'X' and board[y][x] != 'O': 
                lst.append((x, y))
    return lst

def enter_move(board):
    # Funkcja, ktora przyjmuje parametr odzwierciedlajacy biezacy stan tablicy,
    # prosi uzytkownika o wykonanie ruchu, 
    # sprawdza dane wejsciowe i aktualizuje tablice zgodnie z decyzja uzytkownika.
    while True:
        newopos = input('Wykonaj swój ruch: ')
        if newopos.isdecimal():
            newopos = int(newopos)
            lstfreefields = make_list_of_free_fields(board)
            for x, y in lstfreefields:
                if board[y][x] == newopos:
                    board[y][x] = 'O'
                    return
        print('Podales bledne dane, spróbuj jeszcze raz.')



def victory_for(board, sign):
    # Funkcja, ktora dokonuje analizy stanu tablicy w celu sprawdzenia
    # czy uzytkownik/gracz stosujacy "O" lub "X" wygral rozgrywke.
    for row in board:
        won = True
        for char in board:
            if char != sign:
                won = False
                break
        if won:
            return True
    for x in range(len(board)):
        won = True
        for y in range(len(board)):
            if board[y][x] != sign:
                won = False
                break
        if won:
            return True
    won = True
    for x in range(len(board)):
        if board[x][x] != sign:
            won = False
            break
    if won:
        return True
    won = True
    for x in range(len(board)):
        if board[-1-x][x] != sign:
            won = False
            break
    if won:
        return True
    return False
    


def draw_move(board):
    # Funkcja, ktora wykonuje ruch za komputer i aktualizuje tablice.
    freefields = make_list_of_free_fields(board)
    newxpos = freefields[randrange(len(freefields))]
    board[newxpos[1]][newxpos[0]] = 'X'
    
def play_tictactoe():
    board = [
                [1, 2, 3],
                [4, 'X', 6],
                [7, 8, 9]
            ]
    while True:
        display_board(board)
        enter_move(board)
        if victory_for(board, 'O'):
            print('Wygrałeś!')
            break
        draw_move(board)
        if victory_for(board, 'X'):
            print('Wygrał komputer!')
            break


def main():
    play_tictactoe()


if __name__ == '__main__':
    main()
    