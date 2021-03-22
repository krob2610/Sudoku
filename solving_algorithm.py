"""
Moduł zawierajacy funkcje do rozwiazywania sudoku oraz wypisywania
tablicy na ekran w w przypadku nie używania wersji GUI
"""
def print_grid(board):
    """Funkcja która wypisuje na ekran sudoku"""
    for i in range (9):
        if i%3 == 0:
            print("")
        for j in range(9):
            if j%3==0:
                print("  ", end="")
            if j!=8:
                print(str(board[i][j]) + " ", end="")
            else:
                print(board[i][j])

def find_spot_to_fill(board):
    """funkcja która znaleźć kolejne miejsce do wypełnienia"""
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return (i,j)
    return None

def is_okay(board, num, pos):
    """funkcja która sprawdza czy wpisany numer pasuje w dane miejsce
    -W pierwszym forze sprawdzamy czy w wierszu jest już licza taka sama którą my wybraliśmy
    -W 2 tak samo tylko dla kolumn
    -W 3 dla 'kwadratow' 3x3 (pos[0]//3 ma wartości 0,1 lub 2
    *3 daje nam początkowy index danego kwadratu a
    +3 ile razy musimy wykonać pętle od kolejnego indeksu) """
    for i in range(9):
        if board[pos[0]][i] ==num and pos[1] != i:
            return False

    for i in range(9):
        if board[i][pos[1]] ==num and pos[0] != i:
            return False

    for i in range((pos[0]//3) * 3,((pos[0]//3)*3) + 3):
        for j in range((pos[1]//3) * 3,((pos[1]//3)*3) + 3):
            if board[i][j]==num and pos!=(i, j):
                return False
    return True


def back_tracking_solver(board):
    """funkcja do rozwiązywania sudoku, wykorzystuje Backtracking
    -Sprawdzamy czy sudoku jest już rozwiazane
    -Sprawdzamy czy możemy dodać wybrana liczbę w tamto miejsce"""
    spot = find_spot_to_fill(board)
    if not spot:
        return True

    for i in range(9):
        if is_okay(board, i + 1, spot):
            board[spot[0]][spot[1]] = i + 1
            if back_tracking_solver(board):
                return True
            board[spot[0]][spot[1]]=0
    return False

#UNIT TEST
#testowanie czy poprawnie rozwiązuje
# X = [
#         [0, 0, 0, 2, 6, 0, 7, 0, 1],
#         [6, 8, 0, 0, 7, 0, 0, 9, 0],
#         [1, 9, 0, 0, 0, 4, 5, 0, 0],
#         [8, 2, 0, 1, 0, 0, 0, 4, 0],
#         [0, 0, 4, 6, 0, 2, 9, 0, 0],
#         [0, 5, 0, 0, 0, 3, 0, 2, 8],
#         [0, 0, 9, 3, 0, 0, 0, 7, 4],
#         [0, 4, 0, 0, 5, 0, 0, 3, 6],
#         [7, 0, 3, 0, 1, 8, 0, 0, 0]]
# back_tracking_solver(X)
# if X == [
#         [4, 3, 5, 2, 6, 9, 7, 8, 1],
#         [6, 8, 2, 5, 7, 1, 4, 9, 3],
#         [1, 9, 7, 8, 3, 4, 5, 6, 2],
#         [8, 2, 6, 1, 9, 5, 3, 4, 7],
#         [3, 7, 4, 6, 8, 2, 9, 1, 5],
#         [9, 5, 1, 7, 4, 3, 6, 2, 8],
#         [5, 1, 9, 3, 2, 6, 8, 7, 4],
#         [2, 4, 8, 9, 5, 7, 1, 3, 6],
#         [7, 6, 3, 4, 1, 8, 2, 5, 9] ] :
#     print("TRUE")
#
# Y = [
#         [0, 2, 0, 6, 0, 8, 0, 0, 0],
#         [5, 8, 0, 0, 0, 9, 7, 0, 0],
#         [0, 0, 0, 0, 4, 0, 0, 0, 0],
#         [3, 7, 0, 0, 0, 0, 5, 0, 0],
#         [6, 0, 0, 0, 0, 0, 0, 0, 4],
#         [0, 0, 8, 0, 0, 0, 0, 1, 3],
#         [0, 0, 0, 0, 2, 0, 0, 0, 0],
#         [0, 0, 9, 8, 0, 0, 0, 3, 6],
#         [0, 0, 0, 3, 0, 6, 0, 9, 0]
#     ]
# back_tracking_solver(Y)
# if Y == [
#         [1, 2, 3, 6, 7, 8, 9, 4, 5],
#         [5, 8, 4, 2, 3, 9, 7, 6, 1],
#         [9, 6, 7, 1, 4, 5, 3, 2, 8],
#         [3, 7, 2, 4, 6, 1, 5, 8, 9],
#         [6, 9, 1, 5, 8, 3, 2, 7, 4],
#         [4, 5, 8, 7, 9, 2, 6, 1, 3],
#         [8, 3, 6, 9, 2, 4, 1, 5, 7],
#         [2, 1, 9, 8, 5, 7, 4, 3, 6],
#         [7, 4, 5, 3, 1, 6, 8, 9, 2]]:
#
#     print("TRUE")
#
# #test wypisywanie
# print_grid(Y)
# print_grid(X)
#
# #szukanie kolejnego miejsca do wpisania
# if find_spot_to_fill([
#         [4, 3, 5, 2, 6, 9, 7, 8, 1],
#         [6, 8, 2, 5, 7, 1, 4, 9, 3],
#         [1, 9, 7, 8, 3, 4, 5, 6, 2],
#         [8, 2, 6, 1, 9, 5, 3, 4, 7],
#         [3, 7, 4, 6, 0, 2, 9, 1, 5],
#         [9, 5, 1, 7, 4, 3, 6, 2, 8],
#         [5, 1, 9, 3, 2, 6, 8, 7, 4],
#         [2, 4, 8, 9, 5, 7, 1, 3, 6],
#         [7, 6, 3, 4, 1, 8, 2, 5, 9] ]) == (4,4):
#     print("TRUE")
#
# if find_spot_to_fill([
#         [0, 3, 5, 2, 6, 9, 7, 8, 1],
#         [6, 0, 0, 5, 7, 1, 4, 9, 3],
#         [1, 9, 7, 8, 3, 4, 5, 6, 2],
#         [8, 0, 6, 1, 9, 5, 3, 4, 7],
#         [3, 7, 4, 6, 0, 2, 9, 1, 5],
#         [9, 5, 1, 7, 4, 3, 6, 2, 8],
#         [5, 1, 9, 3, 2, 6, 8, 0, 4],
#         [2, 4, 8, 9, 0, 7, 1, 3, 6],
#         [7, 0, 3, 4, 1, 8, 2, 5, 9] ]) == (0,0):
#     print("TRUE")
#
#
# if find_spot_to_fill([
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0]]) == (0,0):
#     print("TRUE")
#
# #czy jest okej
# if is_okay([
#         [4, 3, 5, 2, 6, 9, 7, 8, 1],
#         [6, 8, 2, 5, 7, 1, 4, 9, 3],
#         [1, 9, 7, 8, 3, 4, 5, 6, 2],
#         [8, 2, 6, 1, 9, 5, 3, 4, 7],
#         [3, 7, 4, 6, 0, 2, 9, 1, 5],
#         [9, 5, 1, 7, 4, 3, 6, 2, 8],
#         [5, 1, 9, 3, 2, 6, 8, 7, 4],
#         [2, 4, 8, 9, 5, 7, 1, 3, 6],
#         [7, 6, 3, 4, 1, 8, 2, 5, 9] ], 8, (4,4)):
#     print("TRUE")
#
#
#
# if is_okay([
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0]], 7, (0,0)):
#     print("TRUE")
#

#
#
#
# # X = [
# #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
# #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
# #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
# #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
# #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
# #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
# #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
# #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
# #         [0, 0, 0, 0, 0, 0, 0, 0, 0]
# #     ]
