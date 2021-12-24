import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SIZE = (700, 500)

def main():
    pygame.init()
    logo = pygame.image.load("dust.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Pongo")

    screen = pygame.display.set_mode(SIZE)

    running = True

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()