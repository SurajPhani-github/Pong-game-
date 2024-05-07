import pygame 
import math 
import random
pygame.init()
width=1000
height=600
paddle_height=100
paddle_width=15
FPS=600
screen =pygame.display.set_mode((width,height))
# clock = pygame.time.Clock()
# running=True

# left_paddle= pygame.Rect(20, height//2 - paddle_height//2,paddle_width,paddle_height )
# right_paddle=pygame.Rect(width-10-paddle_width,height//2-paddle_height//2,paddle_width,paddle_height)


font_score=pygame.font.SysFont("Times New Roman",54)

def draw(Screen,paddles,ball,left_score,right_score):
    screen.fill("black")
    left_score_text=font_score.render(f"{left_score}",1,"white")
    right_score_text=font_score.render(f"{right_score}",1,"white")
    screen.blit(left_score_text,(width//4-left_score_text.get_width()//2,30))
    screen.blit(right_score_text,(width*(3/4)- right_score_text.get_width()//2,30))
    for paddle in paddles:
        paddle.draw(screen)
    for x in range(10, height, height//40):
          if x % 2 ==1: 
            continue
          pygame.draw.rect(screen, "white", (width//2 -10,x,5,height//40))
    ball.draw(screen)
    pygame.display.update()


class Paddle : 
    paddle_speed=2
    def __init__(self, x, y, width, height):
        self.x=self.initial_x=x
        self.y=self.initial_y=y
        self.width=width
        self.height=height

    def draw(self,screen):
        pygame.draw.rect(screen,"white",(self.x,self.y,self.width,self.height))
    
    def move(self,up=True):
        paddle_speed=2
        if up:
                self.y-=self.paddle_speed
        else:      
                self.y+=self.paddle_speed
    def restart(self):
         self.x=self.initial_x
         self.y=self.initial_y

class Ball :
        speed=1.3
        max_speed=2.8
        def __init__(self,radius,x,y):
              self.radius = radius 
              self.x=self.intial_x=x
              self.y=self.initial_y=y
               
              self.x_speed= self.speed
              self.y_speed=-0.3
              

        def draw(self,screen):
             pygame.draw.circle(screen,"white",(self.x, self.y),self.radius)

        def move(self):
              self.x+=self.x_speed
              self.y+=self.y_speed

        def restart(self):
             self.x=self.intial_x
             self.y=self.initial_y
             self.y_speed=0
             self.x_speed*=-1
             self
radius=9

def collision(ball, left_paddle, right_paddle):
    radius = ball.radius
    if ball.y + radius >= height :
        ball.y_speed *=-1
    elif ball.y - radius <= 0 :
         ball.y_speed *= -1
    if ball.x_speed <0 :
         if ball.y>=left_paddle.y and ball.y-radius <=left_paddle.y + paddle_height :
              if ball.x -radius <= left_paddle.x + paddle_width:
                    ball.x_speed *= -1
                    mid_y=left_paddle.y+ left_paddle.height/2
                    diff_y= (mid_y-ball.y) 
                    bounce_angle=diff_y * (math.pi/4)
                    change=(left_paddle.height/2)/ball.max_speed
                    y_speed= diff_y/change
                    ball.y_speed=-1* y_speed
                    # ball_speed= math.sqrt(ball.x_speed **2 + ball.y_speed **2 )
                    # ball.x_speed = ball_speed * math.cos(bounce_angle)
                    # ball.y_speed= -ball_speed * math.sin(bounce_angle)        
    else : 
         if ball.y  >=right_paddle.y and ball.y-radius<= right_paddle.y+paddle_height :
              if ball.x + ball.radius >=right_paddle.x :
                   ball.x_speed *= -1
                   mid_y=right_paddle.y+right_paddle.height/2
                   diff_y= (mid_y-ball.y) 
                   change=(right_paddle.height/2)/ball.max_speed
                   y_speed= diff_y/change
                   ball.y_speed=-1*y_speed
    #                ball_speed= math.sqrt(ball.x_speed **2 + ball.y_speed **2 )
    #                bounce_angle=diff_y * (math.pi/4)
    #                ball.x_speed = -ball_speed * math.cos(bounce_angle)
    #                ball.y_speed= -ball_speed * math.sin(bounce_angle)  
    # return ball
                  

#      FUNTIONAITY     #



def paddle_movement(keys,left_paddle,right_paddle):
        if keys[pygame.K_w] and left_paddle.y - left_paddle.paddle_speed >=1:
                left_paddle.move(up=True)
        if keys[pygame.K_s] and left_paddle.y + left_paddle.paddle_speed + left_paddle.height  < height :
                left_paddle.move(up=False)

        if keys[pygame.K_UP] and right_paddle.y-right_paddle.paddle_speed >=1:
                right_paddle.move(up=True)
        if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.paddle_speed + right_paddle.height  < height : 
                right_paddle.move(up=False)
               
def main():

    running = True 
    clock = pygame.time.Clock()
    left_paddle= Paddle(10, height//2 - paddle_height//2,paddle_width,paddle_height )
    right_paddle=Paddle(width-10-paddle_width,height//2-paddle_height//2,paddle_width,paddle_height)
    ball=Ball(radius,width//2,height//2)
    left_score=0
    right_score=0 
    total_score=5
    while running :
        clock.tick(FPS)
        start_text="TotaL Game for 5 points"
        s_text=font_score.render(start_text,1,"white")
        screen.blit(s_text,(width//2-s_text.get_width()//2, height//2-s_text.get_height()//2))
        pygame.display.update()
        pygame.time.delay(2000)
        draw(screen,[left_paddle,right_paddle],ball,left_score,right_score)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       
                running=False
                break
        keys= pygame.key.get_pressed()
        paddle_movement(keys,left_paddle,right_paddle)
        ball.move()
        collision(ball,left_paddle,right_paddle)  

        if ball.x<0:
             right_score+=1
             ball.restart()
        elif ball.x>width:
             left_score+=1
             ball.restart()
        winning=False
        if left_score>=total_score:
             winning=True
             text="Left player wins!!"
        elif right_score>=total_score:
             winning=True
             text="Right player wins!!"
        if winning:
             winning_text=font_score.render(text,1,"white")
             screen.blit(winning_text,(width//2-winning_text.get_width()//2, height//2-winning_text.get_height()//2))
             pygame.display.update()
             pygame.time.delay(4000)
             ball.restart()
             left_paddle.restart()
             right_paddle.restart()
             left_score=0
             right_score=0
                        
if __name__=='__main__':
    main()
