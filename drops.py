import pygame
import random


#COLOR
RED    = (255,  20,  20)
BLUE   = ( 20,  20, 255)
GREEN  = ( 20, 255,  20)
YELLOW = (255, 255,   0)
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)

class Drop:

    def __init__(self, x, y, color, wait):
        self.x = x
        self.y = y
        self.color = color
        self.wait = wait
        self.radius = 1

    def update(self, radinc):
        self.radius = self.radius + radinc

    def draw(self, window):
       pygame.draw.circle(window, self.color, (self.x, self.y), self.radius, 1)

def generate_drop():

    cirx = random.randint(1, 799)
    ciry = random.randint(1, 599)
    # colint = random.randint(1,5)
    # color = 0
    colint = 2  
    if colint == 1:
        color = RED
    if colint == 2:
        color = BLUE
    if colint == 3:
        color = GREEN
    if colint == 4:
        color = YELLOW
        
    return Drop(cirx, ciry, color, 0)

def main():
    clock = pygame.time.Clock()
    FPS = 120

    pygame.init()
    window = pygame.display.set_mode((800, 600))
    running = True

    wait_timer = 0


    dt = clock.tick()
    drops = []

    font = pygame.font.Font(None, 20)
    
    while running:

        if len(drops) == 0:
            drops.append(generate_drop())
                
        speed1 = 0
        wait_timer += dt

        speed1 = random.randint(1, 4)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        sep_time = random.randint(10, 30) * 1000

        if wait_timer > sep_time: # dt in ms
            drops.append(generate_drop())
            wait_timer = 0

        for drop in drops:
            drop.update(speed1)
            if drop.radius > 200:
                drops.pop(drops.index(drop))
            
            
        window.fill(BLACK)
        for drop in drops:
            drop.draw(window)
        
        display_fps = font.render("FPS: " + str(int(clock.get_fps())), True, WHITE)
        window.blit(display_fps, (740, 10))
            
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()