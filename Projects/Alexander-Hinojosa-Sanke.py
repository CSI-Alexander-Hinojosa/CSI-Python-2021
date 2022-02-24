from email import message
import pygame        
pygame.init()
import time

# create the screen
# Display
# pygame.init() = inicia todo los terminales de pygame. 
# pygame.quit() = cierra el programa. 

violet= (237, 28, 234) # Score
green= (101, 250, 95) # Fruit
blue= (15, 113, 214) # Snake
orange= (214, 120, 15) # Game over
yellow= (166, 250, 17) # Background 

dis_widht=500
dis_lenght=400

dis=pygame.display.set_mode((dis_widht,dis_lenght))

pygame.display.set_caption("Welcome to Snake Game, by 8bit")
game_over=False


clock= pygame.time.Clock()
snake_speed = 15 

snake_block=10
font_style= pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_widht/2, dis_lenght/3])

def game_loop():
    game_over = False
    game_close = False

x1= dis_widht/2
y1= dis_lenght/2

x1_change= 0
y1_change= 0

while not game_over:
    while game_close ==True:
        dis.fill(yellow)
        message("F, press Q-Quit or P-Play again", orange)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over=True
                    game_close=False
                if event.key == pygame.K_p:
                    gameLoop()




    for event in pygame.event.get():
        if event.type==pygame.QUIT:
             game_over=True    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -snake_block
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_block
    if x1 >= dis_widht or x1 < 0 or y1 <= dis_lenght or y1 <0:    
        game_over = True
 
#  error in gameover true

    x1 += x1_change
    y1 += y1_change
    dis.fill(yellow)

# Al realizar movimiento vertical, negativo (-) es hacia arriba, mientras que positivo (+) es hacia abajo.

    pygame.draw.rect(dis, blue,[x1, y1 , snake_block, snake_block])

    pygame.display.update()

    clock.tick(snake_speed) 

message("F", orange)
pygame.display.update()

# time.sleep(5)

pygame.quit()
quit()
