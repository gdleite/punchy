import sys, pygame
import os
import random
import math

#Inicializar pygame
pygame.init()
screen = pygame.display.set_mode((513,454))
pygame.display.set_caption("Punchy!!")

#Som Menu
somMenu = pygame.mixer.Sound("som/menu.wav")
somMenu.play()

#MENU LOOP
def menu():
    #Variaveis Menu
    lista=["0","1","2"]
    luvaPos=0
    #Sprites Menu
    title = pygame.image.load(os.path.join("bitmaps","title.png"))
    w,h = title.get_size()
    title = pygame.transform.scale(title, (w*2,h*2))
    
    luva = pygame.image.load(os.path.join("bitmaps","luva.png"))
    w,h = luva.get_size()
    luva = pygame.transform.scale(luva, (w*2,h*2))

    #Som Menu
    somSelectMenu = pygame.mixer.Sound("som/menuselect.wav")

    #Menu Loop
    
    while True:
        screen.blit(title, (0,0))

        #luva
        if luvaPos>2:
            luvaPos=0
        if luvaPos<0:
            luvaPos=2
        if luvaPos==0:
            screen.blit(luva, (150,300))
        elif luvaPos==1:
            screen.blit(luva, (120,345))
        else:
            screen.blit(luva, (100,385))
        pygame.display.flip()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                    pygame.quit()        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    luvaPos-=1
                    somSelectMenu.play()
                if event.key == pygame.K_DOWN:
                    luvaPos+=1
                    somSelectMenu.play()
                if event.key == pygame.K_z:
                    if lista[luvaPos]=="0":
                        somMenu.stop()
                        gameloop()
                    elif lista[luvaPos]=="1":
                        ranking()
                    else:
                        comoJogar()
def comoJogar():
    #Sprites Ranking
    imagem = pygame.image.load(os.path.join("bitmaps","tutorial.png"))
    
    luva = pygame.image.load(os.path.join("bitmaps","luva.png"))
    w,h = luva.get_size()
    luva = pygame.transform.scale(luva, (w*2,h*2))
    

    #Som
    somSelectMenu = pygame.mixer.Sound("som/menuselect.wav")
    while True:
        screen.fill((0,0,0))
        screen.blit(imagem, (0,0))
        screen.blit(luva, (80,390))          
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    somSelectMenu.play()
                    menu()
def derrota():
    #Sprites tela derrota
    telaDerrota = pygame.image.load(os.path.join("bitmaps","derrota.png"))
    luva = pygame.image.load(os.path.join("bitmaps","luva.png"))
    w,h = luva.get_size()
    luva = pygame.transform.scale(luva, (w*2,h*2))

    #Som tela de derrota
    somDerrota = pygame.mixer.Sound("som/lose.wav")
    somSelectMenu = pygame.mixer.Sound("som/menuselect.wav")

    #loop
    somDerrota.play()
    lista=["0","1"]
    luvaPos=1
    while True:
        screen.fill((0, 0, 0))
        screen.blit(telaDerrota, (0,0))
        #luva
        if luvaPos>1:
            luvaPos=0
        if luvaPos<0:
            luvaPos=1
        if luvaPos==0:
            screen.blit(luva, (90,370))
        elif luvaPos==1:
            screen.blit(luva, (310,370))
        pygame.display.flip()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        luvaPos-=1
                        somSelectMenu.play()
                    if event.key == pygame.K_RIGHT:
                        luvaPos+=1
                        somSelectMenu.play()
                    if event.key == pygame.K_RETURN or event.key == pygame.K_z:
                        if lista[luvaPos]=="0":
                            gameloop()
                        else:
                            menu()
        
    
