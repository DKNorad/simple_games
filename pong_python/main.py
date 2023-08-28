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
ball_size = 16
ball_speed = 6


def main():
    running = True

    # Define the objects
    player1 = Paddle(0, 0, paddle_width, paddle_height, paddle_speed, WHITE, field)
    cpu = Paddle(WIDTH - paddle_width, 0, paddle_width, paddle_height, paddle_speed, WHITE, field)
    ball = Ball(WIDTH / 2, HEIGHT / 2, 10, ball_speed, WHITE, field)
    score = Score(pygame.font.get_default_font(), ball_size, WHITE, field, WIDTH / 2, None)

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
        cpu.y_vel = randint(-1, 1)

        # Detect collision
        for paddle in paddles:
            if pygame.Rect.colliderect(ball.get_rect(), paddle.get_rect()):
                ball.hit()

        if WIDTH <= ball.x_pos or ball.x_pos <= 0:
            if ball.x_pos <= 0:
                score.p1_score += 1
            else:
                score.p2_score += 1
            ball.reset()

        player1.move()
        cpu.move()
        ball.move()

        player1.update()
        cpu.update()
        ball.update()
        score.update()
        pygame.draw.line(field, WHITE, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
