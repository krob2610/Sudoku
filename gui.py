# pylint: disable=no-member
"""Interfejs Graficzny dla użytkownika:
uzywamy game_state do określenia w którym etapie gry jesteśmy
1 - początek: uzytkownik wciska jakiś przycisk ktory zeby zaczac
2 - wybór trudności: bierzemy pozycje myszki i sprawdzamy na którym jest przycisku
3 - rysowanie siatki i wpisywanie liczb
4 - uzytkownik może wypełniać tablice: jesli zrobi cała to może wrócić do pkt. 2
(pos[0]//50,pos[1]//50) -  w ten sposob możemy ustalić w którym z kwadratów jesteśmy
Uwaga! - te wartości są na odwrót niż w naszej tabeli
-running określa czy program ma dalej działać
"""
import pygame
from creating_unique_board import generate_random_grid
from solving_algorithm import back_tracking_solver

pygame.init()
screen = pygame.display.set_mode((550,550))
pygame.display.set_caption("Sudoku")
icon = pygame.image.load('SudokuIcon.png')
pygame.display.set_icon(icon)
screen.fill((255,255,255))

number_font = pygame.font.SysFont('Comic Sans Ms', 35)
message_font = pygame.font.SysFont('Comic Sans Ms', 20)

def play_one_more():
    """funkcja która wyświetla się po zakończeniu gry
    i pyta czy użytkownik chce zagrać ponownie
    - Tworzymy przyciski 'TAK' oraz 'NIE' (NIE-wyjscie)"""
    playagain = message_font.render('PLAY AGAIN?', False, (0, 0, 0))
    screen.blit(playagain,(10,10))

    pygame.draw.rect(screen,(64, 255, 0),(200,10,60,30))        #TAK
    pygame.draw.rect(screen,(255, 0, 0),(300,10,60,30))       #NIE

    yes_button = message_font.render('YES', False, (0, 0, 0))
    screen.blit(yes_button,(210,10))

    no_button = message_font.render('NO', False, (0, 0, 0))
    screen.blit(no_button,(315,10))
    pygame.display.update()
    while True:
        for event_v2 in pygame.event.get():
            if event_v2.type == pygame.QUIT:
                return 1
            if event_v2.type == pygame.MOUSEBUTTONUP and event_v2.button == 1:
                pos_v2 = pygame.mouse.get_pos()
                if 200 <= pos_v2[0] <=260 and 10 <= pos_v2[1] <= 40:
                    return 2
                if 300 <= pos_v2[0] <=360 and 10 <= pos_v2[1] <= 40:
                    return 1

def start_game():
    """funkcja ladujaca obraz 'Start game' """
    startsplash = pygame.image.load("paint_start.png")
    screen.blit(startsplash,(0,0))
    pygame.display.update()

def select_diff():
    """funkcja do wybierania poziomu trudności
    -rysujemy i podpisujemy przyciski
    następni jesli uzytkownik kliknie w dane miejsce takie poziom jest wybierany"""
    screen.fill((255,255,255))
    select = number_font.render('Select Difficulty', False, (0, 0, 0))
    screen.blit(select,(150,100))

    pygame.draw.rect(screen,(64, 255, 0),(190,200,200,50))        #łatwy
    pygame.draw.rect(screen,(255, 191, 0),(190,300,200,50))       #średni
    pygame.draw.rect(screen,(255, 0, 0),(190,400,200,50))        #trudny

    easy = number_font.render('EASY', False, (0, 0, 0))
    screen.blit(easy,(245,200))
    normal = number_font.render('NORMAL', False, (0, 0, 0))
    screen.blit(normal,(215,300))
    hard = number_font.render('HARD', False, (0, 0, 0))
    screen.blit(hard,(245,400))

    pygame.display.update()

    while True:
        for event_v3 in pygame.event.get():
            if event_v3.type == pygame.QUIT:
                return 1
            if event_v3.type == pygame.MOUSEBUTTONUP and event_v3.button == 1:
                pos_v3 = pygame.mouse.get_pos()            #dostajemy pozycje myszki
                if 190 <= pos_v3[0] <=390 and 200 <= pos_v3[1] <= 250:
                    return 30
                if 190 <= pos_v3[0] <=390 and 300 <= pos_v3[1] <= 350:
                    return 40
                if 190 <= pos_v3[0] <=390 and 400 <= pos_v3[1] <= 450:
                    return 45

def draw_solved():
    """funkcja porównuje tablice wypełniona przez uzytkownika z
    tablica w pełni wypełnioną oraz rysuje rozwiazanie na ekranie
    (musi uzupełniać tablice uzytkowanika tak aby kolory sie zgadzały)"""
    for i in range(9):
        for j in range(9):
            if Y[i][j] != Y_Base[i][j]:
                Y_Base[i][j] = Y[i][j]
                pygame.draw.rect(screen,(255,255,255), ((j+1)*50+5, (i+1)*50+5, 50-10 , 50-10))
                value = number_font.render(str(Y_Base[i][j]), True, (191, 0, 255))
                screen.blit(value,((j+1)*50+15,(i+1)*50))
                pygame.display.update()

