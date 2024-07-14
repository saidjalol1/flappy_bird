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
pipe = pygame.image.load("rasmlar/pipe.png")
restart = pygame.image.load("rasmlar/restart.png")


bird_images = [
    pygame.image.load('rasmlar/bird1.png'),
    pygame.image.load('rasmlar/bird2.png'),
    pygame.image.load('rasmlar/bird3.png')
]

bird_index = 0
bird_rect = bird_images[0].get_rect()
bird_rect.center = (100, screen_height // 2)
bird_speed = 0
jump_velocity = -10
flying = False
game_over = False
# game_veraiables
ground_scroll = 0
scroll_speed = 4

run  = True
while run:
    
    clock.tick(fps)
    #Bird draw
    #background chizish
    screen.blit(bg, (0,0))
   
    #yerni chizish
    screen.blit(ground, (ground_scroll, 768))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONUP and flying == True:
            if event.button == 1:
                flying = True
                bird_speed = -10
        elif event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            if event.button == 1:
                flying = True
                
    if flying:        
        if bird_rect.y < 768:
            bird_rect.y += bird_speed
        bird_speed += 0.5
        if bird_speed > 8:
            bird_speed = 8
    
    if bird_rect.bottom > 768:
        game_over = True
        flying = False
        
    if game_over == False:
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0
            
    screen.blit(bird_images[bird_index], bird_rect)
    bird_index = (bird_index + 1) % len(bird_images)
    
        
    
    pygame.display.update()
    
    
pygame.quit()