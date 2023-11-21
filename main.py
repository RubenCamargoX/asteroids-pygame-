def menu(width,height,opcion_resolucion):
    pygame.mixer.init()
    pygame.init()
    pygame.display.set_caption("ASTEROIDES")
    #variebles
    scale = [(width-95),(25)]
    if opcion_resolucion == 1 : 
        escala_logo_menu = [335,235]
        pos_logo_menu = (((width/3)+25),(height/16))
        pos_botton_playx = ((width/2)-35)
        pos_botton_playy = ((height/2)-25)
        pos_botton_aboutx = ((width/2)-35)
        pos_botton_abouty = ((height/2)+15)
        pos_botton_exitx = ((width/2)-35)
        pos_botton_exity = ((height/2)+55)
        pos_texto_play = [(width/2)-20, ((height/2)-25)]
        pos_texto_about = [((width/2)-33),((height/2)+15)] 
        pos_texto_exit = [((width/2)-20),((height/2)+55)]
    elif opcion_resolucion == 2 :
        escala_logo_menu = [300,200]
        pos_logo_menu = (((width/3)),(height/9))
        pos_botton_playx = ((width/2)-35)
        pos_botton_playy = ((height/2)-25)
        pos_botton_aboutx = ((width/2)-35)
        pos_botton_abouty = ((height/2)+15)
        pos_botton_exitx = ((width/2)-35)
        pos_botton_exity = ((height/2)+55)
        pos_texto_play = [(width/2)-20, ((height/2)-25)]
        pos_texto_about = [((width/2)-33),((height/2)+15)] 
        pos_texto_exit = [((width/2)-20),((height/2)+55)]
    elif opcion_resolucion == 3 :
        escala_logo_menu = [335,235]
        pos_logo_menu = (((width/3)+25),(height/16))
        pos_botton_playx = ((width/2)-35)
        pos_botton_playy = ((height/2)-25)
        pos_botton_aboutx = ((width/2)-35)
        pos_botton_abouty = ((height/2)+15)
        pos_botton_exitx = ((width/2)-35)
        pos_botton_exity = ((height/2)+55)
        pos_texto_play = [(width/2)-20, ((height/2)-25)]
        pos_texto_about = [((width/2)-33),((height/2)+15)] 
        pos_texto_exit = [((width/2)-20),((height/2)+55)]
    size = [width,height]

    screen = pygame.display.set_mode(size)
    clock  = pygame.time.Clock()

    #fuentes
    font = pygame.font.SysFont("tahoma", 30)
    font2 = pygame.font.SysFont("tahoma", 20)
    
    #texto  para mostrar en pantalla
    TextPlay  = font.render("Play", True, white)
    TextExit = font.render("Exit", True, white)
    TextAbaut = font.render("About", True, white)
    Textres1 = font2.render("1080x720", True, white)
    Textres2 = font2.render("800x600", True, white)
    Textres3 = font2.render("1366x768", True, white)
    Textres = font2.render("1366x1080", True, white)

    #cargar imagenes
    fondoMenu = pygame.image.load("img/fondoMenu.jpg")
    fondoMenu = pygame.transform.scale(fondoMenu, size)
    logomenu = pygame.image.load("img/logomenu.png")
    logomenu = pygame.transform.scale(logomenu, escala_logo_menu)
    asteroids = pygame.image.load("img/asteroids.png")
    asteroids.set_colorkey([0,0,0])
    nave = pygame.image.load("img/nave.png")
    pygame.display.set_icon(nave)

    #cargar sonidos
    star = pygame.mixer.Sound("sound/star.mp3")
    fondo = pygame.mixer.Sound("sound/soundfondo.mp3")

    #coordenas de aparición de los asteroides
    coor_list = []
    for i in range(30):
        x  = random.randint(0,width)
        y  = random.randint(0,height)
        coor_list.append([x,y])

    menu = True
    click_state = False
    while menu == True : 
        #color de fondo
        screen.blit(fondoMenu,(0,0))

        #cargar a la pantalla los asteroides
        for j in coor_list:
            x  = j[0]
            y  = j[1]
            screen.blit(asteroids,(x,y))
            j[1] += 1
            if j[1] > height:
                j[1] = 0

        #para el fondo negro de los botones
        bottonPlay1 = pygame.draw.rect(screen, [0,0,0], (pos_botton_playx,pos_botton_playy,85,40), 0)
        bottonAbout1 = pygame.draw.rect(screen, [0,0,0], (pos_botton_aboutx,pos_botton_abouty,85,40), 0)
        bottonExit1 = pygame.draw.rect(screen, [0,0,0], (pos_botton_exitx,pos_botton_exity,85,40), 0)
        bottonR0 = pygame.draw.rect(screen, [0,0,0], ((width-95),(25),85,40), 0)
        #botones
        bottonPlay = pygame.draw.rect(screen, [237,128,19], (pos_botton_playx,pos_botton_playy,85,40), 2)
        bottonAbout = pygame.draw.rect(screen, [70,189,34], (pos_botton_aboutx,pos_botton_abouty,85,40), 2)
        bottonExit = pygame.draw.rect(screen, [70,189,34], (pos_botton_exitx,pos_botton_exity,85,40), 2)
        bottonR = pygame.draw.rect(screen, [255,255,255], ((width-95),(25),85,40), 2)

        #cambio de colores de las figuras y letras
        if bottonPlay.collidepoint(pygame.mouse.get_pos()):
            bottonPlay = pygame.draw.rect(screen, [237,128,19], (pos_botton_playx,pos_botton_playy,85,40), 2)
            TextPlay  = font.render("Play", True, [237,128,19])
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            bottonPlay = pygame.draw.rect(screen, [70,189,34], (pos_botton_playx,pos_botton_playy,85,40), 2)
            TextPlay  = font.render("Play", True, white)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if bottonAbout.collidepoint(pygame.mouse.get_pos()):
            bottonAbout = pygame.draw.rect(screen, [237,128,19], (pos_botton_aboutx,pos_botton_abouty,85,40), 2)
            TextAbaut = font.render("About", True, [237,128,19])
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            bottonAbout = pygame.draw.rect(screen, [70,189,34], (pos_botton_aboutx,pos_botton_abouty,85,40), 2)
            TextAbaut = font.render("About", True, white)
            # pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if bottonExit.collidepoint(pygame.mouse.get_pos()):
            bottonExit = pygame.draw.rect(screen, [237,128,19], (pos_botton_exitx,pos_botton_exity,85,40), 2)
            TextExit = font.render("Exit", True, [237,128,19])
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            bottonExit = pygame.draw.rect(screen, [70,189,34], (pos_botton_exitx,pos_botton_exity,85,40), 2)
            TextExit = font.render("Exit", True, white)

        #cargar texto
        screen.blit(Textres,scale)
        screen.blit(TextPlay,pos_texto_play)
        screen.blit(TextAbaut,pos_texto_about)
        screen.blit(TextExit,pos_texto_exit)


        #eventos dentro de la pantalla
        for event in pygame.event.get():

            #evento para salir
            if event.type == pygame.QUIT:
                sys.exit()
            
            #eventos para los botones
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if bottonPlay.collidepoint(pygame.mouse.get_pos()):
                    reso = opcion_resolucion
                    op = 3
                    fondo.stop()
                    star.play()
                    time.sleep(1)
                    menu = False
                elif bottonAbout.collidepoint(pygame.mouse.get_pos()):
                    reso = opcion_resolucion
                    op = 2
                    fondo.stop()
                    star.play()
                    time.sleep(0.7)
                    menu = False
                elif bottonExit.collidepoint(pygame.mouse.get_pos()):
                    fondo.stop()
                    star.play()
                    time.sleep(1)
                    sys.exit()
                elif bottonR.collidepoint(pygame.mouse.get_pos()):
                    click_state = not click_state

        if click_state == True:
            bottonR1 = pygame.draw.rect(screen, [255,0,0], ((width-95),(65),85,40), 0)
            bottonR2 = pygame.draw.rect(screen, [0,0,255], ((width-95),(105),85,40), 0)
            bottonR3 = pygame.draw.rect(screen, [0,255,0], ((width-95),(145),85,40), 0)
            screen.blit(Textres1,(width-95,65))
            screen.blit(Textres2,(width-95,105))
            screen.blit(Textres3,(width-95,145))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if bottonR1.collidepoint(pygame.mouse.get_pos()):
                    reso = 1
                    op = 1
                    menu = False
                    Textres = font2.render("1080x720", True, white)
                elif bottonR2.collidepoint(pygame.mouse.get_pos()):
                    reso = 2
                    op = 1
                    menu = False
                    Textres = font2.render("800x600", True, white)
                elif bottonR3.collidepoint(pygame.mouse.get_pos()):
                    reso = 3
                    op = 1
                    menu = False
                    Textres = font2.render("1366x1080", True, white)
        else:
            bottonR1 = 0
            bottonR2 = 0
            bottonR3 = 0


        screen.blit(logomenu, pos_logo_menu)
        pygame.display.update()
        clock.tick(60)
    pygame.mixer.quit()
    return op,reso

