#Faça um programa em python que abra e reproduza
#o áudio de um arquivo mp3. 

import pygame
pygame.init #iniciar 

pygame.mixer.music.load('music.mp3')

pygame.mixer.music.play()

input()
pygame.event.wait() #esperar a musica acabar

# :)