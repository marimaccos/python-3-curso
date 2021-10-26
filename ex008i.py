#faça um programa que abra e reproduza o audio de um arquivo mp3

import pygame

# Inicializando o mixer Pygame
pygame.mixer.init()

# Inicializando o Pygame
pygame.init()

pygame.mixer.music.load('fmaagain.mp3')
pygame.mixer.music.play()
pygame.event.wait()







