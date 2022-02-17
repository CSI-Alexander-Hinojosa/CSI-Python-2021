import pygame        
pygame.init()

# create the screen
# Display
# pygame.init() = inicia todo los terminales de pygame. 
# pygame.quit() = cierra el programa. 

violet= (237, 28, 234) # Score
green= (101, 250, 95) # Fruit
blue= (15, 113, 214)  # Background
orange= (214, 120, 15) # Game over
yellow= (166, 250, 17) # Snake

dis=pygame.display.set_mode((600,500))

pygame.display.set_caption("Welcome to Snake Game, by 8bit")
game_over=False

x1= 300
y1= 300

x1_change= 0
y1_change= 0

clock= pygame.time.Clock()


while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            if event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            if event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            if event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    x1 += x1_change
    y1 += y1_change
    dis.fill(yellow)

# Al realizar movimiento vertical, negativo (-) es hacia arriba, mientras que positivo (+) es hacia abajo.

    pygame.draw.rect(dis, blue,[x1, y1 , 25, 25])

    pygame.display.update()

    clock.tick(25)
pygame.quit()
quit()
