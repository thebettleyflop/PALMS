import pygame
def main_menu(width, height, screen):
    pygame.draw.rect(screen, (40, 40, 40), (width * 0.145, height * 0.195, width * 0.71, height * 0.615), 0)
    pygame.draw.rect(screen, (228, 138, 64), (width * 0.15, height * 0.2, width * 0.7, height * 0.6), 0)
    pygame.draw.rect(screen, (79, 129, 189), (width * 0.15, height * 0.2, width * 0.175, height * 0.3), 0)
    pygame.draw.rect(screen, (205, 153, 205), (width * 0.15, height * 0.5, width * 0.175, height * 0.3), 0)
    pygame.draw.rect(screen, (146, 208, 80), (width * 0.325, height * 0.5, width * 0.175, height * 0.3), 0)
    pygame.draw.rect(screen, (195, 199, 19), (width * 0.5, height * 0.5, width * 0.175, height * 0.3), 0)
    pygame.draw.rect(screen, (255, 131, 131), (width * 0.675, height * 0.5, width * 0.175, height * 0.3), 0)
    pygame.draw.rect(screen, (116, 239, 242), (width * 0.675, height * 0.2, width * 0.175, height * 0.3), 0)

    font = pygame.font.SysFont("Arial Black", int(width*0.0235) )

    collisions = font.render("Collisions", 1, (255, 255, 255))
    screen.blit(collisions, (width*0.175 , height*0.43))