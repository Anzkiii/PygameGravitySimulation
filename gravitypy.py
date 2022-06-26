import pygame
import sys
import math 
import decimal
import time
import os
pygame.init()
screen = pygame.display.set_mode((1500, 700))
clock = pygame.time.Clock()
solarMass = 1.989 * math.pow(10, 30)
earthMass = 5.972 * math.pow(10, 24)
lightYear = 9.4607305 * math.pow(10, 15)
AU = 149597870000
cwd = os.getcwd()
background = pygame.image.load(f"{cwd}\\textures\\background.jpg").convert_alpha()
background_rect = background.get_rect(topleft=(0, 0))
earth_ball = pygame.image.load(f"{cwd}\\textures\\earth.png").convert_alpha()
earth_ball_rect = earth_ball.get_rect(midtop=(1200, 250))

sun_ball = pygame.image.load(f"{cwd}\\textures\\sun.png").convert_alpha()
sun_ball_rect = sun_ball.get_rect(midtop=(250, 200))


class CelestialBody(): 
    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius
        
def gravcalc(m1, m2, r):
    G = 6.67 * math.pow(10, -11)
    F = ((G * m1 * m2) / math.pow(r, 2))
    return int(str(int(F)))

def get_centered_pos() -> pygame.Rect:
    return 

def vect(pos1, pos2):
    return pos1 - pos2

ton618 = CelestialBody(solarMass * 66000000000, AU * 1300)
earth = CelestialBody(earthMass, 6371000)
sun = CelestialBody(solarMass, 696340000)
x = 50
y = 60
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    mouse_pos = pygame.mouse.get_pos()
    
    screen.blit(background, background_rect)
    screen.blit(earth_ball, earth_ball_rect)
    screen.blit(sun_ball, sun_ball_rect)
    
    distance = math.sqrt((earth_ball_rect.centerx - sun_ball_rect.centerx)**2 + (earth_ball_rect.centery - sun_ball_rect.centery)**2)
    earthVect = pygame.math.Vector2(earth_ball_rect.x, earth_ball_rect.y)
    sunVect = pygame.math.Vector2(sun_ball_rect.x, sun_ball_rect.y)
    
    next_pos_vect = pygame.math.Vector2(*get_centered_pos())
    update_pos = next_pos_vect.move_towards(x, y, gravcalc(60, 80, 5))
    earthVect.x += update_pos[0] * abs(x - next_pos_vect.x) 
    earthVect.y += update_pos[1] * abs(y - next_pos_vect.y)
    clock.tick(60)
    pygame.display.update()
    