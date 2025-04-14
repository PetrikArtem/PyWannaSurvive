import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.velocity_x = 0  # Новая переменная
        self.velocity_y = 0
        self.image = pygame.Surface((30, 50))  # хитбокс
        self.image.fill(BLUE)  # цвет
        self.rect = self.image.get_rect()  # позиция и размер
        self.rect.x = x
        self.rect.y = y
        self.velocity_y = 0  # гравитация
        self.jumping = False  # статус прыжка

    def update(self, platforms, traps):
        # Гравитация
        self.velocity_y += 0.3

        # Управление
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit() # Выход по ESC
        elif keys[pygame.K_r]: # Рестарт
            self.rect.x = 100
            self.rect.y = 300
        elif keys[pygame.K_a]:
            self.velocity_x = -5
        elif keys[pygame.K_d]:
            self.velocity_x = 5
        else:
            self.velocity_x = 0  # Останавливаемся, если клавиши не нажаты

        # Прыжок (остаётся без изменений)
        if keys[pygame.K_SPACE] and not self.jumping:
            self.velocity_y = -10
            self.jumping = True

        # Применяем коллизии
        self.check_collision(platforms, traps)

        # Обновляем позицию
        self.rect.x += int(self.velocity_x)
        self.rect.y += int(self.velocity_y)

    def check_collision(self, platforms, traps):
        for trap in traps:
            if pygame.sprite.collide_mask(self, trap):
                self.rect.x = 100
                self.rect.y = 300

        # Горизонтальные коллизии
        self.rect.x += self.velocity_x
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            if self.velocity_x > 0:  # Движение вправо
                self.rect.right = hits[0].rect.left
                self.velocity_x = 0  # Полная остановка
            elif self.velocity_x < 0:  # Движение влево
                self.rect.left = hits[0].rect.right
                self.velocity_x = 0  # Полная остановка
        else:
            self.rect.x -= self.velocity_x  # Отменяем только если нет коллизии
            
        # Вертикальные коллизии
        self.rect.y += self.velocity_y
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            if self.velocity_y > 0:  # Падение вниз
                self.rect.bottom = hits[0].rect.top
                self.velocity_y = 0
                self.jumping = False
            elif self.velocity_y < 0:  # Прыжок вверх
                self.rect.top = hits[0].rect.bottom
                self.velocity_y = 0
        else:
            self.jumping = True
        self.rect.y -= self.velocity_y  # Всегда возвращаем для точного позиционирования