import pygame #importing Pygame Module
pygame.init()

win = pygame.display.set_mode((500,500)) #size of Game panel
pygame.display.set_caption("First Game") #Display on Caprion

walkRight = [pygame.image.load('Game1/R1.png'), pygame.image.load('Game1/R2.png'), pygame.image.load('Game1/R3.png'), pygame.image.load('Game1/R4.png'), pygame.image.load('Game1/R5.png'), pygame.image.load('Game1/R6.png'), pygame.image.load('Game1/R7.png'), pygame.image.load('Game1/R8.png'), pygame.image.load('Game1/R9.png')]
walkLeft = [pygame.image.load('Game1/L1.png'), pygame.image.load('Game1/L2.png'), pygame.image.load('Game1/L3.png'), pygame.image.load('Game1/L4.png'), pygame.image.load('Game1/L5.png'), pygame.image.load('Game1/L6.png'), pygame.image.load('Game1/L7.png'), pygame.image.load('Game1/L8.png'), pygame.image.load('Game1/L9.png')]
bg = pygame.image.load('Game1/bg.jpg')
char = pygame.image.load('Game1/standing.png')

clock = pygame.time.Clock()
x = 50
y = 400
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1
    else:
        win.blit(char, (x,y))
    
    pygame.display.update()

#mainLoop
run = True
while run:
    clock.tick(27)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:   #if red cross button is clicked it will exit
            run = False
    
    keys = pygame.key.get_pressed()         # Getting data from arrow keys

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()

pygame.quit()