import pygame
import sys

class Runner():
    
class Game():
    corredores= []
    
    def __init__(self):
        self.__screen= pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de bichos")
        self.background=pygame.image.load("/home/lorenamh/Escritorio/keepcoding/Python/Python1/carreraPyGame/images/background.png")
        
        self.runner = pygame.image.load("images/fish.png")
        
    def    competir(self):
        x=0
        hayGanador = False
        
        while True:
            #COmprobacion de los eventos
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # para que no bloque la máquina
             #refrescar/renderizar la pantalla       
            self.__screen.blit(self.background,(0,0))
            self.__screen.blit(self.runner,(x,240))
            pygame.display.flip()
                    
            x +=3
            if x >= 250:
                hayGanador=True
                pygame.quit()
                sys.exit() 
        
if __name__ =='__main__':
    pygame.init()
    game=Game()
    game.competir()
    