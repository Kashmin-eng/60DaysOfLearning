import pygame #importing Pygame Module
pygame.init()

win = pygame.display.set_mode((500,500)) #size of Game panel
pygame.display.set_caption("First Game") #Display on Caprion

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:   #if red cross button is clicked it will exit
            run = False
    
    keys = pygame.key.get_pressed()         # Getting data from arrow keys
    if keys[pygame.K_LEFT]:          
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0,0,0))  #in python colour combination is always R,G,B
    pygame.draw.rect(win, (255, 156, 179),(x, y, width, height)) 
    pygame.display.update()
pygame.quit()