import pygame
import random

from Shapes import Ball


#constants
BACKGROUND_IMAGE = 'dog.jpg'

WINDOW_WIDTH = 930
WINDOW_HEIGHT = 800

LEFT = 1
REFRESH_RATE = 60
BALL_SIZE = 45


def addBall():
    x,y = pygame.mouse.get_pos()
    ball = Ball(x,y)
    vx = random.randint(-5, 5)
    vy = random.randint(-5, 5)
    ball.update_v(vx, vy)
    return ball

if __name__ == '__main__':
    # init game

    pygame.init()
    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game")
    img = pygame.image.load(BACKGROUND_IMAGE)
    screen.blit(img, (0, 0))
    pygame.display.flip()
    clock = pygame.time.Clock()
    balls_list = pygame.sprite.Group()
    new_balls_list = pygame.sprite.Group()

    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            elif event.type == pygame.MOUSEBUTTONDOWN  and LEFT == event.button:
                ball = addBall()
                balls_list.add(ball)
        # update balls locations, bounce from edges
        for ball in balls_list:
            ball.update_loc()
            x, y = ball.get_pos()
            vx, vy = ball.get_v()
            if x + BALL_SIZE > WINDOW_WIDTH or x < 0:
                vx *= -1
            if y + BALL_SIZE > WINDOW_HEIGHT or y < 0:
                vy *= -1
            ball.update_v(vx, vy)

        # find which balls collide and should be removed
        new_balls_list.empty()
        for ball in balls_list:
            balls_hit_list = pygame.sprite.spritecollide(ball,balls_list,False)
            if len(balls_hit_list) == 1:
                new_balls_list.add(ball)
        balls_list.empty()
        for ball in new_balls_list:
            balls_list.add(ball)

        # update screen with surviving balls
        screen.blit(img,(0, 0))
        balls_list.draw(screen)
        pygame.display.flip()
        clock.tick(REFRESH_RATE)

    pygame.quit()