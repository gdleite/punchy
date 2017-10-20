import sys, pygame
import os
import random

#Inicializar pygame
pygame.init()
screen = pygame.display.set_mode((518,454))
pygame.display.set_caption("Punchy!")

#MENU LOOP
def menu():
    pass
    
def gameloop():
    #Variaveis Gameloop
    tempo=0
    vidamac=100
    vidavon=100
    controlevon=0 
    myfont = pygame.font.SysFont("monospace", 15)
    esquiva=0       #direcao da esquiva
    esquivacooldown=0
    punchcooldown=0
    standcontrol=0  #controle animaçao
    i=0
    direction="dir" #direcao soco

    #Variaveis Som
    somBackground = pygame.mixer.Sound("som/fight.wav")
    somSoco = pygame.mixer.Sound("som/punchmac.wav")
    somDodge = pygame.mixer.Sound("som/dodge.wav")
    somDodgeFail = pygame.mixer.Sound("som/dodgefail.wav")
    somSocoVon1 = pygame.mixer.Sound("som/punchvon.wav")
    somSocoVon2 = pygame.mixer.Sound("som/punchvon2.wav")
    somCharge = pygame.mixer.Sound("som/charge.wav")
    somBlock = pygame.mixer.Sound("som/block.wav")
    

    #Sprites gerais
    ringue = pygame.image.load(os.path.join("bitmaps","ringue.png"))
    w,h = ringue.get_size()
    ringue = pygame.transform.scale(ringue, (w*2,h*2))

    placar = pygame.image.load(os.path.join("bitmaps","placar.png"))
    w,h = placar.get_size()
    placar = pygame.transform.scale(placar, (w*2,h*2))

    #Sprites mac
    stand = pygame.image.load(os.path.join("bitmaps/mac","stand.png"))
    w,h = stand.get_size()
    stand = pygame.transform.scale(stand, (w*2,h*2))

    stand2 = pygame.image.load(os.path.join("bitmaps/mac","stand2.png"))
    w,h = stand2.get_size()
    stand2 = pygame.transform.scale(stand2, (w*2,h*2))

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

    punchedmacesq1 = pygame.image.load(os.path.join("bitmaps/mac","punchedmac1.png"))
    w,h = punchedmacesq1.get_size()
    punchedmacesq1 = pygame.transform.scale(punchedmacesq1, (w*2,h*2))

    punchedmacesq2 = pygame.image.load(os.path.join("bitmaps/mac","punchedmac2.png"))
    w,h = punchedmacesq2.get_size()
    punchedmacesq2 = pygame.transform.scale(punchedmacesq2, (w*2,h*2))

    punchedmacdir1 = pygame.transform.flip(punchedmacesq1, True, False)
    punchedmacdir2 = pygame.transform.flip(punchedmacesq2, True, False)

    #Sprites von
    idlevon1 = pygame.image.load(os.path.join("bitmaps/von","idlevon1.png"))
    w,h = idlevon1.get_size()
    idlevon1 = pygame.transform.scale(idlevon1, (w*2,h*2))

    idlevon2 = pygame.image.load(os.path.join("bitmaps/von","idlevon2.png"))
    w,h = idlevon2.get_size()
    idlevon2 = pygame.transform.scale(idlevon2, (w*2,h*2))

    socodirvon1 = pygame.image.load(os.path.join("bitmaps/von","socodir1.png"))
    w,h = socodirvon1.get_size()
    socodirvon1 = pygame.transform.scale(socodirvon1, (w*2,h*2))

    socodirvon2 = pygame.image.load(os.path.join("bitmaps/von","socodir2.png"))
    w,h = socodirvon2.get_size()
    socodirvon2 = pygame.transform.scale(socodirvon2, (w*2,h*2))

    socodirvon3 = pygame.image.load(os.path.join("bitmaps/von","socodir3.png"))
    w,h = socodirvon3.get_size()
    socodirvon3 = pygame.transform.scale(socodirvon3, (w*2,h*2))

    socodirvon4 = pygame.image.load(os.path.join("bitmaps/von","socodir4.png"))
    w,h = socodirvon4.get_size()
    socodirvon4 = pygame.transform.scale(socodirvon4, (w*2,h*2))

    socoesqvon1 = pygame.transform.flip(socodirvon1, True, False)
    socoesqvon2 = pygame.transform.flip(socodirvon2, True, False)
    socoesqvon3 = pygame.transform.flip(socodirvon3, True, False)
    socoesqvon4 = pygame.transform.flip(socodirvon4, True, False)

    punchedesqvon1 = pygame.image.load(os.path.join("bitmaps/von","punchedvon1.png"))
    w,h = punchedesqvon1.get_size()
    punchedesqvon1 = pygame.transform.scale(punchedesqvon1, (w*2,h*2))

    punchedesqvon2 = pygame.image.load(os.path.join("bitmaps/von","punchedvon2.png"))
    w,h = punchedesqvon2.get_size()
    punchedesqvon2 = pygame.transform.scale(punchedesqvon2, (w*2,h*2))

    puncheddirvon1 = pygame.transform.flip(punchedesqvon1, True, False)
    puncheddirvon2 = pygame.transform.flip(punchedesqvon2, True, False)

    scaredvon = pygame.image.load(os.path.join("bitmaps/von","scaredvon.png"))
    w,h = scaredvon.get_size()
    scaredvon = pygame.transform.scale(scaredvon, (w*2,h*2))

    blockVonDir = pygame.image.load(os.path.join("bitmaps/von","blockvondir.png"))
    w,h = blockVonDir.get_size()
    blockVonDir = pygame.transform.scale(blockVonDir, (w*2,h*2))

    blockVonEsq = pygame.transform.flip(blockVonDir, True, False)

    #ANIMAÇÕES
    def interface():
        screen.blit(ringue, (0,0))
        screen.blit(placar, (0,0))
        lifebarVon=96*vidavon/100
        lifebarMac=96*vidamac/100
        if lifebarVon<0:
            lifebarVon=0
        if lifebarMac<0:
            lifebarMac=0
        pygame.draw.rect(screen, (255,0,0),(180,36,lifebarMac,15),0)
        pygame.draw.rect(screen, (255,0,0),(292,36,lifebarVon,15),0)
    def esquiva_esquerda():
        screen.fill((0, 0, 0))
        interface()
        somDodge.play()
        screen.blit(socoesqvon3,(200,140))
        screen.blit(predodgeesq, (180,240))
        pygame.display.flip()
        pygame.time.delay(70)
        screen.fill((0, 0, 0))
        interface()
        screen.blit(socoesqvon4,(180,150))
        screen.blit(dodgeesq, (160,240))
        pygame.display.flip()
        pygame.time.delay(350)

    def missesquivaesquerda():
        screen.fill((0, 0, 0))
        interface()
        somDodgeFail.play()
        if controlevon>=110:
            screen.blit(socoesqvon1, (210,140))
        else:
            screen.blit(idlevon1, (210,140))
        screen.blit(predodgeesq, (180,240))
        pygame.display.flip()
        pygame.time.delay(70)
        screen.fill((0, 0, 0))
        interface()
        if controlevon>=110:
            screen.blit(socoesqvon2, (210,140))
        else:
            screen.blit(idlevon2, (210,140))
        screen.blit(dodgeesq, (160,240))
        pygame.display.flip()
        pygame.time.delay(350)
        
    def esquiva_direita():
        screen.fill((0, 0, 0))
        interface()
        somDodge.play()
        screen.blit(socodirvon3,(210,150))
        screen.blit(predodgedir, (230,240))
        pygame.display.flip()
        pygame.time.delay(70)
        screen.fill((0, 0, 0))
        interface()
        screen.blit(socodirvon4,(210,160))
        screen.blit(dodgedir, (250,240))
        pygame.display.flip()
        pygame.time.delay(350)

    def missesquivadireita():
        screen.fill((0, 0, 0))
        interface()
        somDodgeFail.play()
        if controlevon>=110:
            screen.blit(socodirvon1, (210,140))
        else:
            screen.blit(idlevon1, (210,140))
        screen.blit(predodgedir, (220,240))
        pygame.display.flip()
        pygame.time.delay(70)
        screen.fill((0, 0, 0))
        interface()
        if controlevon>=110:
            screen.blit(socodirvon1, (210,140))
        else:
            screen.blit(idlevon2, (210,140))
        screen.blit(dodgedir, (240,240))
        pygame.display.flip()
        pygame.time.delay(350)
        
    def jabesquerdo():
        screen.fill((0, 0, 0))
        interface()
        screen.blit(idlevon1, (210,140))
        screen.blit(socoesq1, (220,240))
        pygame.display.flip()
        pygame.time.delay(90)
        screen.fill((0, 0, 0))
        interface()
        screen.blit(puncheddirvon1, (220,130))
        screen.blit(socoesq2, (230,200))
        somSoco.play()
        pygame.display.flip()
        pygame.time.delay(70)
        screen.fill((0, 0, 0))
        interface()
        screen.blit(puncheddirvon2, (230,120))
        screen.blit(socoesq3, (240,160))
        pygame.display.flip()
        pygame.time.delay(150)
        
    def jabdireito():
        screen.fill((0, 0, 0))
        interface()
        screen.blit(idlevon1, (210,140))
        screen.blit(socodir1, (220,240))
        pygame.display.update()
        pygame.time.delay(90)
        screen.fill((0, 0, 0))
        interface()
        screen.blit(punchedesqvon1, (170,120))
        screen.blit(socodir2, (190,200))
        somSoco.play()
        pygame.display.update()
        pygame.time.delay(70)
        screen.fill((0, 0, 0))
        interface()
        screen.blit(punchedesqvon1, (160,110))
        screen.blit(socodir3, (180,160))
        pygame.display.update()
        pygame.time.delay(150)

    def jabEsquerdoBlock():
        screen.fill((0, 0, 0))
        interface()
        somBlock.play()
        screen.blit(idlevon1, (210,140))
        screen.blit(socoesq1, (220,240))
        pygame.display.flip()
        pygame.time.delay(90)
        screen.fill((0, 0, 0))
        interface()
        screen.blit(blockVonEsq, (215,120))
        screen.blit(socoesq2, (230,200))
        pygame.display.flip()
        pygame.time.delay(70)
        screen.fill((0, 0, 0))
        interface()
        screen.blit(blockVonEsq, (220,120))
        screen.blit(socoesq3, (240,160))
        pygame.display.flip()
        pygame.time.delay(150)

    def jabDireitoBlock():
        screen.fill((0, 0, 0))
        interface()
        somBlock.play()
        screen.blit(idlevon1, (210,140))
        screen.blit(socodir1, (220,240))
        pygame.display.flip()
        pygame.time.delay(90)
        screen.fill((0, 0, 0))
        interface()
        screen.blit(blockVonDir, (190,130))
        screen.blit(socodir2, (190,200))
        pygame.display.flip()
        pygame.time.delay(70)
        screen.fill((0, 0, 0))
        interface()
        screen.blit(blockVonDir, (180,120))
        screen.blit(socodir3, (180,160))
        pygame.display.flip()
        pygame.time.delay(150)
        
    def punchedesq():
        screen.fill((0, 0, 0))
        interface()
        somSocoVon2.play()
        somSocoVon1.play()
        screen.blit(socoesqvon3,(200,140))
        screen.blit(punchedmacesq1, (240,250))
        pygame.display.flip()
        pygame.time.delay(140)
        screen.fill((0, 0, 0))
        interface()
        screen.blit(socoesqvon4,(180,150))
        screen.blit(punchedmacesq2, (260,260))
        pygame.display.flip()
        pygame.time.delay(350)

    def puncheddir():
        screen.fill((0, 0, 0))
        interface()
        somSocoVon2.play()
        somSocoVon1.play()
        screen.blit(socodirvon3,(210,150))
        screen.blit(punchedmacdir1, (170,250))
        pygame.display.update()
        pygame.time.delay(140)
        screen.fill((0, 0, 0))
        interface()
        screen.blit(socodirvon4,(210,160))
        screen.blit(punchedmacdir2, (150,260))
        pygame.display.update()
        pygame.time.delay(350)
        
    def idle(i,controlevon,direction):
        listavon=[idlevon1,idlevon2]
        listamac=[stand,stand2]
        listachargesesq=[socoesqvon1,socoesqvon2]
        listachargesdir=[socodirvon1,socodirvon2]
        # Preparacao Von
        if controlevon < 0:
            screen.blit(scaredvon, (210,140))
        elif controlevon<110:
            screen.blit(listavon[i], (210,140))
        else:
            if direction == "dir":
                screen.blit(listachargesdir[i], (210,140))
            if direction == "esq":
                screen.blit(listachargesesq[i], (210,140))
        screen.blit(listamac[i], (200,240))
        pygame.time.delay(20)

        
    #FUNÇÕES GAMELOOP
    def punchdirection():
        directions=["esq","dir"]
        x=random.randint(0,1)
        return directions[x]
    
    #GAMELOOP
    somBackground.play()
    while True:
        #eventos
        if controlevon==0:
            multiply=1
        if controlevon>=0:
            controlevon += 1
        elif controlevon < 0:
            controlevon-=1
        if controlevon <= -40:
                controlevon=0
        
        if controlevon%10==0:
            print("controlevon: ",controlevon,"esquiva: ",esquiva,"cooldown: ",esquivacooldown,"idle: ",standcontrol)

        if controlevon==99:
            direction = punchdirection()
            somCharge.play()

        if controlevon == 150:
            if direction == "dir" and esquiva<=0:
                print("levou soco na", direction )
                esquiva=0
                vidamac-=10*multiply
                controlevon=0
                puncheddir()
                
            elif direction == "esq" and esquiva>=0:
                print("levou soco na", direction )
                esquiva=0
                vidamac-=10*multiply
                controlevon=0
                punchedesq()
                
            else:
                print("esquivou se do soco na", direction)
                

        #Controle Esquiva    
        if esquivacooldown>0:
            esquivacooldown-=1        
        if esquiva>0:
            esquiva+=1
            esquivacooldown=50
        if esquiva<0:
            esquiva-=1
            esquivacooldown=50
        if esquiva == 30:
            esquiva=0
        if esquiva == -30:
            esquiva = 0

        #Controle Socos
        if punchcooldown>0:
            punchcooldown-=1
        
        
        # Eventos teclado
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                    pygame.quit()
                    
            if event.type == pygame.KEYDOWN:
                
                    
                if event.key == pygame.K_LEFT and esquivacooldown==0:
                    esquivacooldown=50
                    if controlevon>110 and direction=="dir":
                        esquiva_esquerda()
                        esquiva=1
                        controlevon=-1
                    else:
                        missesquivaesquerda()
                    
                    
                elif event.key == pygame.K_RIGHT and esquivacooldown==0:
                    esquivacooldown=50
                    if controlevon>110 and direction=="esq":
                        esquiva_direita()
                        esquiva = -1
                        controlevon=-1
                        
                    else:
                        missesquivadireita()

                    
                elif event.key == pygame.K_z and punchcooldown==0:
                    punchcooldown=5
                    if controlevon<0:
                        jabesquerdo()
                        vidavon-=5
                    else:
                        jabEsquerdoBlock()
                        multiply+=1
                        
                        
                    
                elif event.key == pygame.K_x and punchcooldown==0:
                    punchcooldown=5
                    if controlevon<0:
                        jabdireito()
                        vidavon-=5
                     
                    else:
                        jabDireitoBlock()
                        multiply+=1
        
                    
            
        
        pygame.display.flip()
        screen.fill((0, 0, 0))
        interface()
        idle(i,controlevon,direction)
        standcontrol+=1
        if standcontrol>12 and i==0:
            i=1
            standcontrol=0
        if standcontrol>12 and i==1:
            i=0
            standcontrol=0
        label = myfont.render(str(vidamac), 1, (255,255,0))
        label2 = myfont.render(str(vidavon), 1, (255,255,0))
        screen.blit(label, (30, 40))
        screen.blit(label2, (130, 40))
        pygame.display.flip()
gameloop()

