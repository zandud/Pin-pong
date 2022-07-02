from classes import *

def draws(objs):
    window.blit(background, (0, 0))
    for obj in objs:
        obj.draw()

def moves(ball, right_rocket, left_rocket):
    ball.auto_move()
    right_rocket.move2()
    left_rocket.move1()

def mainloop():
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
                ball.dirX *= -1
        else:
            window.blit(game_over, (int(wid/2-150), int(up/2-100)))
            # Возможность перезапуска:
            keys_pressed = key.get_pressed()
            if keys_pressed[K_SPACE]:
                ball = Ball(int(wid/2), int(up/2), 'res/ball.png', int(2*(wid/up)), int(18*(wid/up)), int(18*(wid/up)))
        display.update()
        clock.tick(120)

background = transform.scale(image.load('res/sky.png'), (wid, up))
ball = Ball(int(wid/2), int(up/2), 'res/ball.png', int(2*(wid/up)), int(18*(wid/up)), int(18*(wid/up)))
left_rocket = Player(25, int(up/2), 'res/right-rocket.png', int(4*(wid/up)), int(70*(wid/up)), int(70*(wid/up)))
right_rocket = Player(wid-25-120, int(up/2), 'res/left-rocket.png', int(4*(wid/up)), int(70*(wid/up)), int(70*(wid/up)))

mainloop()