def victory(pontos):
    #Sprites tela vitoria
    telaVitoria = pygame.image.load(os.path.join("bitmaps","vitoria.png"))

    luva = pygame.image.load(os.path.join("bitmaps","luva.png"))
    w,h = luva.get_size()
    luva = pygame.transform.scale(luva, (w*2,h*2))

    #Som tela de vitoria
    somVitoria = pygame.mixer.Sound("som/win.wav")
    somSelectMenu = pygame.mixer.Sound("som/menuselect.wav")
    

    #Loop
    cond=False
    nome=""
    fonte = pygame.font.Font("fonte/emulogic.ttf", 16)
    pts = fonte.render(str(pontos), 1, (255,255,255))
    somVitoria.play()
    lista=["0","1"]
    luvaPos=1
    while True:
        letras = fonte.render(str(nome), 1, (255,255,255))
        screen.fill((0, 0, 0))
        screen.blit(telaVitoria, (0,0))
        screen.blit(pts,(270,170))
        screen.blit(letras,(230,206))
        #luva
        if luvaPos>1:
            luvaPos=0
        if luvaPos<0:
            luvaPos=1
        if luvaPos==0:
            screen.blit(luva, (90,385))
        elif luvaPos==1:
            screen.blit(luva, (300,385))
        pygame.display.flip()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        luvaPos-=1
                        somSelectMenu.play()
                    if event.key == pygame.K_RIGHT:
                        luvaPos+=1
                        somSelectMenu.play()
                    if event.key == pygame.K_a and len(nome)<11:
                        nome+="a"
                        somSelectMenu.play()
                    if event.key == pygame.K_b and len(nome)<11:
                        nome+="b"
                        somSelectMenu.play()
                    if event.key == pygame.K_c and len(nome)<11:
                        nome+="c"
                        somSelectMenu.play()
                    if event.key == pygame.K_d and len(nome)<11 :
                        nome+="d"
                        somSelectMenu.play()
                    if event.key == pygame.K_e and len(nome)<11:
                        nome+="e"
                        somSelectMenu.play()
                    if event.key == pygame.K_f and len(nome)<11:
                        nome+="f"
                        somSelectMenu.play()
                    if event.key == pygame.K_g and len(nome)<11:
                        nome+="g"
                        somSelectMenu.play()
                    if event.key == pygame.K_h and len(nome)<11:
                        nome+="h"
                        somSelectMenu.play()
                    if event.key == pygame.K_i and len(nome)<11:
                        nome+="i"
                        somSelectMenu.play()
                    if event.key == pygame.K_j and len(nome)<11:
                        nome+="j"
                        somSelectMenu.play()
                    if event.key == pygame.K_k and len(nome)<11:
                        nome+="k"
                        somSelectMenu.play()
                    if event.key == pygame.K_l and len(nome)<11:
                        nome+="l"
                        somSelectMenu.play()
                    if event.key == pygame.K_m and len(nome)<11:
                        nome+="m"
                        somSelectMenu.play()
                    if event.key == pygame.K_n and len(nome)<11:
                        nome+="n"
                        somSelectMenu.play()
                    if event.key == pygame.K_o and len(nome)<11:
                        nome+="o"
                        somSelectMenu.play()
                    if event.key == pygame.K_p and len(nome)<11:
                        nome+="p"
                        somSelectMenu.play()
                    if event.key == pygame.K_q and len(nome)<11:
                        nome+="q"
                        somSelectMenu.play()
                    if event.key == pygame.K_r and len(nome)<11:
                        nome+="r"
                        somSelectMenu.play()
                    if event.key == pygame.K_s and len(nome)<11:
                        nome+="s"
                        somSelectMenu.play()
                    if event.key == pygame.K_t and len(nome)<11:
                        nome+="t"
                        somSelectMenu.play()
                    if event.key == pygame.K_u and len(nome)<11:
                        nome+="u"
                        somSelectMenu.play()
                    if event.key == pygame.K_v and len(nome)<11:
                        nome+="v"
                        somSelectMenu.play()
                    if event.key == pygame.K_w and len(nome)<11:
                        nome+="w"
                        somSelectMenu.play()
                    if event.key == pygame.K_x and len(nome)<11:
                        nome+="x"
                        somSelectMenu.play()
                    if event.key == pygame.K_y and len(nome)<11:
                        nome+="y"
                        somSelectMenu.play()
                    if event.key == pygame.K_z and len(nome)<11:
                        nome+="z"
                        somSelectMenu.play()
                    if event.key == pygame.K_BACKSPACE:
                        nome=""
                    if event.key == pygame.K_RETURN:
                        if nome=="":
                            nome="semnome"
                        ranking = open("leaderboard.txt","r+")
                        conteudo = ranking.readlines()
                        for i in range(len(conteudo)):
                            recorde=conteudo[i].split(" ")
                            if pontos > int(recorde[1]):
                                conteudo.insert(i,nome+" "+str(pontos)+"\n")
                                break
                        ranking.truncate(0)
                        ranking.seek(0)
                        for i in range(6):
                            ranking.write(conteudo[i])
                        ranking.close()
                        if lista[luvaPos]=="0":
                            gameloop()
                        else:
                            menu()

