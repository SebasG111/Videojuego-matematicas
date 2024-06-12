#------------videojuego---------
import pygame
import sys
from Preguntas import *
import random
from tkinter import *
import tkinter as tk
from tkinter import messagebox

#--------Globales/Constantes-------#
seleccion = None #Importante--

cuadroA = 0
x = 100
y = 550
alto = 50
ancho = 50
velocidad = 5
fps = 75
door1_visible = True
door2_visible = True
door3_visible = True
door4_visible = True
door5_visible = True
door6_visible = True

destruir = 0
#-----Enunciados de las preguntas---#
mensaje = ["Encontrar los puntos de corte con el eje x e y de la siguiente ecuacion ",
           "Encontrar la ecuacion de la recta de los puntos dados",
           "Responder de acuerdo al enunciado",
           "Identificar a que conica pertenece la ecuacion dada",
           "Reemplazar los valores dados en la funcion y responder",
           "Responder de acuerdo al enunciado"]
#-----Hitxbox de las paredes---#
def bloquear_estado():
    global x
    global y
    if estado[pygame.K_LEFT]:
        x += velocidad
    elif estado[pygame.K_RIGHT]:
        x -= velocidad
    elif estado[pygame.K_UP]:
        y += velocidad
    elif estado[pygame.K_DOWN]:
        y -= velocidad

#--------Estados del personaje-----#

def animaciones(direccion, contador):
    if direccion == "derecha":
        estado1 = derecha[contador % len(derecha)]
        quieto[0] = derecha[0]
    elif direccion == "izquierda":
        estado1 = izquierda[contador % len(izquierda)]
        quieto[0] = izquierda[0]
    elif direccion == "arriba":
        estado1 = arriba[contador % len(arriba)]
        quieto[0] = arriba[0]
    elif direccion == "abajo":
        estado1 = abajo[contador % len(abajo)]
        quieto[0] = abajo[0]
    else:
        estado1 = quieto[0]
    ventana.blit(personaje, (x,y), estado1)


#-Hace que cuando el jugador falle la pregunta este sea empujado hacia atras
#-Sin esto el jugador se quedaria en un bucle infinito hasta que responda bien la pregunta
def empujar_jugador():
    global x, y, direccion
    if direccion == "izquierda":
        x += 50
    elif direccion == "derecha":
        x -= 50
    elif direccion == "arriba":
        y += 50
    elif direccion == "abajo":
        y -= 50
    
#-------Primera puerta y primera pregunta-----#
#-Arroja una pregunta correspondiente a la puerta
def mostrar_pregunta():
    global seleccion
    pag2 = Tk()
    pag2.withdraw()
    #----#
    preguntaV2 = tk.Toplevel()
    preguntaV2.geometry("500x500")
    #--elegir pregunta aleatoria--
    op2 = tk.StringVar()
    #-----#
    pregunta = generar_pregunta[seleccion]
    respuesta = generar_respuesta[seleccion]
    clave2 = random.choice(list(pregunta.keys()))
    enunciado2 = tk.Label(preguntaV2,text=mensaje[seleccion])
    enunciado2.pack()
    mostrar2 = tk.Label(preguntaV2,text=clave2)
    mostrar2.pack()
    opciones2 = pregunta[clave2]
    respuestaV2 = respuesta[clave2]
    opcionesM2 = tk.OptionMenu(preguntaV2, op2, *opciones2)
    opcionesM2.pack()
    responder2 = tk.Button(preguntaV2,text="Confirmar",command=lambda:verificar_respuesta(op2,respuestaV2,clave2,pag2,pregunta))
    responder2.pack()
    pag2.mainloop()

#Verifica  si la respuesta ingresada por el usuario es correcta

def verificar_respuesta(op2,respuestaV2,clave2,pag2,pregunta):
    global door3_visible
    global seleccion
    global destruir
    res2 = op2.get()
    if res2 == pregunta[clave2][respuestaV2]:
        print("a")
        destruir[seleccion]()
        pag2.destroy()
    else:
        empujar_jugador()
        pag2.destroy()

#---Destruir puertas---#

def destroy_door1():
    global door1_visible
    door1_visible = False
    hitbox_door1.x = -1000
    hitbox_door1.y = -1000



