import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_SPEED = 5
PADDLE_SPEED = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Пинг-понг')

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)

    def move(self, up=True):
        if up:
            self.rect.y -= PADDLE_SPEED
        else:
            self.rect.y += PADDLE_SPEED

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        self.vx = BALL_SPEED
        self.vy = BALL_SPEED

    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.vy = -self.vy

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.rect.center = (WIDTH // 2, HEIGHT // 2)
            self.vx = -self.vx

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)

    def collide_with_paddle(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.vx = -self.vx

def main():
    clock = pygame.time.Clock()

    left_paddle = Paddle(30, HEIGHT // 2 - 50)
    right_paddle = Paddle(WIDTH - 40, HEIGHT // 2 - 50)
    ball = Ball()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            left_paddle.move(up=True)
        if keys[pygame.K_s]:
            left_paddle.move(up=False)
        if keys[pygame.K_UP]:
            right_paddle.move(up=True)
        if keys[pygame.K_DOWN]:
            right_paddle.move(up=False)

        ball.move()
        ball.collide_with_paddle(left_paddle)
        ball.collide_with_paddle(right_paddle)

        screen.fill(BLACK)
        left_paddle.draw(screen)
        right_paddle.draw(screen)
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()

