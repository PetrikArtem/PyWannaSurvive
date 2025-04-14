import pygame
from settings import *

class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, direction):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        
        if direction == "up":
            self.triangle_points = [
                (0, height),           # Левый нижний угол
                (width // 2, 0),       # Вершина треугольника (вверху)
                (width, height)        # Правый нижний угол
            ]
        elif direction == "right":
            self.triangle_points = [
                (0, 0),                # Левый верхний угол
                (0, height),           # Левый нижний угол
                (width, height // 2)   # Вершина треугольника (справа)
            ]
        elif direction == "down":
            self.triangle_points = [
                (0, 0),                # Левый верхний угол
                (width // 2, height),  # Вершина треугольника (внизу)
                (width, 0)             # Правый верхний угол
            ]
        elif direction == "left":
            self.triangle_points = [
                (width, 0),            # Правый верхний угол
                (0, height // 2),      # Вершина треугольника (слева)
                (width, height)        # Правый нижний угол
            ]
        
        # Рисуем треугольник на изображении
        pygame.draw.polygon(self.image, RED, self.triangle_points)
        
        # Создаем маску для точного треугольного хитбокса
        self.mask = pygame.mask.from_surface(self.image)