def enter_number(screen_v4, pos_v4, left_or_right):
    """funkcja do wpisywania wartości
    - 1 if sprawdza czy nie wyjsc z programu
    - 2 if sprawdza czy wybrana przez nas pozycja nie jest wyjściowa
    (tych nie możemy edytować - są to czarne liczby)
    - 3 if jeśli 2 razy klikniemy lewy przycisk
    wpisujemy jako ostateczna
    (czyli program sprawdza czy jest ona poprawna i jesli tak to modyfikuje tabele)
    - 4 if jeśli 2 razy klikniemy prawy przycisk dajemy swoja propozycje liczby"""
    i = pos_v4[1]
    j = pos_v4[0]
    while True:
        for event_v5 in pygame.event.get():
            if event_v5.type == pygame.QUIT:
                return
            if event_v5.type == pygame.KEYDOWN:
                if Y_Base[i-1][j-1] != 0:
                    return
                if event_v5.key-48 > 0 and event_v5.key-48 < 10 and left_or_right == 1:
                    if Y[i-1][j-1] == event_v5.key-48:
                        Y_Base[i-1][j-1] = event_v5.key-48
                        pygame.draw.rect(screen_v4, (255, 255, 255),
                                         (pos_v4[0] * 50 + 5, pos_v4[1] * 50 + 5, 50 - 10, 50 - 10))
                        value = number_font.render(str(event_v5.key-48), True, (0, 255, 64))
                        screen_v4.blit(value, (pos_v4[0] * 50 + 15, pos_v4[1] * 50))
                        pygame.display.update()

                elif event_v5.key-48 > 0 and event_v5.key-48 < 10 \
                        and left_or_right == 3:
                    pygame.draw.rect(screen_v4, (255, 255, 255),
                                     (pos_v4[0] * 50 + 5, pos_v4[1] * 50 + 5, 50 - 10 , 50 - 10))
                    value = number_font.render(str(event_v5.key-48), True, (255, 191, 0))
                    screen_v4.blit(value, (pos_v4[0] * 50 + 15, pos_v4[1] * 50))
                    pygame.display.update()
                return
def draw_grid():
    """funkcja to rysowania siatki SUDOKU
    -w ifie gruszbe linie dla kwadratow
    -nastepnie normalne linie
    -2 for wpisujemy dane do tablicy
    -ostatni enter to przycisk 'Solve' """
    screen.fill((255,255,255))
    for i in range(10):
        if i%3 == 0:
            pygame.draw.line(screen,(0,0,0), (50+50*i, 50), (50+50*i,500), 4)
            pygame.draw.line(screen,(0,0,0), (50, 50+50*i), (500,50+50*i), 4)
        pygame.draw.line(screen,(0,0,0), (50+50*i, 50), (50+50*i,500), 2)
        pygame.draw.line(screen,(0,0,0), (50, 50+50*i), (500,50+50*i), 2)
    pygame.display.update()

    for i in range (len(Y[0])):
        for j in range(len(Y[0])):
            if Y_Base[i][j] != 0:
                value = number_font.render(str(Y[i][j]), True, (0,0,0))
                screen.blit(value,((j+1)*50+15,(i+1)*50))

    pygame.draw.rect(screen,(64, 255, 0),(50,510,100,30))
    solve_button = message_font.render('SOLVE', False, (0, 0, 0))
    screen.blit(solve_button,(60,510))

    pygame.display.update()


GAME_STATE = 1
RUNNING = True
Y = [[0 for i in range(9)] for j in range(9)]
Y_Base = Y
while RUNNING:

    if GAME_STATE == 1:
        start_game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type == pygame.KEYDOWN:
                GAME_STATE +=1

    elif GAME_STATE == 2:
        LEVEL = select_diff()
        if LEVEL == 1:
            RUNNING = False
        Y=generate_random_grid(LEVEL)
        Y_Base = [r[:] for r in Y]
        back_tracking_solver(Y)
        GAME_STATE +=1

    elif GAME_STATE == 3:
        draw_grid()
        GAME_STATE+=1

    elif GAME_STATE == 4:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and (event.button == 1 or event.button == 3):
                pos = pygame.mouse.get_pos()
                if 50 <= pos[0] <=499 and 50 <= pos[1] <= 499:
                    enter_number(screen, (pos[0]//50,pos[1]//50), event.button )
                    if Y == Y_Base:
                        WHAT_NEXT = play_one_more()
                        if WHAT_NEXT == 2:
                            GAME_STATE = 2
                        else:
                            RUNNING = False
                if 50<=pos[0]<=150 and 510 <= pos[1] <= 540:
                    draw_solved()
                    WHAT_NEXT = play_one_more()
                    if WHAT_NEXT == 2:
                        GAME_STATE = 2
                    else:
                        RUNNING = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