def about(width,height):
    size = [width,height]
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("ASTEROIDES")
    nave = pygame.image.load("img/nave.png")
    pygame.display.set_icon(nave)
    fondo1 = pygame.mixer.Sound("sound/soundfondo.mp3")
    fondo1.play()
    screen = pygame.display.set_mode(size)
    clock  = pygame.time.Clock()

    # muestra las imagenes de la pantalla principal
    fondo = pygame.image.load("img/fondoEspacio.jpg")
    fondo = pygame.transform.scale(fondo, (width,height))


    #cargar fuente en diccionario
    fuente1 = pygame.font.Font(None, 70)

    # cargar fuente
    fuente = pygame.font.SysFont("Cooper Black", 30)
    fuente1 = pygame.font.SysFont("Ink Free", 30)
    # cargar texto
    texto = fuente.render("C r e d i t s ", False, (245, 253, 3 ))
    texto1 = fuente1.render(" Desarrolladores del juego :", False, (245, 253, 3 ))
    noelia = fuente1.render(" - Noelia Gonzales ", False, (225, 195, 136 ))
    ruben = fuente1.render(" - Ruben Camargo ", False, (225, 195, 136 ))
    willian = fuente1.render(" - Jhon Fernández  ", False, (225, 195, 136 ))
    carlos = fuente1.render(" - Juan Carlos Kama ", False, (225, 195, 136 ))
    cristian = fuente1.render(" - Cristian Cayo  ", False, (225, 195, 136 ))
    backT = fuente1.render("BACK", False, (255, 255, 255))
    #muestra las coordenadas de los puntos (lluvia)
    coord_list= []
    for i in range(60):
            x = random.randint(0,width)
            y = random.randint(0, height)
            coord_list.append([x,y])

    about = True
    while about == True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if back.collidepoint(pygame.mouse.get_pos()):
                op = 1
                fondo1.stop()
                about = False
        
        screen.fill(black)
        screen.blit(fondo,(0,0))
        #muestra el boton
        back = pygame.draw.rect(screen, [222,100,0], (width-100,height-50,85,40), 0)
        if back.collidepoint(pygame.mouse.get_pos()):
            back = pygame.draw.rect(screen, [237,128,19], (width-100,height-50,97,40), 0)
            backT  = fuente.render("MENU", True, [70,189,34])
        else:
            back = pygame.draw.rect(screen, [237,128,19], (width-100,height-50,97,40), 0)
            backT  = fuente.render("MENU", True, (255,255,255))
        # muuestra la lluvia aleatorio
        list_de_coordenadas= ()
        for j in coord_list:
                x = j[0]
                y = j[1]
                pygame.draw.circle(screen,white ,(x, y), 2)
                j[1] +=1
                if j[1] > 600:
                    j[1] = 0 
        #mostrar texto de los desarrolladores del juego          
        screen.blit(texto, (300,10))
        screen.blit(texto1, (10,170))
        screen.blit(noelia, (10,210))
        screen.blit(ruben, (10,250))
        screen.blit(willian, (10,290))
        screen.blit(carlos, (10,330))
        screen.blit(cristian, (10,370))
        screen.blit(backT, (width-100,height-50))
        
        pygame.display.flip()
        clock.tick(60)
    return  op
    #falta mostrar el boton para regresar a menu

