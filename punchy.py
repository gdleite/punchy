import sys, pygame
import os
pygame.init()
screen = pygame.display.set_mode((518,454))
pygame.display.set_caption("Punch!")


#variaveis globais
tempo=0
vidamac=100
vidavon=100
controlevon=0
myfont = pygame.font.SysFont("monospace", 15)
esquiva=0

#carregar sprites 
ringue = pygame.image.load(os.path.join("bitmaps","ringue.png"))
w,h = ringue.get_size()
ringue = pygame.transform.scale(ringue, (w*2,h*2))

stand = pygame.image.load(os.path.join("bitmaps/mac","stand.png"))
w,h = stand.get_size()
stand = pygame.transform.scale(stand, (w*2,h*2))

predodgeesq = pygame.image.load(os.path.join("bitmaps/mac","predodge.png"))
w,h = predodgeesq.get_size()
predodgeesq = pygame.transform.scale(predodgeesq, (w*2,h*2))
predodgedir = pygame.transform.flip(predodgeesq, True, False)

dodgeesq = pygame.image.load(os.path.join("bitmaps/mac","dodge1.png"))
w,h = dodgeesq.get_size()
dodgeesq = pygame.transform.scale(dodgeesq, (w*2,h*2))

dodgedir = pygame.transform.flip(dodgeesq, True, False)

socoesq1 = pygame.image.load(os.path.join("bitmaps/mac","soco1.png"))
w,h = socoesq1.get_size()
socoesq1 = pygame.transform.scale(socoesq1, (w*2,h*2))

socoesq2 = pygame.image.load(os.path.join("bitmaps/mac","soco2.png"))
w,h = socoesq2.get_size()
socoesq2 = pygame.transform.scale(socoesq2, (w*2,h*2))

socoesq3 = pygame.image.load(os.path.join("bitmaps/mac","soco3.png"))
w,h = socoesq3.get_size()
socoesq3 = pygame.transform.scale(socoesq3, (w*2,h*2))

socodir1 = pygame.transform.flip(socoesq1, True, False)
socodir2 = pygame.transform.flip(socoesq2, True, False)
socodir3 = pygame.transform.flip(socoesq3, True, False)

#funcoes
def esquiva_esquerda():
    screen.blit(predodgeesq, (180,240))
    pygame.display.flip()
    pygame.time.delay(70)
    screen.fill((0, 0, 0))
    screen.blit(ringue, (0,0))
    screen.blit(dodgeesq, (160,240))
    pygame.display.flip()
    pygame.time.delay(350)
    
def esquiva_direita():
    screen.blit(predodgedir, (220,240))
    pygame.display.flip()
    pygame.time.delay(70)
    screen.fill((0, 0, 0))
    screen.blit(ringue, (0,0))
    screen.blit(dodgedir, (240,240))
    pygame.display.flip()
    pygame.time.delay(350)
    
def jabesquerdo():
    screen.blit(socoesq1, (220,240))
    pygame.display.flip()
    pygame.time.delay(90)
    screen.fill((0, 0, 0))
    screen.blit(ringue, (0,0))
    screen.blit(socoesq2, (230,200))
    pygame.display.flip()
    pygame.time.delay(70)
    screen.fill((0, 0, 0))
    screen.blit(ringue, (0,0))
    screen.blit(socoesq3, (240,160))
    pygame.display.flip()
    pygame.time.delay(150)
    
def jabdireito():
    screen.blit(socodir1, (220,240))
    pygame.display.flip()
    pygame.time.delay(90)
    screen.fill((0, 0, 0))
    screen.blit(ringue, (0,0))
    screen.blit(socodir2, (190,200))
    pygame.display.flip()
    pygame.time.delay(70)
    screen.fill((0, 0, 0))
    screen.blit(ringue, (0,0))
    screen.blit(socodir3, (180,160))
    pygame.display.flip()
    pygame.time.delay(150)
    
def idle():
    screen.blit(stand, (200,240))
    pygame.display.update()
    pygame.time.delay(20)

   
    
    
while True:
    controlevon+=1
    print(controlevon,esquiva)
    if controlevon==100:
        if esquiva==0:
            vidamac-=10
            controlevon=0
        else:
            controlevon=0
    if esquiva>0:
        esquiva+=1
    if esquiva ==30:
        esquiva=0
    print(esquiva)
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                esquiva_esquerda()
                esquiva=1
                
            elif event.key == pygame.K_RIGHT:
                esquiva_direita()
                esquiva=1
            elif event.key == pygame.K_z:
                jabesquerdo()
            elif event.key == pygame.K_x:
                jabdireito()
    idle()
                
        
    
    pygame.display.flip()
    screen.fill((0, 0, 0))
    screen.blit(ringue, (0,0))
    label = myfont.render(str(vidamac), 1, (255,255,0))
    screen.blit(label, (200, 200))
    pygame.display.flip()


