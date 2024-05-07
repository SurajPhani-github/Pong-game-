import pygame

pygame.init()
screen =pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
pygame.display.set_caption("Pong Game")
FPS=60

def draw(Screen):
    screen.fill("black")
    pygame.display.update()
def main():

    running = True 
    clock = pygame.time.Clock()
    while running : 
        clock.tick(FPS)
        draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                break


if __name__=='__main__':
    main()
