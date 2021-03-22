"""moduł służacy do tworzenia nowej UNIKALNEJ planszy sudoku
oznacza to że ma ona tylko jedno rozwiazanie"""
import random
from solving_algorithm import find_spot_to_fill, is_okay, back_tracking_solver


def generate_random_grid(lvl):
    """algorytm do tworzenia losowego sudoku do rozwiazania
    -w 1 forze wpisujemy w kilku losowych miejsc na planszy losowe liczby z zakresu 1-9
    -w warunku while sprawdzamy czy wylosowana liczba może stać w danym miejscu
    -następnie rozwiązujemy sudoku
    -w 2 whilu będziemy usuwać liczby z losowych pozycji z sudoku
    (liczbe pozostałych liczb określa lvl)
    tak aby po każdym usunięciu sudoku miało jedno rozwiązanie
    (to wyznaczone przez back_tracking_solver)
    jesli nie ma to szukamy na innej pozycji
    """
    grid = [[0 for i in range(9)] for j in range(9)]
    for _ in range(10):
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1,10)
        while(not is_okay(grid,num, (row,col)) or grid[row][col] != 0):
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1,10)
        grid[row][col]= num
    back_tracking_solver(grid)

    while count_zero(grid) <lvl:
        row = random.randrange(9)
        col = random.randrange(9)
        while grid[row][col] == 0:
            row = random.randrange(9)
            col = random.randrange(9)
        backup = grid[row][col]
        grid[row][col]=0
        grid_copy = [r[:] for r in grid]      # kopia
        counter = 0
        counter = backtracking_more_then_one_solution(grid_copy,counter)
        if counter==2:
            grid[row][col] = backup
    return grid


def backtracking_more_then_one_solution(board,counter):
    """funkcja sprawdzajaca czy sudoku ma wiecej niż 1 rozwiazanie
    -jesli sa 2 rozwiazania to przerywamy działanie (1 if)
    -sprawdzamy czy funcka ma rozwiazania(2 if)
    -for to normalny algorytm uzpełniania chyba że następna pozycja jest ostatnia"""
    if counter == 2:
        return counter
    spot = find_spot_to_fill(board)
    if not spot:
        return True
    for i in range(9):
        if is_okay(board, i + 1, spot):
            board[spot[0]][spot[1]] = i + 1
            last = find_spot_to_fill(board)
            if not last:
                counter+=1
                break
            if backtracking_more_then_one_solution(board,counter):
                return True

        board[spot[0]][spot[1]]=0
    return False

def count_zero(board):
    """funkcja do zliczania zer w na planszy"""
    zero = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                zero +=1
    return zero

#UNIT TEST
# numeber_of_zero = 40
# Y = generate_random_grid(numeber_of_zero)
# print_grid(Y)
# if count_zero(Y) == numeber_of_zero:
#     print("TRUE")
#
# numeber_of_zero = 30
# Y = generate_random_grid(numeber_of_zero)
# print_grid(Y)
# if count_zero(Y) == numeber_of_zero:
#     print("TRUE")
