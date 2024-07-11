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



class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f"rasmlar/bird{num}.png")
            self.images.append(img)
            
        self.image = pygame.image.load("rasmlar/bird1.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
    def update(self):
        #animatsiya
        self.counter += 1
        bird_down = 5
        
        if self.counter > bird_down:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]
        

bird_group = pygame.sprite.Group()
flappy = Bird(100, int(screen_height / 2))
bird_group.add(flappy)


# game_veraiables
ground_scroll = 0
scroll_speed = 4

run  = True
while run:
    
    clock.tick(fps)
    #Bird draw
    #background chizish
    screen.blit(bg, (0,0))
    bird_group.draw(screen)
    bird_group.update()
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