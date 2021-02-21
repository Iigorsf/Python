#Faça um programa em python que abra e reproduza o áudio de uma música no arquivo MP3#

import pygame
pygame.init()
pygame.mixer.music.load('paisdaganja.mp3')
pygame.mixer.music.play()
pygame.event.wait()

