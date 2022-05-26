import pygame
from button import Button, Caption
from typename import typename
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
font_dir = path.join(path.dirname(__file__), 'arcadeclassic')
snd_dir = path.join(path.dirname(__file__), 'snd')


class Lose(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.message = Caption('YOU LOSE', 80, size[0] / 2, 300)
        self.image = pygame.transform.scale(pygame.image.load(path.join(img_dir, 'pause.png')).convert(), (400, 300))
        self.rect = self.image.get_rect()
        self.rect.center = (size[0] / 2, size[1] / 2)
        self.button_ex = Button((370, 50), 'EXIT', self.rect.centerx, self.rect.centery + 100, 50)
        # поменять размер
        self.button_rec = Button((370, 50), 'SAVE RECORD', self.rect.centerx, self.rect.centery + 20, 50)
        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.button_ex)
        self.captions = pygame.sprite.Group()
        self.captions.add(self.button_ex.caption)
        self.captions.add(self.message)


def lose(screen, is_score, wave):
    song = pygame.mixer.Sound(path.join(snd_dir, 'Quinton Sung-Exit Music (Radiohead 8-bit).mp3'))
    song.set_volume(0.1)
    song.play(loops=-1)
    print(screen.get_size())
    buttons = Lose(screen.get_size())
    if is_score:
        buttons.buttons.add(buttons.button_rec)
        buttons.captions.add(buttons.button_rec.caption)
    menu = pygame.sprite.Group()
    menu.add(buttons)
    running = True
    while running:
        xm, ym = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons.button_ex.rect.collidepoint((xm, ym)):
                    song.stop()
                    typename(screen, is_score, wave)
                    return True
                elif buttons.button_rec.rect.collidepoint((xm, ym)):
                    song.stop()
                    typename(screen, is_score, wave)
                    return True
            elif event.type == pygame.MOUSEMOTION:
                if buttons.button_ex.rect.collidepoint((xm, ym)):
                    buttons.button_ex.state(True)
                else:
                    buttons.button_ex.state(False)

        buttons.buttons.update()
        menu.draw(screen)
        buttons.buttons.draw(screen)
        buttons.captions.draw(screen)
        pygame.display.flip()
    pygame.quit()
