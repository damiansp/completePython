# Example code only; not executable
import pygame


NAME = 'Action Jackson'
ANTIALIAS = True
BKG_COLOR = 0, 0, 0 # None for transparent
TXT_COLOR = 255, 255, 255
FONT_SIZE_PX = 64


def main():
    pygame.init()
    # to see fonts available:
    print(pygame.font.get_fonts())
    font = pygame.font.SysFont('arial', FONT_SIZE_PX)
    #my_font = pygame.font.Font('myFont.tff', 16)
    name_surface = font.render(NAME, ANTIALIAS, BKG_COLOR, TXT_COLOR)
    pygame.image.save(name_surface, 'name.png')
    

if __name__ == '__main__':
    main()
