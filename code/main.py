#imports
import pygame

running = True

pygame.init()

print("Main Running")

events = pygame.event.get()

keys = pygame.key.get_pressed()

while running:
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = False

pygame.quit