def destroy_door2():
    global door2_visible
    door2_visible = False
    hitbox_door2.x = -1000
    hitbox_door2.y = -1000



def destroy_door3():
    global door3_visible
    door3_visible = False
    hitbox_door3.x = -1000
    hitbox_door3.y = -1000

def destroy_door4():
    global door4_visible
    door4_visible = False
    hitbox_door4.x = -1000
    hitbox_door4.y = -1000

def destroy_door5():
    global door5_visible
    door5_visible = False
    hitbox_door5.x = -1000
    hitbox_door5.y = -1000

def destroy_door6():
    global door6_visible
    door6_visible = False
    hitbox_door6.x = -1000
    hitbox_door6.y = -1000
#-------FIN DEL JUEGO------#
def game_over():
    mensaje = messagebox.showwarning("FELICIDADES!!","HAZ GANADO EL JUEGO!!!")
    empujar_jugador()



if __name__=='__main__':
    pygame.init()
    #-------Personaje-------#
    personaje = pygame.image.load("personaje.png")
    #-hitbox jugador
    jugador_recta = personaje.get_rect()
    jugador_recta.topleft = (x-90,y-90)
    hitbox_jugador = pygame.Rect(jugador_recta.x+100,jugador_recta.y+100,
                                 jugador_recta.width-237,jugador_recta.height-245)
    #----Estado del personaje----#
    izquierda = [(0, 64, 64, 64),(64, 64, 64, 64),(128, 64, 64, 64),(192, 64, 64, 64)]
    derecha = [(0, 128, 64, 64),(64, 128, 64, 64),(128, 128, 64, 64),(192, 128, 64, 64)]
    arriba = [(0, 192, 64, 64),(64, 192, 64, 64),(128, 192, 64, 64),(192, 192, 64, 64)]
    abajo = [(0, 0, 64, 64),(64, 0, 64, 64),(128, 0, 64, 64),(192, 0, 64, 64)]
    quieto = [(0, 0, 64, 64)]
    contador = 0
    reloj = pygame.time.Clock()
    frame = 0
    frameM = 10
    #--FONT--
    font = pygame.font.SysFont('Arial',50)
    black = (0,0,0)
    #---Cargar imagenes--#
    #-Imagenes de las puertas-
    puertas = pygame.image.load("17.png")
    puertas = pygame.transform.scale(puertas,(90,90))
    #-Imagenes de los muros superiores
    muros = pygame.image.load("18.png")
    muros = pygame.transform.scale(muros,(180,90))
    #-Imagenes paredes laterales
    lateral = pygame.image.load("19.png")
    lateral = pygame.transform.scale(lateral,(30,300))
    #-------Tamaño------#
    tamaño = (1200,650)
    ventana = pygame.display.set_mode(tamaño)
    #-------fondo-----#
    fondoINC = pygame.image.load("FONDO UNO.jpg")
    fondo1 = pygame.transform.scale(fondoINC, (1200,650))
    #-------Muros-----#
    #-Habitacion 1
    #-muro1
    muro1 = muros
    hitbox_muro1 = muro1.get_rect()
    hitbox_muro1.x = -20
    hitbox_muro1.y = 400
    #-muro2
    muro2 = lateral
    hitbox_muro2 = muro2.get_rect()
    hitbox_muro2.x = 250
    hitbox_muro2.y = 400
    #-puerta-
    door1 = puertas
    hitbox_door1 = door1.get_rect()
    hitbox_door1.x = 160
    hitbox_door1.y = 400
    #---------Habitacion 2-----------#
    muro4 = muros
    hitbox_muro4 = muro4.get_rect()
    hitbox_muro4.x = -20
    hitbox_muro4.y = 180
    #--
    muro3 = lateral
    hitbox_muro3 = muro3.get_rect()
    hitbox_muro3.x = 250
    hitbox_muro3.y = 180
    #--
    door2 = puertas
    hitbox_door2 = door2.get_rect()
    hitbox_door2.x = 160
    hitbox_door2.y = 180
    #---------Pasillo----#
    #-Muro lateral 1
    muro5 = lateral
    #Muro lateral 2
    muro6 = lateral
    #---Hitbox de las paredes laterales---#
    hitbox_uni1 = pygame.Rect(357,0,30,480)
    #-Muros superiores
    muro7 = muros
    #-
    muro8 = muros
    #-Entrada/ Puerta 3
    muro9 = muros
    hitbox_muro9 = muro9.get_rect()
    hitbox_muro9.x = 358
    hitbox_muro9.y = 400
    #-Puerta 3-
    door3 = puertas
    hitbox_door3 = door3.get_rect()
    hitbox_door3.x = 538
    hitbox_door3.y = 400
    #Muro lateral 1
    muro12 = lateral
    hitbox_uni3 = pygame.Rect(628,180,30,500)
    #-----Habitacion 4/ Pregunta 4---#
    muro11 = lateral
    #-
    door4 = puertas
    hitbox_door4 = door3.get_rect()
    hitbox_door4.x = 388
    hitbox_door4.y = 180
    #-
    muro14 = muros
    hitbox_muro14 = muro9.get_rect()
    hitbox_muro14.x = 477
    hitbox_muro14.y = 180
    #----Pasillo 2------
    #-Muros superiores
    muro15 = muros
    #-
    muro16 = muros
    #-
    muro17 = muros
    #-
    muro18 = muros
    #-
    muro19 = muros
    #-
    muro20 = lateral
    #-
    muro21 = muros
    hitbox_muro21 = muro21.get_rect()
    hitbox_muro21.x = 810
    hitbox_muro21.y = 400
    #-
    muro22 = muros
    hitbox_muro22 = muro21.get_rect()
    hitbox_muro22.x = 1079
    hitbox_muro22.y = 400
    #-
    muro24 = muros
    hitbox_muro24 = muro24.get_rect()
    hitbox_muro24.x = 810
    hitbox_muro24.y = 180
    #-
    muro25 = muros
    hitbox_muro25 = muro25.get_rect()
    hitbox_muro25.x = 1079
    hitbox_muro25.y = 180
    #Pared superior
    hitbox_uni4 = pygame.Rect(0,0,1200,90)
    hitbox_uni5 = pygame.Rect(0,650,1200,20)
    hitbox_uni6 = pygame.Rect(810,0,30,480)
    #-Puerta 5/ pregunta 5
    door5 = puertas
    hitbox_door5 = door5.get_rect()
    hitbox_door5.x = 990
    hitbox_door5.y = 400
    #-Puerta 6/ pregunta 6
    door6 = puertas
    hitbox_door6 = door6.get_rect()
    hitbox_door6.x = 990
    hitbox_door6.y = 180
    #-Recompensa-
    cofre = pygame.image.load("cofre.png")
    cofre = pygame.transform.scale(cofre,(60,60))
    hitbox_cofre = cofre.get_rect()
    hitbox_cofre.x = 1000
    hitbox_cofre.y = 100
    #-----DECORACIONES----
    #-Libreria grande
    libreria = pygame.image.load("libreria1.png")
    libreria = pygame.transform.scale(libreria,(140,70))
    #-Libreria mediana
    libreriaM = pygame.image.load("libreria2.png")
    libreriaM = pygame.transform.scale(libreriaM,(70,70))
    #-Libreria pequeña
    libreriaP = pygame.image.load("libreria3.png")
    libreriaP = pygame.transform.scale(libreriaP,(35,70))
    #-Plantas
    plant = pygame.image.load("26.png")
    plant = pygame.transform.scale(plant,(50,70))
    plantD = pygame.image.load("27.png")
    plantD = pygame.transform.scale(plantD,(50,100))
    #-Cuadros
    marc = pygame.image.load("25.png")
    marc = pygame.transform.scale(marc,(50,30))
    marcD = pygame.image.load("24.png")
    marcD = pygame.transform.scale(marcD,(50,35))
    #-----------#
    libreria1 = libreria
    hitbox_libreria1 = libreria1.get_rect()
    hitbox_libreria1.x = 0
    hitbox_libreria1.y = 440
    #---
    libreria2 = libreria
    hitbox_libreria2 = libreria2.get_rect()
    hitbox_libreria2.x = 120
    hitbox_libreria2.y = 40
    #---
    libreriaM1 = libreriaM
    hitbox_libreriaM1 = libreriaM1.get_rect()
    hitbox_libreriaM1.x = 288
    hitbox_libreriaM1.y = 40
    #---
    libreriaP1 = libreriaP
    hitbox_libreriaP1 = libreriaP1.get_rect()
    hitbox_libreriaP1.x = 380
    hitbox_libreriaP1.y = 440
    #---
    libreriaM2 = libreriaM
    hitbox_libreriaM2 = libreriaM2.get_rect()
    hitbox_libreriaM2.x = 420
    hitbox_libreriaM2.y = 440
    #----
    libreria3 = libreria
    hitbox_libreria3 = libreria3.get_rect()
    hitbox_libreria3.x = 640
    hitbox_libreria3.y = 40
    #----
    libreria4 = libreria
    hitbox_libreria4 = libreria4.get_rect()
    hitbox_libreria4.x = 460
    hitbox_libreria4.y = 40
    #----
    libreriaM3 = libreriaM
    hitbox_libreriaM3 = libreriaM3.get_rect()
    hitbox_libreriaM3.x = 900
    hitbox_libreriaM3.y = 220
    #----
    libreriaM4 = libreriaM
    hitbox_libreriaM4 = libreriaM4.get_rect()
    hitbox_libreriaM4.x = 1100
    hitbox_libreriaM4.y = 220
    #----
    plant1 = plant
    hitbox_plant1 = plant1.get_rect()
    hitbox_plant1.x = 50
    hitbox_plant1.y = 50
    #----
    plant2 = plant
    hitbox_plant2 = plant2.get_rect()
    hitbox_plant2.x = 40
    hitbox_plant2.y = 220
    #----
    marc1 = marc
    marcD2 = marcD
    #----
    plantD1 = plantD
    hitbox_plantD1 = plantD1.get_rect()
    hitbox_plantD1.x = 560
    hitbox_plantD1.y = 190
    #----
    plantD2 = plantD
    hitbox_plantD2 = plantD2.get_rect()
    hitbox_plantD2.x = 390
    hitbox_plantD2.y = 10
    #----
    libreria5 = libreria
    hitbox_libreria5 = libreria5.get_rect()
    hitbox_libreria5.x = 830
    hitbox_libreria5.y = 440
    #----
    plantD3 = plantD
    hitbox_plantD3 = plantD3.get_rect()
    hitbox_plantD3.x = 1100
    hitbox_plantD3.y = 410
    #----
    plantD4 = plantD
    hitbox_plantD4 = plantD4.get_rect()
    hitbox_plantD4.x = 488
    hitbox_plantD4.y = 410
    #----
    libreria6 = libreria
    hitbox_libreria6 = libreria6.get_rect()
    hitbox_libreria6.x = 280
    hitbox_libreria6.y = 540
    #----
    libreriaP2 = libreriaP
    hitbox_libreriaP2 = libreriaP2.get_rect()
    hitbox_libreriaP2.x = 594
    hitbox_libreriaP2.y = 540
    #----
    marc2 = marc
    #----
    limite = pygame.Rect(-20,0,20,650)
    limite2 = pygame.Rect(1200,0,20,650)
    #----Lista de las imagenes y sus posiciones----#
    generar_imagenes = [[muro14,477,180],[muro25,810,180],[muro1,-20,400],[muro2,250,400],[muro3,250,180],[muro4,-20,180],[muro5,358,180],
                        [muro6,358,-100],[muro11,628,180],[muro12,628,400],[muro7,0,0],[muro8,179,0],[muro9,358,400],
                        [muro15,387,0],[muro16,566,0],[muro17,745,0],[muro18,924,0],[muro19,1103,0],[muro20,810,180],
                        [muro20,810,0],[muro21,810,400],[muro22,1079,400],[muro24,1079,180],[cofre,1000,100],[libreria1,0,440],
                        [libreria2,120,40],[libreriaM1,288,40],[libreriaP1,380,440],[libreriaM2,420,440],[libreria3,640,40],
                        [libreria4,460,40],[libreriaM3,900,220],[libreriaM4,1100,220],[plant1,50,50],[plant2,40,220],[marc1,100,220],
                        [marcD2,500,220],[plantD1,560,190],[plantD2,390,10],[libreria5,830,440],[plantD3,1100,410],[plantD4,488,410],
                        [libreria6,280,540],[libreriaP2,594,540],[marc2,1150,440]]
    #----Lista de hitboxs----#
    verificar_colisiones = [hitbox_muro1,hitbox_muro2,hitbox_muro3,hitbox_muro4,
                            hitbox_muro9,hitbox_muro14,hitbox_uni1,hitbox_uni3,
                            hitbox_uni4,hitbox_uni5,hitbox_muro21,hitbox_muro22,
                            hitbox_uni6,hitbox_muro25,hitbox_muro24,hitbox_libreria1,
                            hitbox_libreria2,hitbox_libreriaM1,hitbox_libreriaP1,
                            hitbox_libreriaM2,hitbox_libreria3,hitbox_libreria4,
                            hitbox_libreriaM3,hitbox_libreriaM4,hitbox_plant1,
                            hitbox_plant2,hitbox_plantD1,hitbox_plantD2,hitbox_libreria5,
                            hitbox_plantD3,hitbox_plantD4,hitbox_libreria6,hitbox_libreriaP2,limite,limite2]
    #-Lista para destruir las puertas cuando la respuesta sea correcta-#
    destruir = [destroy_door1,destroy_door2,destroy_door3,destroy_door4,destroy_door5,destroy_door6]
    #------Juego------#
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        estado = pygame.key.get_pressed()
        if estado[pygame.K_LEFT]:
            x -= velocidad
            direccion = "izquierda"
            frame += 1
            if frame >= frameM:
                contador += 1
                frame = 0
        elif estado[pygame.K_RIGHT]:
            x += velocidad
            direccion = "derecha"
            frame += 1
            if frame >= frameM:
                contador += 1
                frame = 0
        elif estado[pygame.K_UP]:
            y -= velocidad
            direccion = "arriba"
            frame += 1
            if frame >= frameM:
                contador += 1
                frame = 0
        elif estado[pygame.K_DOWN]:
            y += velocidad
            direccion = "abajo"
            frame += 1
            if frame >= frameM:
                contador += 1
                frame = 0
        else:
            direccion = "quieto"
            contador = 0
        #---Hitbox del jugador---#
        jugador_recta.topleft = (x-78,y-55)
        hitbox_jugador.topleft = (jugador_recta.x+100,jugador_recta.y+100)
        #---Colisiones---#
        for hitbox in verificar_colisiones:
           if hitbox_jugador.colliderect(hitbox):
             bloquear_estado()
             break
        #-----Puerta 1/Pregunta 1---#
        if hitbox_jugador.colliderect(hitbox_door1):
            seleccion = 0
            mostrar_pregunta()
        #-----Puerta2/pregunta 2---#
        if hitbox_jugador.colliderect(hitbox_door2):
            seleccion = 1
            mostrar_pregunta()
        #----Puerta 3/ pregunta 3
        if hitbox_jugador.colliderect(hitbox_door3):
            seleccion = 2
            mostrar_pregunta()
        #-Puerta 4/ pregunta 4
        if hitbox_jugador.colliderect(hitbox_door4):
            seleccion = 3
            mostrar_pregunta()
        #-Puerta 5/ pregunta 5
        if hitbox_jugador.colliderect(hitbox_door5):
            seleccion = 4
            mostrar_pregunta()
        #-Puerta 6/ pregunta 6
        if hitbox_jugador.colliderect(hitbox_door6):
            seleccion = 5
            mostrar_pregunta()
        #---Movimiento--#
        ventana.fill("WHITE")
        ventana.blit(fondo1, (0,0))
        #---Habitacion 1----#
        if door1_visible:
          ventana.blit(door1,(160,400))
        #-Mostrar imagenes-#
        for i in range(0,len(generar_imagenes)):
            b = generar_imagenes[i]
            ventana.blit(b[0],(b[1],b[2]))
        #--Habitacion 2---#
        if door2_visible:
          ventana.blit(door1,(160,180))
        #--Puerta 3--#
        if door3_visible:
           ventana.blit(door3,(538,400))
        #-Puerta 4
        if door4_visible:
           ventana.blit(door4,(388,180))
        #-Puerta 5
        if door5_visible:
            ventana.blit(door5,(990,400))
        #-Puerta 6/ pregunta 6
        if door6_visible:
            ventana.blit(door5,(990,180))
        #----COFRE----#
        if hitbox_jugador.colliderect(hitbox_cofre):
            game_over()
        #------
        animaciones(direccion, contador)
        pygame.display.flip()
        reloj.tick(fps)
    

    