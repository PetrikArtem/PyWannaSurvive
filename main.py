import pygame
from settings import *

pygame.init()

# Экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PyWannaSurvive")
clock = pygame.time.Clock()

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Фон
    screen.fill(BLACK)

    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()