# create the screen
# Display
# pygame.init() = inicia todo los terminales de pygame. 
# pygame.quit() = cierra el programa. 
import pygame
pygame.init()

violet= (237, 28, 234) # Score
green= (101, 250, 95) # Background
blue= (15, 113, 214) # Fruit 
orange= (214, 120, 15) # Game over
yellow= (166, 250, 17) # Snake

dis=pygame.display.set_mode((600,500))

pygame.display.set_caption("Welcome to Snake Game, by 8bit")
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.rect(dis, yellow,[300, 250 , 20, 20])
    pygame.display.update()
pygame.quit()
quit()