def ranking():
    #Sprites Ranking
    recordes = pygame.image.load(os.path.join("bitmaps","leaderboard.png"))
    
    luva = pygame.image.load(os.path.join("bitmaps","luva.png"))
    w,h = luva.get_size()
    luva = pygame.transform.scale(luva, (w*2,h*2))
    
    #Ranking Loop
    scores = open("leaderboard.txt")
    conteudo = scores.readlines()
    fonte = pygame.font.Font("fonte/emulogic.ttf", 16)

    #Som
    somSelectMenu = pygame.mixer.Sound("som/menuselect.wav")
    while True:
        posY=0
        screen.blit(recordes, (0,0))
        screen.blit(luva, (90,395))
        for i in conteudo:
            i=i.strip("\n")
            x = fonte.render(i, 1, (255,255,255))
            screen.blit(x, (90,100+posY))
            posY+=50          
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    somSelectMenu.play()
                    scores.close()
                    menu()
                     
def gameloop():
    #Variaveis Gameloop
    clock=pygame.time.Clock()
    clock.tick(1000)
    segundos=0
    minutos=0
    vidamac=100
    vidavon=100
    controlevon=0 
    fonte = pygame.font.Font("fonte/emulogic.ttf", 14)
    esquiva=0       #direcao da esquiva
    esquivacooldown=0
    punchcooldown=0
    standcontrol=0  #controle animaçao
    i=0
    direction="dir" #direcao soco
    pontos=0
    status="facil"
    prep=99
    react=50
    damageVon=10
    ptsMultiply=1
    bonusControl=2

    #Variaveis Som
    somBackground = pygame.mixer.Sound("som/fight.wav")
    somSoco = pygame.mixer.Sound("som/punchmac.wav")
    somDodge = pygame.mixer.Sound("som/dodge.wav")
    somDodgeFail = pygame.mixer.Sound("som/dodgefail.wav")
    somSocoVon1 = pygame.mixer.Sound("som/punchvon.wav")
    somSocoVon2 = pygame.mixer.Sound("som/punchvon2.wav")
    somCharge = pygame.mixer.Sound("som/charge.wav")
    somBlock = pygame.mixer.Sound("som/block.wav")
    somKo = pygame.mixer.Sound("som/falling.wav")
    somTorcida = pygame.mixer.Sound("som/torcida.wav")
    

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

    victoryMac1 = pygame.image.load(os.path.join("bitmaps/mac","victory1.png"))
    w,h = victoryMac1.get_size()
    victoryMac1 = pygame.transform.scale(victoryMac1, (w*2,h*2))

    victoryMac2 = pygame.image.load(os.path.join("bitmaps/mac","victory2.png"))
    w,h = victoryMac2.get_size()
    victoryMac2 = pygame.transform.scale(victoryMac2, (w*2,h*2))

    koMacEsq1 = pygame.image.load(os.path.join("bitmaps/mac","koMac.png"))
    w,h = koMacEsq1.get_size()
    koMacEsq1 = pygame.transform.scale(koMacEsq1, (w*2,h*2))

    koMacDir1 = pygame.transform.flip(koMacEsq1, True, False)

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

    koVonDir1 = pygame.image.load(os.path.join("bitmaps/von","kovon1.png"))
    w,h = koVonDir1.get_size()
    koVonDir1 = pygame.transform.scale(koVonDir1, (w*2,h*2))

    koVonDir2 = pygame.image.load(os.path.join("bitmaps/von","kovon2.png"))
    w,h = koVonDir2.get_size()
    koVonDir2 = pygame.transform.scale(koVonDir2, (w*2,h*2))

    koVonEsq1 = pygame.transform.flip(koVonDir1, True, False)
    koVonEsq2 = pygame.transform.flip(koVonDir2, True, False)

    victoryVon1 = pygame.image.load(os.path.join("bitmaps/von","victoryvon1.png"))
    w,h = victoryVon1.get_size()
    victoryVon1 = pygame.transform.scale(victoryVon1, (w*2,h*2))

    victoryVon2 = pygame.image.load(os.path.join("bitmaps/von","victoryvon2.png"))
    w,h = victoryVon2.get_size()
    victoryVon2 = pygame.transform.scale(victoryVon2, (w*2,h*2))    
    

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
        if vidamac!=0:
            pygame.draw.rect(screen, (255,0,0),(180,36,lifebarMac,15),0)
        if vidavon>=0:
            pygame.draw.rect(screen, (255,0,0),(292,36,lifebarVon,15),0)
        mins = fonte.render("0"+str(minutos), 1, (255,255,255)) 
        secs = fonte.render(":"+str(math.floor(segundos)), 1, (255,255,255))
        screen.blit(secs, (445, 33))
        screen.blit(mins, (415, 33))
        pts = fonte.render(str(pontos), 1, (255,255,255))
        screen.blit(pts, (320, 52))
        
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
        screen.blit(socodirvon4,(220,160))
        screen.blit(punchedmacdir2, (150,260))
        pygame.display.update()
        pygame.time.delay(350)

    def koVonDir():
        somKo.play()
        cont=1000
        posXVon=0
        posYVon=0
        posXMac=0
        posYMac=0
        for i in range(1000):
            screen.fill((0, 0, 0))
            interface()
            if posXVon<100:
                screen.blit(koVonDir1,(230+posXVon,120-posYVon))
            else:
                screen.blit(koVonDir2,(330,180-posYVon))
            if i<80:
                screen.blit(socoesq3, (250-posXMac,150))
            elif i<150:
                screen.blit(socoesq2, (230-posXMac,200))
            elif i<220:
                screen.blit(socoesq1, (220-posXMac,240))
            else:
                screen.blit(stand, (200,240))
            if posXVon<100:
                posXVon+=0.25
            if posYVon<70:
                posYVon+=0.25
            pygame.display.update()
        
        somBackground.stop()
        somTorcida.play()
        for i in range(10):
            screen.fill((0, 0, 0))
            interface()
            screen.blit(koVonDir2,(330,110))
            if i%2==0:
                screen.blit(victoryMac1,(200,240))
            else:
                screen.blit(victoryMac2,(200,220))
            pygame.display.update()
            pygame.time.delay(300)
        somTorcida.stop()
            
    def koVonEsq():
        somKo.play()
        cont=1000
        posXVon=0
        posYVon=0
        for i in range(900):
            screen.fill((0, 0, 0))
            interface()
            if posXVon<60:
                screen.blit(koVonEsq1,(160-posXVon,110-posYVon))
            else:
                screen.blit(koVonEsq2,(60,110-posYVon))
            if i<80:
                screen.blit(socodir3, (180,160))
            elif i<150:
                screen.blit(socodir2, (190,200))
            elif i<220:
                screen.blit(socodir1, (220,240))
            else:
                screen.blit(stand, (200,240))
            if posXVon<60:
                posXVon+=0.3
            if posYVon<20:
                posYVon+=0.1
            pygame.display.update()
        somTorcida.play()
        somBackground.stop()
        for i in range(8):
            screen.fill((0, 0, 0))
            interface()
            screen.blit(koVonEsq2,(60,90))
            if i%2==0:
                screen.blit(victoryMac1,(200,240))
            else:
                screen.blit(victoryMac2,(200,220))
            pygame.display.update()
            pygame.time.delay(300)
        somTorcida.stop()

    def koMacDir():
        posXMac=0
        posYMac=0
        somKo.play()
        for i in range(1000):
            screen.fill((0, 0, 0))
            interface()
            if i < 100:
                screen.blit(socoesqvon4,(180,150))
            elif i < 160:
                screen.blit(socoesqvon3,(200,145))
            else:
                screen.blit(idlevon1,(210,140))
            if i < 350:
                screen.blit(punchedmacesq2,(260+posXMac,260+posYMac))
            else:
                screen.blit(koMacEsq1,(260+posXMac,260+posYMac))
            if posXMac<=200:
                posXMac+=0.3
            if posYMac<=200:
                posYMac+=0.3
            pygame.display.update()
        somTorcida.play()
        somBackground.stop()
        for i in range(8):
            screen.fill((0, 0, 0))
            interface()
            if i%2==0:
                screen.blit(victoryVon1,(210,140))
            else:
                screen.blit(victoryVon2,(210,140))
            pygame.display.update()
            pygame.time.delay(500)
        somTorcida.stop()

    def koMacEsq():
        posXMac=0
        posYMac=0
        somKo.play()
        for i in range(1000):
            screen.fill((0, 0, 0))
            interface()
            if i < 100:
                screen.blit(socodirvon4,(220,160))
            elif i < 160:
                screen.blit(socodirvon3,(210,150))
            else:
                screen.blit(idlevon1,(210,140))
            if i < 350:
                screen.blit(punchedmacdir2,(150-posXMac,260+posYMac))
            else:
                screen.blit(koMacEsq1,(150-posXMac,260+posYMac))
            if posXMac<=200:
                posXMac+=0.3
            if posYMac<=200:
                posYMac+=0.3
            pygame.display.update()
        somTorcida.play()
        somBackground.stop()
        for i in range(8):
            screen.fill((0, 0, 0))
            interface()
            if i%2==0:
                screen.blit(victoryVon1,(210,140))
            else:
                screen.blit(victoryVon2,(210,140))
            pygame.display.update()
            pygame.time.delay(500)
        somTorcida.stop()
        
        
        
        
                    
        
    def idle(i,controlevon,direction):
        listavon=[idlevon1,idlevon2]
        listamac=[stand,stand2]
        listachargesesq=[socoesqvon1,socoesqvon2]
        listachargesdir=[socodirvon1,socodirvon2]
        # Preparacao Von
        if controlevon < 0:
            screen.blit(scaredvon, (210,140))
        elif controlevon<prep:
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
    while True: #vidavon>0 or vidamac>0
        #eventos

        #Aumentar dificuldade
        if vidavon==52:
            react=20
            somCharge = pygame.mixer.Sound("som/charge2.wav")
            damageVon=15    
        if controlevon==0:
            multiply=1

        #Controle Loop
        if controlevon>=0:
            controlevon += 1
        elif controlevon < 0:
            controlevon-=1
        if controlevon <= -40:
                controlevon=0
        if controlevon==30:
            prep = random.randint(50,120)

        #Controle Tempo
        segundos+=0.02
        if segundos>=60:
            minutos+=1
            segundos=0
        
        if controlevon==prep-10:
            direction = punchdirection()
            somCharge.play()
        

        if controlevon == prep+react:
            if direction == "dir" and esquiva<=0:
                esquiva=0
                vidamac-=damageVon*multiply
                controlevon=0
                puncheddir()
                if vidamac<=0:
                    koMacEsq()
                
                
            elif direction == "esq" and esquiva>=0:
                esquiva=0
                vidamac-=damageVon*multiply
                controlevon=0
                punchedesq()
                if vidamac<=0:
                    koMacDir()
                
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
                    if controlevon>prep and direction=="dir":
                        esquiva_esquerda()
                        esquiva=1
                        controlevon=-1
                    else:
                        missesquivaesquerda()
                        
                elif event.key == pygame.K_RIGHT and esquivacooldown==0:
                    esquivacooldown=50
                    if controlevon>prep and direction=="esq":
                        esquiva_direita()
                        esquiva = -1
                        controlevon=-1
                    else:
                        missesquivadireita()
                        
                elif event.key == pygame.K_z and punchcooldown==0:
                    punchcooldown=5
                    if controlevon<0:
                        jabesquerdo()
                        vidavon-=4
                        if bonusControl==1:
                            ptsMultiply+=1
                            bonusControl=0
                        else:
                            bonusControl=0
                            ptsMultiply=1                            
                        pontos+=100*ptsMultiply
                    else:
                        jabEsquerdoBlock()
                        multiply+=1
                    if vidavon<=0:
                        koVonDir()
              
                elif event.key == pygame.K_x and punchcooldown==0:
                    punchcooldown=5
                    if controlevon<0:
                        jabdireito()
                        vidavon-=4
                        if bonusControl==0:
                            ptsMultiply+=1
                            bonusControl=1
                        else:
                            bonusControl=0
                            ptsMultiply=1
                        pontos+=100*ptsMultiply
                    else:
                        jabDireitoBlock()
                        multiply+=1
                    if vidavon<=0:
                        koVonEsq()
                        
        if vidavon<=0 or vidamac<=0:
            break
        
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
        pygame.display.flip()
        
    if vidavon<=0:
        victory(pontos)
    else:
        derrota()
    
menu()

