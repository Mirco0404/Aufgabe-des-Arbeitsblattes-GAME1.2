import pygame                   # Stellt Objekte und Konstanten zur Spielprogrammierung zur Verfügung
import os
import random
import time

#-------------------------------------------Einstellungen-------------------------------------------#
class Settings(object):
    breite = 1000
    höhe = 800
    fps = 60
    bordersize = 0
    title = "Auftrag Nr.2" 
    file_path = os.path.dirname(os.path.abspath(__file__))
    images_path = os.path.join(file_path, "images")

#-------------------------------------------Klasse vom Objekt-------------------------------------------#
class Chest(pygame.sprite.Sprite):
    def __init__(self, pygame):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(Settings.images_path, "mcchest.png")).convert_alpha()     #Das Image wird in self.image gespeichert
        self.image = pygame.transform.scale(self.image, (110, 110))                                              #Das Image wird gescalet
        self.rect = self.image.get_rect()
        self.rect.centerx = Settings.breite // 2                                                            #Mitte der X-Achse
        self.rect.centery = Settings.höhe // 2                                                          #Mitte der Y-Achse
        self.speed = 5
        self.imagex = 110
        self.imagey = 110


    def update(self):
        keys = pygame.key.get_pressed()         #In keys wird die aktuelle Taste gespeichert welche gedrückt wird.

        if keys[pygame.K_UP]:
            self.rect.centery -= self.speed

        elif keys[pygame.K_DOWN]:
            self.rect.centery += self.speed

        elif keys[pygame.K_LEFT]:
            self.rect.centerx -= self.speed

        elif keys[pygame.K_RIGHT]:
            self.rect.centerx += self.speed


        if self.rect.right >= Settings.breite - Settings.bordersize:
            self.rect.right = Settings.breite - Settings.bordersize
            print("right border")
        elif self.rect.left <= Settings.bordersize:
            self.rect.left = Settings.bordersize
            print("left border")
        elif self.rect.top <= Settings.höhe - Settings.höhe + Settings.bordersize:
            self.rect.top = Settings.höhe - Settings.höhe + Settings.bordersize
            print("top border")
        elif self.rect.bottom >= Settings.höhe - Settings.bordersize:
            self.rect.bottom = Settings.höhe - Settings.bordersize
            print("bottom border")


    def respawn(self):
        self.rect.centerx = random.randrange(Settings.breite - self.imagex)
        self.rect.centery = random.randrange(Settings.höhe - self.imagey)


#-------------------------------------------Klasse damit das Spiel läuft-------------------------------------------#
class Game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((Settings.breite, Settings.höhe))
        pygame.display.set_caption(Settings.title)
        self.background = pygame.image.load(os.path.join(Settings.images_path, "background.png")).convert()         #Das Hintergrund Bild wird ausgwählt, gescalet und "gezeichnet".
        self.background = pygame.transform.scale(self.background, (Settings.breite, Settings.höhe))
        self.background_rect = self.background.get_rect()

#---------------------------------------------------------------------------------------------------

        self.all_Chest = pygame.sprite.Group()
        self.Chest = Chest(pygame)                          #Es wird eine Spritegruppe erstellt und ein Objekt erstellt aus der Klasse "Kirby". Dieses Objekt wird der neuen Spritegruppe hinzugefügt.
        self.all_Chest.add(self.Chest)

#---------------------------------------------------------------------------------------------------
        self.clock = pygame.time.Clock()
        self.done = False

    def run(self):
        while not self.done:
            self.clock.tick(Settings.fps)
            for event in pygame.event.get():                    #Event wird abgefragt, d.h. sobald das "X" betätigt wird, schließt sich das Fenster.
                if event.type == pygame.QUIT:
                    self.done = True
                elif event.type == pygame.KEYDOWN:              #Event wird abgefragt, d.h. sobald "ESC" betätigt wird, schließt sich das Fenster.
                    if event.key == pygame.K_ESCAPE:
                        self.done = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.Chest.respawn()




            self.screen.blit(self.background, self.background_rect)

            self.all_Chest.draw(self.screen)                                                    #Kirby wird gezeichnet
            self.all_Chest.update()


            pygame.display.flip()   # Aktualisiert das Fenster


if __name__ == '__main__':
                                    
    pygame.init()               # Bereitet die Module zur Verwendung vor  
    game = Game()
    game.run()

  
    pygame.quit()               # beendet pygame

