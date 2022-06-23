import pygame
import sys
import math 
import decimal
import time
import os
pygame.init()
screen = pygame.display.set_mode((1500, 850))
clock = pygame.time.Clock()
solarMass = 1.989 * math.pow(10, 30)
lightYear = 9.4607305 * math.pow(10, 15)
AU = 149_597_870_000
cwd = os.getcwd()
background = pygame.image.load(f"{cwd}\\PyGame Gravity\\textures\\background.jpg").convert_alpha()
background_rect = background.get_rect(topleft=(0, 0))
earth_ball = pygame.image.load(f"{cwd}\\PyGame Gravity\\textures\\earth.png").convert_alpha()
earth_ball_rect = earth_ball.get_rect(midtop=(1200, 200))
sun_ball = pygame.image.load(f"{cwd}\\PyGame Gravity\\textures\\sun.png").convert_alpha()
sun_ball_rect = sun_ball.get_rect(midtop=(250, 200))
class CelestialBody(): 
    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius
def gravcalc(m1, m2, r):
    G = 6.67 * math.pow(10, -11)
    F = ((G * m1 * m2) / math.pow(r, 2))
    return F

ton618 = CelestialBody(solarMass * 66000000000, 1.949 * math.pow(10, 14))
earth = CelestialBody(5.972 * math.pow(10, 24), 6371000)
sun = CelestialBody(solarMass, 696340000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    mouse_pos = pygame.mouse.get_pos()
    
    screen.blit(background, background_rect)
    screen.blit(earth_ball, earth_ball_rect)
    screen.blit(sun_ball, sun_ball_rect)
    
    distance = math.sqrt((sun_ball_rect.centerx-earth_ball_rect.centerx)**2 + (sun_ball_rect.centery-earth_ball_rect.centery)**2)
    print(gravcalc(66, 81, distance))
    
    earth_ball_rect.centerx -= gravcalc(10000000000000, 81, distance)
    sun_ball_rect.centerx -= -gravcalc(10000000000000, 81, distance)
    
    clock.tick(60)
    pygame.display.update()
    
    
    
