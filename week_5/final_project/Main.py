import pygame
import os
import Objects
import ScreenEngine
import Logic
import Service


SCREEN_DIM = (800, 600)

pygame.init()
gameDisplay = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption("MyRPG")
KEYBOARD_CONTROL = True

if not KEYBOARD_CONTROL:
    import numpy as np
    answer = np.zeros(4, dtype=float)

base_stats = {
    "strength": 20,
    "endurance": 20,
    "intelligence": 5,
    "luck": 5
}


def create_game(sprite_size, is_new):
    global hero, engine, drawer, iteration
    if is_new:
        hero = Objects.Hero(base_stats, Service.create_sprite(
            os.path.join("texture", "Hero.png"), sprite_size))
        engine = Logic.GameEngine()
        Service.service_init(sprite_size)
        Service.reload_game(engine, hero)
        with ScreenEngine as SE:
            drawer = SE.GameSurface((640, 480), pygame.SRCALPHA, (0, 480),
                                    SE.ProgressBar((640, 120), (640, 0),
                                                   SE.InfoWindow((160, 600), (50, 50),
                                                                 SE.HelpWindow((700, 500), pygame.SRCALPHA, (0, 0),
                                                                               SE.ScreenHandle(
                                                                                   (0, 0))
                                                                               ))))

    else:
        engine.sprite_size = sprite_size
        hero.sprite = Service.create_sprite(
            os.path.join("texture", "Hero.png"), sprite_size)
        Service.service_init(sprite_size, False)

    Logic.GameEngine.sprite_size = sprite_size

    drawer.connect_engine(engine)

    iteration = 0


size = 60
create_game(size, True)

while engine.working:

    if KEYBOARD_CONTROL:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                engine.working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    engine.show_help = not engine.show_help
                if event.key == pygame.K_KP_PLUS:
                    size = size + 1
                    create_game(size, False)
                if event.key == pygame.K_KP_MINUS:
                    size = size - 1
                    create_game(size, False)
                if event.key == pygame.K_r:
                    create_game(size, True)
                if event.key == pygame.K_ESCAPE:
                    engine.working = False
                if engine.game_process:
                    if event.key == pygame.K_UP:
                        engine.move_up()
                        iteration += 1
                    elif event.key == pygame.K_DOWN:
                        engine.move_down()
                        iteration += 1
                    elif event.key == pygame.K_LEFT:
                        engine.move_left()
                        iteration += 1
                    elif event.key == pygame.K_RIGHT:
                        engine.move_right()
                        iteration += 1
                else:
                    if event.key == pygame.K_RETURN:
                        create_game()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                engine.working = False
        if engine.game_process:
            actions = [
                engine.move_right,
                engine.move_left,
                engine.move_up,
                engine.move_down,
            ]
            answer = np.random.randint(0, 100, 4)
            prev_score = engine.score
            move = actions[np.argmax(answer)]()
            state = pygame.surfarray.array3d(gameDisplay)
            reward = engine.score - prev_score
            print(reward)
        else:
            create_game()

    gameDisplay.blit(drawer, (0, 0))
    drawer.draw(gameDisplay)

    pygame.display.update()

pygame.display.quit()
pygame.quit()
exit(0)
