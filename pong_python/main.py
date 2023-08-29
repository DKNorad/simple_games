import pygame
from paddle import Paddle
from ball import Ball
from score import Score
from random import randint

pygame.init()

WHITE = (255, 255, 255)

WIDTH, HEIGHT = 800, 600
field = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
FPS = 60

paddle_width = 16
paddle_height = 100
paddle_speed = 10
ball_size = 12
ball_speed = 6


def calculate_velocity(ball_obj, p1_paddle, cpu_paddle, side):
    if side == "left":
        paddle_middle_y = p1_paddle.y_pos + p1_paddle.height / 2
        paddle_height = p1_paddle.height
    else:
        paddle_middle_y = cpu_paddle.y_pos + cpu_paddle.height / 2
        paddle_height = cpu_paddle.height

    difference_with_ball = paddle_middle_y - ball_obj.y_pos
    print(difference_with_ball)
    vel_reduction = paddle_height / 2 / ball_obj.MAX_VEL
    print(vel_reduction)
    y_vel = difference_with_ball / vel_reduction
    print(y_vel)

    return y_vel


def handle_collision(ball_obj, p1_paddle, cpu_paddle):
    # Handle ball collision to top and bottom walls.
    if ball_obj.y_pos - ball_obj.radius <= 0:
        ball_obj.y_vel *= -1
    elif ball_obj.y_pos + ball_obj.radius >= ball_obj.field.get_size()[1]:
        ball_obj.y_vel *= -1

    # Handle ball collision to the player paddle on the left.
    if ball_obj.x_vel < 0:
        if p1_paddle.y_pos <= ball_obj.y_pos <= p1_paddle.y_pos + p1_paddle.height:
            if p1_paddle.x_pos + p1_paddle.width >= ball_obj.x_pos - ball_obj.radius:
                ball_obj.hit(-1 * calculate_velocity(ball_obj, p1_paddle, cpu_paddle, "left"))

    # Handle ball collision to the CPU paddle on the right.
    if ball_obj.x_vel > 0:
        if cpu_paddle.y_pos <= ball_obj.y_pos <= cpu_paddle.y_pos + cpu_paddle.height:
            if cpu_paddle.x_pos <= ball_obj.x_pos + ball_obj.radius:
                ball_obj.hit(-1 * calculate_velocity(ball_obj, p1_paddle, cpu_paddle, "left"))

def main():
    running = True

    # Define the objects
    player1 = Paddle(10, 0, paddle_width, paddle_height, paddle_speed, WHITE, field)
    cpu = Paddle(WIDTH - paddle_width - 10, 0, paddle_width, paddle_height, paddle_speed, WHITE, field)
    ball = Ball(WIDTH // 2, HEIGHT // 2, ball_size, ball_speed, WHITE, field)
    score = Score(pygame.font.get_default_font(), 22, WHITE, field, WIDTH, HEIGHT)

    paddles = [player1, cpu]

    while running:
        field.fill(1)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1.y_vel = -1
                if event.key == pygame.K_s:
                    player1.y_vel = 1
            if event.type == pygame.KEYUP:
                player1.y_vel = 0

        cpu.y_pos = ball.y_pos - 45

        if WIDTH <= ball.x_pos or ball.x_pos <= 0:
            if ball.x_pos <= 0:
                score.p1_score += 1
            else:
                score.p2_score += 1
            ball.reset()

        player1.move()
        cpu.move()
        ball.handle_movement()
        handle_collision(ball, player1, cpu)

        player1.update()
        cpu.update()
        ball.update()
        score.update()
        pygame.draw.line(field, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
