import pygame, ctypes, sys, menu

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

pygame.init()
background = (54, 54, 54)
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("PALMS")
screen.fill(background)

menu.main_menu(width, height, screen)

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
