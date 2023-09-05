import pygame
import pygame_menu
from pygame_menu import Theme
from paddle import Paddle
from ball import Ball
from score import Score

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 600
FIELD = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
FPS = 60

paddle_width = 16
paddle_height = 100
player_paddle_height = 100
paddle_speed = 7
ball_size = 8
difficulty = "Normal"
default_option = None


def get_font(size):
    return pygame.font.Font(pygame.font.get_default_font(), size)


def set_difficulty(selected, value):
    global difficulty
    global player_paddle_height
    global default_option

    difficulty = value
    player_paddle_height = selected[0][1]


def quit_game():
    pygame.quit()


def play():
    # Define the objects.
    ball = Ball(WIDTH // 2, HEIGHT // 2, ball_size, WHITE, FIELD)
    player1 = Paddle(10, HEIGHT // 2 - player_paddle_height // 2,
                     paddle_width, player_paddle_height, paddle_speed, WHITE, FIELD)
    cpu = Paddle(WIDTH - paddle_width - 10, HEIGHT // 2 - paddle_height // 2,
                 paddle_width, paddle_height, paddle_speed, WHITE, FIELD, difficulty, ball_obj=ball)
    score = Score(get_font(22), WHITE, FIELD, WIDTH, HEIGHT)

    # Assign the paddle objects to the ball class.
    ball.p1_paddle = player1
    ball.cpu_paddle = cpu

    while True:
        FIELD.fill(1)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1.y_vel = -1
                if event.key == pygame.K_s:
                    player1.y_vel = 1
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            if event.type == pygame.KEYUP:
                player1.y_vel = 0

        if WIDTH <= ball.x_pos or ball.x_pos <= 0:
            if ball.x_pos <= 0:
                score.p1_score += 1
                ball.x_vel = 10
            else:
                score.p2_score += 1
                ball.x_vel = -10
            ball.reset()

        player1.move()
        cpu.cpu_ai()
        ball.handle_collision()
        ball.handle_movement()

        player1.update()
        cpu.update()
        ball.update()
        score.update()
        pygame.draw.line(FIELD, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        pygame.display.update()
        clock.tick(FPS)


def main_menu():
    running = True

    while running:
        FIELD.fill(1)

        menu_theme = Theme(background_color=BLACK, title_font_color=WHITE, widget_padding=5,
                           title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
                           widget_selection_effect=pygame_menu.widgets.NoneSelection(),
                           fps=60, title_font=get_font(150), widget_alignment=pygame_menu.locals.ALIGN_LEFT,
                           widget_margin=(10, 0), widget_font_color=WHITE, title_offset=(10, 70))

        menu = pygame_menu.Menu('Pong', 800, 600, theme=menu_theme)
        menu.add.button('Play', play)
        menu.add.dropselect('Difficulty :',
                            [('Easy', 120), ('Normal', 100), ('Hard', 80), ('Impossible', 65)],
                            default=1, onchange=set_difficulty, selection_box_bgcolor=BLACK,
                            selection_box_border_color=WHITE, selection_option_font_color=WHITE,
                            selection_option_selected_font_color=BLACK, placeholder_add_to_selection_box=False,
                            selection_box_height=4)
        menu.add.button('Quit', quit_game)
        menu.mainloop(FIELD)


if __name__ == "__main__":
    main_menu()
    pygame.quit()
