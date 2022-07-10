from classes import *

def draws(objs):
    window.blit(background, (0, 0))
    for obj in objs:
        obj.draw()

def moves(ball, right_rocket, left_rocket):
    ball.auto_move()
    right_rocket.move2()
    left_rocket.move1()

def settings(mode):
    b_standart = GameSprite(wid/2, up/2 - 100, 'res/standart.png', 0, 349*scale, 82*scale)
    b_random = GameSprite(wid/2, up/2 + 100, 'res/random.png', 0, 315*scale, 78*scale)
    b_exit = GameSprite(50, 50, 'res/vixod.png', 0, 156*scale, 69*scale)
    green_fon =  GameSprite(50, 50, 'res/green_fon.jpg', 0, 400*scale, 100*scale)
    game = True
    clock = time.Clock()
    while game:
        if mode == 'standart':
            green_fon.rect.x = wid/2 - 30
            green_fon.rect.y = up/2 - 130
        else:
            green_fon.rect.x = wid/2 - 30
            green_fon.rect.y = up/2 + 70
        draws((green_fon, b_standart, b_random, b_exit))
        for e in event.get():
            if e.type == QUIT:
                game = False
                exit()
            elif e.type == MOUSEBUTTONDOWN and e.button == 1:
                x, y = e.pos
                if b_exit.rect.collidepoint(x, y):
                    game = False
                elif b_standart.rect.collidepoint(x, y):
                    mode = 'standart'
                elif b_random.rect.collidepoint(x, y):
                    mode = 'random'
        display.update()
        clock.tick(120)
    return mode
def menu():
    b_play = GameSprite(wid/2 - 100*scale, up/2 - 100*scale, 'res/play.png', 0, 200*scale, 200*scale)
    b_exit = GameSprite(b_play.rect.bottomright[0], b_play.rect.bottomright[1] ,'res/exit.png', 0, 105*scale, 105*scale)
    b_settings = GameSprite(b_play.rect.bottomleft[0] - 100*scale, b_play.rect.bottomleft[1], 'res/settings.png', 0, 120*scale, 120*scale)
    game = True
    mode = 'standart'
    clock = time.Clock()
    while game:
        for e in event.get():
            if e.type == QUIT:
                game = False
                exit()
            elif e.type == MOUSEBUTTONDOWN and e.button == 1:
                x, y = e.pos
                if b_exit.rect.collidepoint(x, y):
                    exit()
                elif b_play.rect.collidepoint(x, y):
                    game = False
                elif b_settings.rect.collidepoint(x, y):
                    mode = settings(mode)
        draws((b_settings, b_play, b_exit))
        display.update()
        clock.tick(120)
    return mode
def mainloop(mode):
    global ball
    game = True
    clock = time.Clock()
    game_over = font.Font(None, 100).render('YOU LOSE!!!', True, (70, 0, 0))

    while game:
        for e in event.get():
            if e.type == QUIT:
                game = False
        draws((ball, left_rocket, right_rocket)) # Отрисовка всех игровых объектов в цикле
        if ball.is_outside == False:
            moves(ball, right_rocket, left_rocket) # Перемещение игровых объектов в цикле
            if sprite.collide_rect(left_rocket, ball) or sprite.collide_rect(right_rocket, ball):
                if mode == 'random':
                    ball.dirY = uniform(-1, 1)
                ball.dirX *= -1
        else:
            window.blit(game_over, (int(wid/2-150), int(up/2-100)))
            # Возможность перезапуска:
            keys_pressed = key.get_pressed()
            if keys_pressed[K_SPACE]:
                ball = Ball(int(wid/2), int(up/2), 'res/ball.png', 6*scale, 30*scale, 30*scale)
        display.update()
        clock.tick(120)

background = transform.scale(image.load('res/sky.png'), (wid, up))
ball = Ball(int(wid/2), int(up/2), 'res/ball.png', 6*scale, 30*scale, 30*scale)
left_rocket = Player(25, int(up/2), 'res/right-rocket.png', 8*scale, 120*scale, 120*scale)
right_rocket = Player(wid-25-120*scale, int(up/2), 'res/left-rocket.png', 8*scale, 120*scale, 120*scale)

mode = menu()
mainloop(mode)
