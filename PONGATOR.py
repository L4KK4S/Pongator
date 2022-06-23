import pygame, sys
import time
from math import sqrt
from random import choice
from pygame import mixer

def jeu(tempsdejeu, playerone, playertwo):
    
    tps = tempsdejeu
    
    mixer.init()
    mixer.music.load("tetris-theme-officiel.wav")
    mixer.music.set_volume(0.9)
    mixer.music.play()
    
    def distance(x1,y1,x2,y2):
        return sqrt((x2-x1)**2+(y2-y1)**2)
    
    class Balle:
        
        def __init__(self):
            self.abscisse=choice([LARGEUR-200, 200])
            self.ordonnee=HAUTEUR//2+100
            self.vitesse=[0, 0] 
        
        def dessinerballe(self):
            pygame.draw.circle(fenetre,(250,250,250),(self.abscisse,self.ordonnee),10)
        
        def bouger(self):
            self.abscisse=self.abscisse + self.vitesse[0]
            self.ordonnee=self.ordonnee + self.vitesse[1]
            if self.ordonnee-20 < 100 or self.ordonnee+20 > HAUTEUR :
                self.vitesse[1]=self.vitesse[1]*-1
    
        
        def but(self, j, j0):
            if self.abscisse+20 > LARGEUR:
                self.vitesse=[0,0]
                self.abscisse=LARGEUR-200
                self.ordonnee=HAUTEUR//2+100
                p.scorej1()
                j.coord=[LARGEUR//2+450, HAUTEUR//2+75]
                j0.coord=[LARGEUR//2-450, HAUTEUR//2+75]
            if self.abscisse-20 < 0 :
                self.vitesse=[0,0]
                self.abscisse=200
                self.ordonnee=HAUTEUR//2+100
                p.scorej2()
                j.coord=[LARGEUR//2+450, HAUTEUR//2+75]
                j0.coord=[LARGEUR//2-450, HAUTEUR//2+75]
    
        def acceleration(self):
            if self.vitesse[0]<0:
                self.vitesse[0]=self.vitesse[0]-1
                print("-1")
            else:
                self.vitesse[0]=self.vitesse[0]+1
                print("+1")
            if self.vitesse[1]<0:
                self.vitesse[1]=self.vitesse[1]-1
                print("-1")
            else:
                self.vitesse[1]=self.vitesse[1]+1
                print("+1")
            
            
    class Pong:
        
        def __init__(self):
            self.scorep1=0
            self.scorep2=0
        
        def scorej1(self):
            self.scorep1+=1
            
        def scorej2(self):
            self.scorep2+=1
            
    class Joueur:
        
        def __init__(self, x, y, couleur):
            self.coord=[x, y]
            self.couleur=couleur
            
        def dessinerbar(self):
            pygame.draw.rect(fenetre,self.couleur,((self.coord[0],self.coord[1]),(7, 75 )))
                        
        def bas(self):
            self.coord[1]+=10
            
        def haut(self):
            self.coord[1]-=10
            
        def gauche(self):
            self.coord[0]-=10
            
        def droite(self):
            self.coord[0]+=10
            
        def sortir(self, other, ab, ab2):
            if self.coord[0]<5 or LARGEUR//2+40>self.coord[0]>LARGEUR//2:
                self.coord[0]+=10
            if self.coord[1]-5<100:
                self.coord[1]+=10
            if self.coord[1]+75>HAUTEUR:
                self.coord[1]-=10
            if self.coord[0]>LARGEUR-20 or LARGEUR//2-50<self.coord[0]<LARGEUR//2:
                self.coord[0]-=10
            for i in range(75):
                if distance(self.coord[0]+ab, self.coord[1]+i, other.abscisse, other.ordonnee)<10:
                    if self==j2:
                        self.coord[0]-=3
                    if self==j1:
                        self.coord[0]+=3
                if distance(self.coord[0]+ab2, self.coord[1]+i, other.abscisse, other.ordonnee)<10:
                    if self==j2:
                        self.coord[0]+=3
                    if self==j1:
                        self.coord[0]-=3
                    
        def rebond(self, other, ab):
            for i in range(80):
                if other.abscisse>LARGEUR//2:
                    if distance(self.coord[0]+ab, self.coord[1]+i, other.abscisse, other.ordonnee)<10:
                        other.vitesse[0]=other.vitesse[0]*-1
                if other.abscisse<LARGEUR//2:
                    if distance(self.coord[0]+ab, self.coord[1]+i, other.abscisse, other.ordonnee)<10:
                        other.vitesse[0]=sqrt(other.vitesse[0]**2)
        
        def depart(self, other, ab, neg):
            for i in range(75):
                if distance(self.coord[0]+ab, self.coord[1]+i, other.abscisse, other.ordonnee)<11:
                    other.vitesse=[2*-neg, 2]
                    
    LARGEUR = 1100
    HAUTEUR = 700
    
    pygame.display.init()
    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))  # pour définir les dimensions de la fenêtre
    fenetre.fill([0,0,0])  # pour colorier le fond avec une couleur
    
    temps=time.time()
    continuer = True
    p=Pong()
    b=Balle()
    j1=Joueur(LARGEUR//2+450, HAUTEUR//2+75,(0, 0, 255))
    j2=Joueur(LARGEUR//2-450, HAUTEUR//2+75,(255, 0, 0))
    fpsClock = pygame.time.Clock()
    TpsZero = pygame.time.get_ticks()
    
    while continuer:
        seconds =str(tps - int(round((pygame.time.get_ticks() - TpsZero) / 1000,0)))
        
        mixer.music.play(-1)
    
        fenetre.fill([0, 0, 0])
        pygame.draw.rect(fenetre,(255, 255, 255),((0, 97),(LARGEUR, 6)))
    
        pygame.draw.rect(fenetre,(255, 255, 255),((LARGEUR // 2 - 6, 100),(6, HAUTEUR - 100)))
    
        pygame.draw.rect(fenetre,(255, 255, 255),((450, 0 ),(200,100 )), 1)
    
        pygame.draw.rect(fenetre,(255, 0, 0),((0, 103),(5, 600 )))
    
        pygame.draw.rect(fenetre,(0, 0, 255),((1095, 103),(5, 600 )))
    
        
        pygame.init()
        myfont = pygame.font.Font("minecraft.ttf", 50)
        image_texte = myfont.render ( playerone, 1 , (255,0,0) )
        fenetre.blit(image_texte, (100 , 25))
        image_texte = myfont.render ( str(p.scorep1), 1 , (255,0,0) )
        fenetre.blit(image_texte, (30 , 25))
        pygame.draw.rect(fenetre,(255, 0, 0),((90, 0),(5, 97 )))
    
        image_texte = myfont.render ( playertwo, 1 , (0,0,255) )
        fenetre.blit(image_texte, (675 , 25))
        image_texte = myfont.render ( str(p.scorep2), 1 , (0,0,255) )
        fenetre.blit(image_texte, (1045 , 25))
        pygame.draw.rect(fenetre,(0, 0, 255),((1015, 0),(5, 97 )))
    
    
        image_texte = myfont.render ( seconds, 1 , (255, 255, 255) )
    
        fenetre.blit(image_texte, (520 , 25))
        # construction de la balle dans la fenetre
        b.dessinerballe()
        
        # construction des raquettes dans la fenetre
        j1.dessinerbar()
        j2.dessinerbar()
        
        # déplacement de la balle
        b.bouger()
        j1.rebond(b, 0)
        j2.rebond(b, 7)
        b.but(j1, j2)
        
        if b.vitesse[0]==0:
            j1.depart(b, 0, 1,)
            j2.depart(b, 7, -1,)
        
        if b.vitesse!=[0, 0]:
            if time.time()-temps>7: 
                temps=time.time()
                b.acceleration()
        else:
            temps=time.time()
        # mise à jour de la fenêtre
        pygame.display.update()
        
        # routine pour pouvoir quiter la boucle while
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # lorsqu'on clique sur la croix de la fenêtre       
                continuer = False
                mixer.music.stop()
            
        # déplacement de la raquette
        keys=pygame.key.get_pressed()
        
        
        if keys[pygame.K_UP]:
            j1.haut()
        if keys[pygame.K_DOWN]:
            j1.bas()
        if keys[pygame.K_LEFT]:
            j1.gauche()
        if keys[pygame.K_RIGHT]:
            j1.droite()
        if keys[pygame.K_z]:
            j2.haut()
        if keys[pygame.K_s]:
            j2.bas()
        if keys[pygame.K_q]:
            j2.gauche()
        if keys[pygame.K_d]:
            j2.droite()
        j1.sortir(b, 0, 7)
        j2.sortir(b, 7, 0)
        # temps de pause à ajuster
        
        if int(seconds) <= 0:
          continuer = False
          mixer.music.stop()
          myfont = pygame.font.Font("minecraft.ttf", 75)
          pygame.draw.rect(fenetre,(0, 0, 0),((300, 350),(500, 125)))
          if p.scorep1 == p.scorep2:
            image_texte = myfont.render ( "DRAW", 1 , (255,255,255) )
            fenetre.blit(image_texte, (400 , 370))
            pygame.display.update()
          if p.scorep1 < p.scorep2:
            image_texte = myfont.render ( playertwo + " WON", 1 , (255,255,255) )
            fenetre.blit(image_texte, (250 , 370))
            pygame.display.update()
          if p.scorep1 > p.scorep2:
            image_texte = myfont.render ( playerone + " WON", 1 , (255,255,255) )
            fenetre.blit(image_texte, (250 , 370))
            pygame.display.update()
          time.sleep(5)
    
    
        time.sleep(0.005)
    
    
    # Fermeture de la fenêtre (qui a donc lieu si on quitte la boucle while)
    
    pygame.display.quit()
    sys.exit()
    mixer.music.stop()

LARGEUR = 1100
HAUTEUR = 700

ch = 90
j1 = "PLAYERONE"
j2 = "PLAYERTWO"

mixer.init()
mixer.music.load("dbs.wav")
mixer.music.set_volume(0.9)
mixer.music.play(-1)

pygame.display.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))  # pour définir les dimensions de la fenêtre
fenetre.fill([0,0,0]) 

pygame.init()

myfont = pygame.font.Font("minecraft.ttf", 100)
image_texte = myfont.render ( "PONGATOR", 1 , (255,255,255) )
fenetre.blit(image_texte, (290 , 100))

myfont = pygame.font.Font("minecraft.ttf", 70)

image_texte = myfont.render ( "PLAY", 1 , (255,255,255) )
fenetre.blit(image_texte, (400 , 300))
image_texte = myfont.render ( "OPTIONS", 1 , (255,255,255) )
fenetre.blit(image_texte, (400 , 370))


pygame.draw.polygon(fenetre, (255, 255, 255), [(370, 305),(370,335), (390,320) ])

pygame.display.update()

endroit = "play"   
# routine pour pouvoir quiter la boucle while
for event in pygame.event.get(): 
    if event.type == pygame.QUIT:
        continuer = False
        pygame.display.quit()
        sys.exit()
        mixer.music.stop()
continuer = True
while continuer:
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pygame.draw.polygon(fenetre, (0, 0, 0), [(370, 375),(370,405), (390,390)])
        pygame.draw.polygon(fenetre, (255, 255, 255), [(370, 305),(370,335), (390,320) ])
        pygame.display.update()
        endroit = "play"
    if keys[pygame.K_DOWN]:
        pygame.draw.polygon(fenetre, (0, 0, 0), [(370, 305),(370,335), (390,320) ])
        pygame.draw.polygon(fenetre, (255, 255, 255), [(370, 375),(370,405), (390,390)])
        pygame.display.update()
        endroit = "options"
    if keys[pygame.K_RETURN]:
        print(endroit)
        if endroit == "play":
            mixer.music.stop()
            jeu(ch, j1, j2)
    if keys[pygame.K_RETURN]:
        print(endroit)
        if endroit == "options":
            LARGEUR = 1100
            HAUTEUR = 700
            ch = "90"
            p1 = "playerone"
            p2 = "playertwo"
            
            pygame.display.init()
            fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))  # pour définir les dimensions de la fenêtre
            fenetre.fill([0,0,0]) 
            
            
            
            myfont = pygame.font.Font("minecraft.ttf", 100)
            
            image_texte = myfont.render ( "OPTIONS", 1 , (255,255,255) )
            fenetre.blit(image_texte, (350 , 80))
            
            
            myfont = pygame.font.Font("minecraft.ttf", 50)
            
            image_texte = myfont.render ( "Time", 1 , (255,255,255) )
            fenetre.blit(image_texte, (200 , 250))
            image_texte = myfont.render ( ch, 1 , (255,255,255) )
            fenetre.blit(image_texte, (230 , 300))
            pygame.draw.polygon(fenetre, (255, 255, 255), [(330, 260),(330,290), (350,275) ])
            pygame.draw.polygon(fenetre, (255, 255, 255), [(180, 260),(180,290), (160,275) ])
            
            image_texte = myfont.render ( "P1 name", 1 , (255,255,255) )
            fenetre.blit(image_texte, (400 , 250))
            image_texte = myfont.render ( p1 , 1 , (255,255,255) )
            fenetre.blit(image_texte, (420 , 300))
            pygame.draw.rect(fenetre,(255, 255, 255),((610, 250),(40, 40)))
            
            
            
            image_texte = myfont.render ( "P2 name", 1 , (255,255,255) )
            fenetre.blit(image_texte, (700 , 250))
            image_texte = myfont.render ( p2 , 1 , (255,255,255) )
            fenetre.blit(image_texte, (720 , 300))
            pygame.draw.rect(fenetre,(255, 255, 255),((910, 250),(40, 40)))
            
            
            myfont = pygame.font.Font("minecraft.ttf", 15)
            image_texte = myfont.render ( "NEW", 1 , (0,0,0) )
            fenetre.blit(image_texte, (615 , 265))
            image_texte = myfont.render ( "NEW", 1 , (0,0,0) )
            fenetre.blit(image_texte, (915 , 265))
            
            
            myfont = pygame.font.Font("minecraft.ttf", 70)
            image_texte = myfont.render ( "PLAY", 1 , (255,255,255) )
            fenetre.blit(image_texte, (450 , 450))
              
            pygame.display.update()
            
            continuer = True 
            while continuer :
                keys=pygame.key.get_pressed()
                if keys[pygame.K_DOWN]:
                  pygame.draw.polygon(fenetre, (255, 255, 255), [(410, 450),(410,490), (440,470) ])
                  pygame.display.update()
                  endroit ="play2"
                if keys[pygame.K_RETURN] and endroit == "play2":
                  mixer.music.stop()
                  jeu(int(ch),p1,p2)
                ev = pygame.event.get()
                for event in ev:
                  if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    if 610<=pos[0]<=650 and 250<=pos[1]<=290:
                      qu1 = input("what is the new name ?")
                      p1 = qu1
                      pygame.draw.rect(fenetre,(0, 0, 0),((420, 300),(300, 50)))
                      image_texte = myfont.render ( p1 , 1 , (255,255,255) )
                      fenetre.blit(image_texte, (420 , 300))
                      pygame.display.update()
                    if 910<=pos[0]<=950 and 250<=pos[1]<=290:
                      qu2 = input("what is the new name ?")
                      p2 = qu2
                      pygame.draw.rect(fenetre,(0, 0, 0),((720, 300),(300, 50)))
                      image_texte = myfont.render ( p2 , 1 , (255,255,255) )
                      fenetre.blit(image_texte, (720 , 300))
                      pygame.display.update()
                    if 330<=pos[0]<=350 and 260<=pos[1]<=290:
                      if int(ch)<120 : 
                          ch = str(int(ch) + 10)
                          print(ch)
                          pygame.draw.rect(fenetre,(0, 0, 0),((230, 300),(90, 50 )))
                          image_texte = myfont.render ( ch, 1 , (255,255,255) )
                          fenetre.blit(image_texte, (230 , 300))
                          pygame.display.update()
                    if 160<=pos[0]<=180 and 260<=pos[1]<=290:
                      if 30<int(ch): 
                          ch = str(int(ch) - 10)
                          print(ch)
                          pygame.draw.rect(fenetre,(0, 0, 0),((230, 300),(90, 50 )))
                          image_texte = myfont.render ( ch, 1 , (255,255,255) )
                          fenetre.blit(image_texte, (230 , 300))
                          pygame.display.update()
                for event in ev:
                    if event.type == QUIT:
                        continuer = False
                        pygame.mixer.music.stop()
                        pygame.display.quit()
                        sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # si croix, fermer la page
            continuer = False
            pygame.mixer.music.stop()
            pygame.display.quit()
            sys.exit()