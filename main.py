import pygame
from settings import *
from src.player import Player
from src.platforms import Platform
from src.spikes import Spike

pygame.init()

# Экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PyWannaSurvive")
clock = pygame.time.Clock()

# Спрайты
all_sprites = pygame.sprite.Group()  # все объекты для отрисовки
platforms = pygame.sprite.Group()   # только платформы (для коллизий)
traps = pygame.sprite.Group()
# Игрок
player = Player(100, 300)
all_sprites.add(player)
# Ловушки
spike1 = Spike(380, 200, 100, 100, "up")
spike2 = Spike(470, 120, 100, 100, "down")
# Платформы
bottom_border = Platform(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40)
left_border = Platform(0,0, 5, 1080)
right_border = Platform(SCREEN_WIDTH - 5, 0, 5, SCREEN_HEIGHT)
top_border = Platform(0, 0, SCREEN_WIDTH, 5)
platform1 = Platform(100, 400, 200, 20)
platform2 = Platform(300, 300, 500, 2000)

traps.add(spike1, spike2)
platforms.add(bottom_border, left_border, right_border, top_border, platform1, platform2) # добавляем в группу для коллизий
all_sprites.add(bottom_border, platform1, platform2, spike1, spike2) # и для отрисовки

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update(platforms, traps)


    # Обновление экрана
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()