import pygame as pg


pg.init()   

WIDTH, HEIGHT = 700, 500
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("PONG")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT  = 20, 100
BALL_RADIUS = 7

SCORE_FONT = pg.font.SysFont("Helvetica", 25)
WINNING_SCORE = 3

class Paddle:
    #   Class Variable -- note that anything that applies to all paddles are made to be class variables
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height):
        self.x =self.original_x = x
        self.y= self.original_y = y
        self.width, self.height = width, height


    def draw(self, win: pg.Surface):
        pg.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))
    
    def move(self, up=True):
        if up:  #   If up
            self.y -= self.VEL
        else:   #   Else down
            self.y += self.VEL
    
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y


class Ball:
    MAX_VEL = 5

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        #   Always at max velocity in X direction
        self.x_vel = self.MAX_VEL
        #   Only y direction velocity changes
        self.y_vel = 0
    
    def draw(self, win: pg.Surface):
        pg.draw.circle(win, WHITE, (self.x, self.y), self.radius)
    
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        #   To reverse who the ball moves toward after ball goes out; it goes toward the opposite direction to where it went out.
        self.x_vel *= -1
        


def draw(win: pg.Surface, paddles: list[Paddle], ball:Ball, left_score, right_score):  
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(WIN)
    
    #   The '1' is for anti-aliasing
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)

    win.blit(left_score_text, (WIDTH // 4 - left_score_text.get_width() // 2, 20))
    win.blit(right_score_text, (WIDTH*(3/4) - right_score_text.get_width() // 2, 20))
    

    #   Drawing line in middle of screen
    line_rect_width = 10
    #   Note that the increment is height // 20
    for i in range(10, HEIGHT, HEIGHT // 20):
        #   Drawing Rectangles with gaps between them
        if i % 2 == 1:
            continue
        #.rect(x, y, width, height)
        pg.draw.rect(win, WHITE, (WIDTH // 2 - line_rect_width // 2, i, line_rect_width, HEIGHT // 20))

    ball.draw(WIN)

    pg.display.update()


def handle_collision(ball: Ball, left_paddle: Paddle, right_paddle: Paddle):
    """Collisions of ball with ceiling and paddles"""
    #   Colissions with ceilings
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1
    
    #   Collisions with paddles
    
    
    """
        Theory:
        The Y-direction change
        involves getting y-displacement of the ball from the center of the paddle, then get the angle

        When the y-displacement of th eball from the center of the paddle is maximum, the y-velocity should also
        be maximum.
        That is, the closer to the center the ball is to the paddle, the slower its speed at which it rebounds.
        So the y_vel = MAX_VEL * (difference_in_y/paddle_height/2) 

    """

    if ball.x_vel < 0:  ##  If ball is moving left
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y =  middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = y_vel * -1
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1
    
                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y =  middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = y_vel * -1

def handle_paddle_movement(keys, left_paddle:Paddle, right_paddle:Paddle):
    if keys[pg.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up=True)
    if keys[pg.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)
    
    if keys[pg.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    if keys[pg.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)


def main():
    run = True
    clock = pg.time.Clock()
    
    #   the HEIGHT // 2 - PADDLE_HEIGHT // 2 is make the position of the paddle correspond to its center lengthwise
    left_paddle = Paddle(10, HEIGHT // 2 -PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 -PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    left_score = 0
    right_score = 0


    while run:
        clock.tick(FPS) #   regulates the speed of the wile loop
        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break # out of for loop

        """It's double player --this one"""
        keys = pg.key.get_pressed() #   <-- map of pressed keys
        handle_paddle_movement(keys, left_paddle, right_paddle)
        handle_collision(ball, left_paddle, right_paddle)

        #   For scoring when the ball goes off the screen
        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()

        won = False
        if left_score >= WINNING_SCORE:
            won = True
            win_text = "Left Player Won!"
        elif right_score >= WINNING_SCORE:
            won = True
            win_text = "Right Player Won!"

        if won:
            render_win_text = SCORE_FONT.render(win_text, 1, pg.Color("gainsboro")) 
            WIN.blit(render_win_text, (WIDTH // 2 - render_win_text.get_width() // 2, HEIGHT // 2 - render_win_text.get_height() // 2))
            pg.display.update()
            pg.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0

        ball.move()
                
    
    pg.quit()


if __name__=="__main__":
    main()