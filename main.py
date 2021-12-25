import pygame
from paddle import Paddle
from ball import Ball

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

    paddleA = Paddle(GREEN, 5, 75)
    paddleA.rect.x = 20
    paddleA.rect.y = 200

    paddleB = Paddle(RED, 5, 75)
    paddleB.rect.x = 670
    paddleB.rect.y = 200

    ball = Ball(WHITE, 10, 10)
    ball.rect.x = 345
    ball.rect.y = 195

    sprites = pygame.sprite.Group()

    sprites.add(paddleA)
    sprites.add(paddleB)
    sprites.add(ball)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
        if keys[pygame.K_s]:
            paddleA.moveDown(5)
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(5)

        sprites.update()

        if ball.rect.x >= 690:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > 490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
            ball.bounce()
        
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
        sprites.draw(screen)
        pygame.display.flip()
        
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()