def juego (width,height,opcion_resolucion):
    pygame.init()
    pygame.mixer.init()
    size = [width,height]
    screen=pygame.display.set_mode(size)
    pygame.display.set_caption("ASTEROIDES")
    nave1 = pygame.image.load("img/nave.png")
    pygame.display.set_icon(nave1)
    clock= pygame.time.Clock()
    if opcion_resolucion == 1 : 
        scale_nav = (50,50)
        scale_asteroids = (50,50)
        scale_laser = (45,45)
        scale_explo = (70,70)
    elif opcion_resolucion == 2 :
        scale_nav = (40,40)
        scale_asteroids = (40,40)
        scale_laser = (40,40)
        scale_explo = (60,60)
    elif opcion_resolucion == 3 :
        scale_nav = (50,50)
        scale_asteroids = (50,50)
        scale_laser = (45,45)
        scale_explo = (70,70)

    #surface=donde dibujar el texto
    def dibujarTexto(surface,text,size,x,y):
        font = pygame.font.SysFont("serif",size)
        text_surface= font.render(text,True,white)
        text_rect=text_surface.get_rect()
        text_rect.midtop=(x,y)
        surface.blit(text_surface,text_rect)

    def dibujarBarraVida(surface,x,y,porcentaje):
        barra_lenght= 100
        barra_height= 10
        fill_lenght=(porcentaje/100)*barra_lenght
        border= pygame.Rect(x,y,barra_lenght,barra_height)
        fill= pygame.Rect(x,y,fill_lenght,barra_height)
        pygame.draw.rect(surface,green,fill)
        pygame.draw.rect(surface,white,border,1)

    #clase para la nave espacial
    class Nave(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image=pygame.transform.scale((pygame.image.load("img/nave.png").convert()),scale_nav)
            #bug con la imagen de la nave a la hora de chocar
            self.image.set_colorkey(black)
            self.rect=self.image.get_rect()
            self.rect.centerx = width//2
            self.rect.bottom=height-10
            self.speed_x=0
            self.vida=100
        def update(self):
            self.speed_x=0
            self.speed_y=0
            #movimiento de la nave
            keystate= pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.speed_x=-5
            if keystate[pygame.K_RIGHT]:
                self.speed_x=5
            if keystate[pygame.K_UP]:
                self.speed_y=-5
            if keystate[pygame.K_DOWN]:
                self.speed_y=5
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            #para que se mantenga en el ancho y altura establecido
            if self.rect.right>width:
                self.rect.right=width
            if self.rect.left<0:
                self.rect.left=0
            if self.rect.top<0:
                self.rect.top=0
            if self.rect.bottom>height:
                self.rect.bottom=height
        def disparar(self):
            bullet=Bala(self.rect.centerx,self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            laser_sound.play()

    class Meteorito(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            #meteoros de distinto tamaño aleatoriamente
            #self.image=random.choice(meteoro_imagenes)
            self.image=pygame.image.load("img/asteroids.png").convert()
            self.image = pygame.transform.scale(self.image,scale_asteroids)
            self.image.set_colorkey(black)
            self.rect=self.image.get_rect()
            self.rect.x=random.randrange(width-self.rect.width)
            self.rect.y=random.randrange(-25,-10)
            self.speedy=random.randrange(1,3)
            self.speedx=random.randrange(-3,3)
            #caida de los meteoros
        def update(self):
            self.rect.y+=self.speedy
            self.rect.x+=self.speedx
            if self.rect.top>height+10 or self.rect.left < -25 or self.rect.right > width+25:
                self.rect.x=random.randrange(width-self.rect.width)
                self.rect.y=random.randrange(-25,-10)
                self.speedy=random.randrange(1,3)

    class Bala(pygame.sprite.Sprite):
        def __init__(self,x,y):
            super().__init__()
            #carga la imagen
            self.image=pygame.image.load("img/laser1.png")
            self.image = pygame.transform.scale(self.image,scale_laser)
            #remover el fondo
            self.image.set_colorkey(black)
            self.rect=self.image.get_rect()
            self.rect.y=y
            self.rect.centerx=x
            self.speedy=-10
        def update(self):
            #la bala sube automaticamente 
            self.rect.y+=self.speedy
            #elimina las instacias/balas para que no ocupe espacio de memoria
            if self.rect.bottom<0:
                self.kill()

    class ExplosionBala(pygame.sprite.Sprite):
        def __init__(self,center):
            super().__init__()
            self.image = explosion_anim[0]
            self.rect=self.image.get_rect()
            self.rect.center = center
            self.frame=0
            self.last_update=pygame.time.get_ticks() #cuanto tiempo transcurrio cuando se inicio el juego
            self.frame_rate=50 #velocidad de la explosion
        def update(self):
            now=pygame.time.get_ticks()
            if now-self.last_update > self.frame_rate:
                self.last_update=now
                self.frame+=1
                if self.frame == len(explosion_anim):
                    self.kill()
                else:
                    center=self.rect.center
                    self.image=explosion_anim[self.frame]
                    self.rect= self.image.get_rect()
                    self.rect.center=center
    class ExplosionNave(pygame.sprite.Sprite):
        def __init__(self,center):
            super().__init__()
            self.image = explosion_anim2[0]
            self.rect=self.image.get_rect()
            self.rect.center = center
            self.frame=0
            self.last_update=pygame.time.get_ticks() #cuanto tiempo transcurrio cuando se inicio el juego
            self.frame_rate=50 #velocidad de la explosion
        def update(self):
            now=pygame.time.get_ticks()
            if now-self.last_update > self.frame_rate:
                self.last_update=now
                self.frame+=1
                if self.frame == len(explosion_anim2):
                    self.kill()
                else:
                    center=self.rect.center
                    self.image=explosion_anim2[self.frame]
                    self.rect= self.image.get_rect()
                    self.rect.center=center

    def muestraGameOver():
        fuente = pygame.font.SysFont("Cooper Black", 30)
        volver  = fuente.render("MENU", True, (255,255,255))
        screen.fill(black)
        dibujarTexto(screen,"PLAY AGAIN",30,700,550)
        dibujarTexto(screen,"GAME OVER",70,width//2,height//2)
        pygame.display.flip()
        espera=True
        while espera:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if back.collidepoint(pygame.mouse.get_pos()):
                        espera = False
            back = pygame.draw.rect(screen, [222,100,0], (700,550,85,40), 0)
            if back.collidepoint(pygame.mouse.get_pos()):
                back = pygame.draw.rect(screen, [237,128,19], (700,550,97,40), 0)
                volver  = fuente.render("MENU", True, [70,189,34])
            else:
                back = pygame.draw.rect(screen, [237,128,19], (700,550,97,40), 0)
                volver  = fuente.render("MENU", True, (255,255,255))
            screen.blit(volver, (700,550))

    def pause() :
        screenP = pygame.display.set_mode((400, 300))
        screenP.fill(black)
        pausa = True
        while pausa:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                   if event.key==pygame.K_ESCAPE:
                        sys.exit(pause())
                        pausa = False
            pygame.display.update()
                   

    background = pygame.image.load("img/fondoPlayer.png")
    background = pygame.transform.scale(background,(width,height))
    #cargar img explosiones
    #lista de explosiones
    explosion_anim=[]
    for i in range(9):
        file="img/regularExplosion0{}.png".format(i)
        img=pygame.image.load(file).convert()
        img.set_colorkey(black)
        img_scale=pygame.transform.scale(img,scale_explo)
        explosion_anim.append(img_scale)

    explosion_anim2=[]
    img=pygame.image.load("img/regularExplosion03.png").convert()
    img.set_colorkey(black)
    img_scale=pygame.transform.scale(img,scale_explo)
    explosion_anim2.append(img_scale)

    #cargando sonidos 
    laser_sound=pygame.mixer.Sound("sound/laser.ogg")
    explosion_sound=pygame.mixer.Sound("sound/explosion.wav")
    pygame.mixer.music.load("sound/soundPlayer.ogg")
    pygame.mixer.music.set_volume(0.9)


    all_sprites=pygame.sprite.Group()
    meteoro_lista=pygame.sprite.Group()
    bullets=pygame.sprite.Group()


    jugador=Nave()
    cant = 0
    all_sprites.add(jugador)
    cant = 0
    for i in range(8):
        print (cant)
        meteoro=Meteorito()
        all_sprites.add(meteoro)
        meteoro_lista.add(meteoro)

    score=0
    pygame.mixer.music.play(loops=-1)
    Game_over=False


    back = pygame.draw.rect(screen, [0,0,255], (250,350,85,40), 0)
    running=True
    pausee = False
    while running:
        if Game_over==True:
            muestraGameOver()
            running=False
        elif pausee == True:
            pause()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    jugador.disparar()
                elif event.key==pygame.K_ESCAPE:
                    pausee = not pausee

        all_sprites.update()
        #colisiones-meteoro-laser
        hits=pygame.sprite.groupcollide(meteoro_lista,bullets,True,True)
        #vuelve a caer los meteoros aunque se destruyan
        for hit in hits:
            cant += 1
            if cant ==15 :
                cant = 1
                for i in range(cant):
                    print (cant)
                    meteoro=Meteorito()
                    all_sprites.add(meteoro)
                    meteoro_lista.add(meteoro)
            score+=50
            explosion_sound.play()
            explosion=ExplosionBala(hit.rect.center)
            all_sprites.add(explosion)
            meteoro=Meteorito()
            all_sprites.add(meteoro)
            meteoro_lista.add(meteoro)
        #colisiones-jugador-meteoro
        hits = pygame.sprite.spritecollide(jugador,meteoro_lista,True)
        for hit in hits:
            # explosion_sound.play()
            explosiones=ExplosionNave(hit.rect.center)
            all_sprites.add(explosiones)
            jugador.vida-=33.9
            meteoro=Meteorito()
            all_sprites.add(meteoro)
            meteoro_lista.add(meteoro)
            if jugador.vida<0:
                Game_over=True


        screen.blit(background,(0,0))
        all_sprites.draw(screen)
        #marcador
        dibujarTexto(screen,str("Points:"),25,(width-170),10)
        dibujarTexto(screen,str(score),25,(width-50),10)
        dibujarBarraVida(screen,5,5,jugador.vida)
        pygame.display.flip()
    pygame.quit()
    return op


#inicio del juego
import pygame,sys,time,random

op = 1

#tamaño de las ventana
width = 800
height = 600
reso = 2

#colores
white = [255,255,255]
black = [0,0,0]
blue = [0, 0, 255]
green=[0,255,0]

#iniciar pygame
pygame.init()
pygame.mixer.init()
salir = False
while salir == False :
    if op == 1:
        op,reso = menu(width,height,reso)
    elif op == 2:
        op = about(width,height)
    elif op == 3:
        op = juego(width,height,reso)
    if reso == 1 :
        width = 1060
        height = 620
    elif reso == 2 :
        width = 800
        height = 600
    elif reso == 3 :
        width3 = 1366
        height3 = 1080
pygame.mixer.quit()