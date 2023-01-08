import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('desafio021.MP3')
pygame.mixer.music.play()
pygame.event.wait(10000)
pygame.mixer.music.fadeout(5000)
pygame.event.wait(6000)
#parar = input('Digite qualquer coisa para parar!')
