import pygame

class Fighter():
    def __init__(self,x,y):
        self.rect = pygame.Rect((x,y,80,180))
        self.vel_y = 0
        self.jump = False
        self.tipo_ataque = 0
    
    #definiedo variable de movimiento
    def move_p1(self,Pantalla_Ancho,Pantalla_Alto,surface):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        
        #Presionar Tecla
        key = pygame.key.get_pressed()
        
        #Movimiento
        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED
        #Salto de Personaje
        if key[pygame.K_w] and self.jump==False:
            self.vel_y = -30
            self.jump = True
            
        #Ataque de Personajes
        if key[pygame.K_u] or key[pygame.K_i]:
            self.attack(surface)
            #Determinar el tipo de ataque
            if key[pygame.K_u]:
                self.tipo_ataque=1
            if key[pygame.K_i]:
                self.tipo_ataque=2
            
        #Gravedad del juego
        self.vel_y += GRAVITY
        dy += self.vel_y
            
        #Limitar Personaje a Pantalla
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > Pantalla_Ancho:
            dx = Pantalla_Ancho - self.rect.right
        if self.rect.bottom + dy > Pantalla_Alto - 50:
            self.vel_y = 0
            self.jump = False
            dy = Pantalla_Alto - 50 - self.rect.bottom
        
        #Actualizar Posicion
        self.rect.x += dx
        self.rect.y += dy
        
    #Player 2
    def move_p2(self,Pantalla_Ancho,Pantalla_Alto):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        
        #Presionar Tecla
        key = pygame.key.get_pressed()
        
        #Movimiento
        if key[pygame.K_LEFT]:
            dx = -SPEED
        if key[pygame.K_RIGHT]:
            dx = SPEED
        #Salto de Personaje
        if key[pygame.K_UP] and self.jump==False:
            self.vel_y = -30
            self.jump = True
            
        #Gravedad del juego
        self.vel_y += GRAVITY
        dy += self.vel_y
            
        #Limitar Personaje a Pantalla
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > Pantalla_Ancho:
            dx = Pantalla_Ancho - self.rect.right
        if self.rect.bottom + dy > Pantalla_Alto - 50:
            self.vel_y = 0
            self.jump = False
            dy = Pantalla_Alto - 50 - self.rect.bottom
        
        #Actualizar Posicion
        self.rect.x += dx
        self.rect.y += dy
        
    def attack(self,surface):
        attack_rec = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        pygame.draw.rect(surface, (0,0,255), attack_rec)
    
    #Crear Personaje
    def draw_p1(self,surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)
        
    def draw_p2(self,surface):
        pygame.draw.rect(surface, (0,255,0), self.rect)