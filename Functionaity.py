import Padle
import pygame 
pygame.init()
key= pygame.key.get_pressed()
screen =pygame.display.set_mode((Padle.width,Padle.height))
paddle_speed=5
FPS=60
width=1000
height=600
paddle_height=100
paddle_width=15

def move(self,up=True):
      if up:
            self.y-=self.paddle_speed
      else:      
            self.y+=self.paddle_speed


def paddle_movement(key,left_paddle,right_paddle):
        if key[pygame.K_w]:
                left_paddle.move(up=True)
        if key[pygame.K_s]:
                left_paddle.move(up=False)

        if key[pygame.K_UP]:
                right_paddle.move(up=True)
        if key[pygame.K_DOWN]:
                right_paddle.move(up=False)

def draw(Screen,paddles):
    screen.fill("black")
    for paddle in paddles:
        paddle.draw(screen)

    pygame.display.update()
class Paddle : 
    paddle_speed=5
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def draw(self,screen):
        pygame.draw.rect(screen,"white",(self.x,self.y,self.width,self.height))


def main():

    running = True 
    clock = pygame.time.Clock()
    left_paddle= Paddle(20, height//2 - paddle_height//2,paddle_width,paddle_height )
    right_paddle=Paddle(width-10-paddle_width,height//2-paddle_height//2,paddle_width,paddle_height)
    while running : 
        clock.tick(FPS)
        draw(screen,[left_paddle,right_paddle])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                break

if __name__=='__main__':
    main()
