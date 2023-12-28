import pygame, sys
from pygame.locals import *
from time import sleep


ROWS = 3
COLS = 3

WIDTH = 200 * ROWS
HEIGHT = 200 * COLS

FPS = 60

BLACK = (0, 0, 0)


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT+30))
pygame.display.set_caption("Tick Tack Toe")
clock = pygame.time.Clock()

class Board:
    def __init__(self):
        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

        self.winner = ""

        # Check Turn 
        self.turn = "X"
        self.isPressed = False



        self.font = pygame.font.Font(None, 200)



    def draw_board(self):
        # rows and columns
        rect1 = pygame.Rect(0,200, WIDTH, 5)
        pygame.draw.rect(screen, BLACK, rect1)

        rect2 = pygame.Rect(0,400, WIDTH, 5)
        pygame.draw.rect(screen, BLACK, rect2)

        rect3 = pygame.Rect(200,0, 5, HEIGHT)
        pygame.draw.rect(screen, BLACK, rect3)

        rect4 = pygame.Rect(400,0, 5, HEIGHT)
        pygame.draw.rect(screen, BLACK, rect4)

        rect5 = pygame.Rect(0,600, WIDTH, 5)
        pygame.draw.rect(screen, BLACK, rect5)

        turn_font = pygame.font.Font(None, 24)
        turn_text = turn_font.render(f"Turn: {self.turn}", True, BLACK)
        turn_text_rect = turn_text.get_rect(bottomleft=(5,630))
        screen.blit(turn_text, turn_text_rect)

    def check_winner(self):
        # check horizontal
        for row in self.board:
            if row.count("X") == 3:
                self.winner = "X"

            if row.count("O") == 3:
                self.winner = "O"


        # check vertical
        flip_board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],

        ]
        for col_index, col in enumerate(self.board):
            for row_index, row in enumerate(col):
                flip_board[row_index][col_index] = row

        for row in flip_board:
            if row.count("X") == 3:
                self.winner = "X"
            if row.count("O") == 3:
                self.winner = "O"

        # check diagonal left
        x_left_diagonal_count = 0
        o_left_diagonal_count = 0
        for i in range(len(self.board)):
            if self.board[i][i] == "X":
                x_left_diagonal_count += 1
            if self.board[i][i] == "O":
                o_left_diagonal_count += 1


        if x_left_diagonal_count == 3:
            self.winner = "O"
        if o_left_diagonal_count == 3:
            self.winner = "O"

        # check diagonal right
        if self.board[0][2] == "X" and self.board[1][1] == "X" and self.board[2][0] == "X":
            self.winner = "X"
        if self.board[0][2] == "O" and self.board[1][1] == "O" and self.board[2][0] == "O":
            self.winner = "O"

        # check draw:



    def update(self):
        for col_index, col in enumerate(self.board):
            for row_index, row in enumerate(col):
                pos_x = int(WIDTH/COLS) * row_index
                pos_y = int(HEIGHT/ROWS) * col_index
                
                rect = pygame.Rect(pos_x, pos_y, 200, 200)
                pygame.draw.rect(screen, (255, 255, 255), rect)

                text = self.font.render(str(row), True, BLACK)
                text_rect = text.get_rect(center=rect.center)

                if rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[0]:
                        if self.board[col_index][row_index] == "":

                            if self.turn == "X":
                                text = self.board[col_index][row_index] = "X"
                                self.turn = "O"

                            elif self.turn == "O":
                                text = self.board[col_index][row_index] = "O"
                                self.turn = "X"


                            text = self.font.render(str(text), True, BLACK)
                            self.check_winner()



                screen.blit(text, text_rect)


def draw_winner(win):
    rect = pygame.Rect(0,0, WIDTH, HEIGHT+30)
    pygame.draw.rect(screen, (255, 255, 255), rect)

    font = pygame.font.Font(None, 60)
    text = font.render(f"WINNER: {win}", True, BLACK)
    text_rect = text.get_rect(center=rect.center)

    pos_x, pos_y = rect.center
    btn_play_again = pygame.Rect(pos_x-75, pos_x+50, 150, 50)
    pygame.draw.rect(screen, BLACK, btn_play_again)

    text_play_again = pygame.font.Font(None, 30).render("Play Again", True, (255, 255, 255))
    text_play_again_rect = text_play_again.get_rect(center=btn_play_again.center)

    if btn_play_again.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            play_again()


    screen.blit(text_play_again, text_play_again_rect)
    screen.blit(text, text_rect)

def play_again():
    board.board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ]
    board.flip_board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ]
    board.winner = ""
    board.turn = "X"
    sleep(0.1)
















board = Board()
while True:
    screen.fill('white')

    if board.winner == "":
        board.update()
        board.draw_board()
    else:
        draw_winner(board.winner)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(FPS)
    pygame.display.update()

