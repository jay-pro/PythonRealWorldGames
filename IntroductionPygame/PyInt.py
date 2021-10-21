import pygame
width, height = 800, 600

GScreen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game 1")

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        #GScreen.fill((255,255,255))
        GScreen.fill((255,0,255))
        pygame.display.update()

if __name__ == "__main__":
    main()