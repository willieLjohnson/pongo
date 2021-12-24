import pygame
from paddle import Paddle

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 172)
RED = (255, 0, 172)

SIZE = (700, 500)

def main():
    pygame.init()
    logo = pygame.image.load("dust.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Pongo")

    screen = pygame.display.set_mode(SIZE)

    running = True

    clock = pygame.time.Clock()

    paddleA = Paddle(GREEN, 5, 50)
    paddleA.rect.x = 20
    paddleA.rect.y = 200

    paddleB = Paddle(RED, 5, 50)
    paddleB.rect.x = 670
    paddleB.rect.y = 200

    sprites = pygame.sprite.Group()

    sprites.add(paddleA)
    sprites.add(paddleB)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    running = False

        sprites.update()
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
        sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()