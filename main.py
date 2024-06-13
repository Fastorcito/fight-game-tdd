import pygame
from Pelea import Fighter

pygame.init()

#Parametros de Pantalla
Pantalla_Ancho = 1820
Pantalla_Alto = 880

#Creación de la Pantalla
Pantalla = pygame.display.set_mode((Pantalla_Ancho,Pantalla_Alto))
pygame.display.set_caption("Brawler")

#delimitar FPS
clock = pygame.time.Clock()
fps = 60

#fondo del inicio
bg_image = pygame.image.load("Assets/Maps/BG_1.jpg").convert_alpha()

#Funcion para poner Background
def draw_bg():
    #adaptar la imagen a la pantalla
    scaled_bg = pygame.transform.scale(bg_image, (Pantalla_Ancho,Pantalla_Alto))
    Pantalla.blit(scaled_bg, (0,0))
    
#Instancias para los peleadores
Fighter_1 = Fighter(400,650)
Fighter_2 = Fighter(1200,650)

#Game Loop
run = True
while run:
    
    clock.tick(fps)
    
    #llamar funcion background
    draw_bg()
    
    #Mover Personajes
    Fighter_1.move_p1(Pantalla_Ancho,Pantalla_Alto,Pantalla)
    Fighter_2.move_p2(Pantalla_Ancho,Pantalla_Alto)
    
    #Poner a los Peleadores
    Fighter_1.draw_p1(Pantalla)
    Fighter_2.draw_p2(Pantalla)
    
    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    #Actualizar pantalla
    pygame.display.update()

#terminate game
pygame.quit()