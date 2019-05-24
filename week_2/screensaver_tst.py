from typing import Tuple, List  # Any, Union
import pygame

SCREEN_DIM: Tuple[int, int] = (800, 600)


def main():
    # Основная программа
    pygame.init()

    # <class 'pygame.Surface'>
    gameDisplay: object = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    # steps: int = 35
    # speeds: List[Tuple[Union[int, Any], Union[int, Any]]] = []
    # show_help: bool = False
    working: bool = True
    points: List[Tuple[int, int]] = []
    pause: bool = True

    print("\nTesting:\n=== === === === === ===\n\n")

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    points = []
                if event.key == pygame.K_p:
                    pause = not pause

            if event.type == pygame.MOUSEBUTTONDOWN:
                points.append(event.pos)  # [(487, 248)]
                print(points)

        gameDisplay.fill((0, 0, 0))

    print("type(gameDisplay)", type(gameDisplay))
    # <class 'pygame.Surface'>

    print("gameDisplay.__dir__:  \n\t", gameDisplay.__dir__)
    # <built-in method __dir__ of pygame.Surface object at 0x10c097ab0 >

    print("gameDisplay.__doc__:  \n\t", gameDisplay.__doc__)
    # Surface((width, height), flags=0, depth=0, masks=None) -> Surface
    # Surface((width, height), flags=0, Surface) -> Surface
    # pygame object for representing images

    print("gameDisplay.__class:__\n\t", gameDisplay.__class__)
    # <class 'pygame.Surface'>

    pygame.display.quit()
    pygame.quit()
    exit(0)


if __name__ == "__main__":
    main()
