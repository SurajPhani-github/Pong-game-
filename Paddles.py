import pygame 


pygame.init()
width=1000
height=600
screen =pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running=True
dt=0
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

screen.fill("black")
pygame.display.flip()

paddle_height=100
paddle_width=10
paddle_speed=10

player_paddle1= pygame.Rect(80,height//2-paddle_height//2,paddle_width,paddle_height)
player_paddle2=pygame.Rect(80,height//2-paddle_height//2, paddle_width,paddle_height)

while running : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False


screen.fill("black")
screen.fill(player_paddle1)
screen.fill(player_paddle2)
pygame.display.flip()
