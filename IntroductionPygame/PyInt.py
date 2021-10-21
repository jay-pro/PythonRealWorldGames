import pygame
import os

width, height = 800, 600

FPS = 60

GScreen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game 1")
PICTURE = pygame.image.load(os.path.join("D:/18110168_GITHUBS/PythonRealWorldGames/IntroductionPygame/resources","OhYouthKarryon.jpg"))
SONG = os.path.join(os.getcwd(), "D:/18110168_GITHUBS/PythonRealWorldGames/IntroductionPygame/resources/Reminiscence-JohannesBornlof.mp3")

def draw_fn():
    #GScreen.fill((255,255,255))
    GScreen.fill((255,0,255))
    GScreen.blit(PICTURE,(0,0))

    pygame.display.update()

def main():
    pygame.mixer.init()
    pygame.mixer.music.load(SONG)
    pygame.mixer.music.play(-1)
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        draw_fn()

if __name__ == "__main__":
    main()