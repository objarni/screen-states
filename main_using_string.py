import pygame

"""
I denna struktur använder vi en enkel textsträng för
att beskriva vilket state vi befinner oss i.
"""
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def mainloop(screen, font):
    # Initial state
    state = "start"

    while True:
        # Event handling
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if state == "start":
                if ev.key == pygame.K_SPACE:
                    state = "end"
            if state == "end":
                if ev.key == pygame.K_ESCAPE:
                    state = "start"
        elif ev.type == pygame.QUIT:
            break

        # Render
        if state == "start":
            screen.fill(BLACK)
            text_surface = font.render("START SCREEN - press Space", True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (400, 200)
            screen.blit(text_surface, text_rect)

        if state == "end":
            screen.fill(BLACK)
            text_surface = font.render("END SCREEN - press Escape", True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (400, 200)
            screen.blit(text_surface, text_rect)

        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("State as string")
    font = pygame.font.Font(pygame.font.match_font('arial'), 30)
    mainloop(screen, font)
    pygame.quit()
