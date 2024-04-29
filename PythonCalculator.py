import pygame
import sys
from pygame.locals import *

pygame.init()

# Устанавливаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Устанавливаем размер окна
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Complex Calculator")

# Устанавливаем шрифт и размер текста
font = pygame.font.Font(None, 32)

def draw_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def calculator():
    running = True
    expression = ""
    result = ""

    while running:
        screen.fill(WHITE)

        draw_text("Enter expression:", 20, 20, BLACK)
        draw_text(expression, 20, 50, BLACK)

        draw_text("Result:", 20, 120, BLACK)
        draw_text(result, 20, 150, BLACK)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    try:
                        result = str(eval(expression))
                    except:
                        result = "Error"
                elif event.key == K_BACKSPACE:
                    expression = expression[:-1]
                elif event.unicode.isdigit() or event.unicode in ['+', '-', '*', '/']:
                    expression += event.unicode

        pygame.display.update()

    pygame.quit()

calculator()