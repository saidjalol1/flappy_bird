import pygame


pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

#load images
bg = pygame.image.load("rasmlar/bg.png")
ground = pygame.image.load("rasmlar/ground.png")


# game_veraiables
ground_scroll = 0
scroll_speed = 4

run  = True
while run:
    
    clock.tick(fps)

    #background chizish
    screen.blit(bg, (0,0))
    #yerni chizish
    screen.blit(ground, (ground_scroll, 768))
    ground_scroll -= scroll_speed
    
    if abs(ground_scroll) > 35:
        ground_scroll = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
    
    
pygame.quit()

