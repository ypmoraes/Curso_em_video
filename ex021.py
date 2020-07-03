import pygame

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('e:/LOCAL/Betrayer/Metalik Klinik1-Anak Sekolah.mp3')
pygame.mixer.music.play()
pygame.event.wait()