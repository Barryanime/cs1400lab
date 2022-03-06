import pygame, sys, math, random

def pixel_collision(mask1, rect1, mask2, rect2):
    offset_x = rect2[0] - rect1[0]
    offset_y = rect2[1] - rect1[1]
    # See if the two masks at the offset are overlapping.
    overlap = mask1.overlap(mask2, (offset_x, offset_y))
    return overlap

def main():
    # setup pygame
    pygame.init()

    screen_size = width, height = (600, 400)
    screen = pygame.display.set_mode(screen_size)

    ball = pygame.image.load("GolfBall.png").convert_alpha()
    ball = pygame.transform.smoothscale(ball, (75, 75))
    ball_mask = pygame.mask.from_surface(ball)

    ball_rects = []
    for count in range(10):
        ball_pos = (random.randint(0, width), random.randint(0,height))
        ball_rect = ball.get_rect()
        ball_rect.center = ball_pos
        ball_rects.append(ball_rect)

    player = pygame.image.load("alien1.png").convert_alpha()
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)

    # Game loop
    is_playing = True
    while is_playing:
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_playing = False

        # update the characters

        pos = pygame.mouse.get_pos()
        player_rect.center = pos

        # for ball_rect in ball_rects:
        #     if pixel_collision(player_mask, player_rect, ball_mask, ball_rect):
        #         print("pixel collision")
        #         ball_rects.remove(ball_rect)

        ball_rects = [rect for rect in ball_rects if not pixel_collision(player_mask, player_rect, ball_mask, rect)]
        # add more powerups
        if random.randint(0,100) > 98:
            ball_pos = (random.randint(0, width), random.randint(0,height))
            ball_rect = ball.get_rect()
            ball_rect.center = ball_pos
            ball_rects.append(ball_rect)

        # draw some stuff
        screen.fill((100,100,100))
        for ball_rect in ball_rects:
            screen.blit(ball, ball_rect)
        screen.blit(player, player_rect)

        pygame.display.update()
        pygame.time.wait(20)

    # after the loop
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()