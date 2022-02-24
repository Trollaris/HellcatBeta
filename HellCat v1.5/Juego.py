from Jugador import nombre, ataquejugador, vidajugador, manajugador, energiajugador, costeCuracion, curacion
from Enemigos import VidaGoblin, nombreGoblin, ataqueGoblin
from Razas import vidaHumano,vidaDr,vidaDuende,vidaElfo,vidaEnano,vidaOrco,vidaTf, ataqueDr, ataqueDuende,ataqueElfo,ataqueEnano,ataqueHumano,ataqueOrco,ataqueTf, manaDr,manaDuende,manaElfo,manaEnano,manaHumano,manaOrco,manaTf ,humano,duende,elfo,enano,orco,tiflin,Draconate ,energiaDr,energiaDuende,energiaElfo,energiaEnano,energiaHumano,energiaTf
from Razas import energiaOr, manaHombre, ataqueHombre, energiaHombre, vidaHombre, WolfMan

#Aqui empieza el juego!!!
print("Bienvenido jugador a HellCat...")
nombre = input("¿Como te llamas, jugador? ")
print("Encantado de conocerte, " + nombre)
print("Que raza te gustaria escoger?? a-Humano / s-Duende / d-Enano / f-Elfo / q-Orco / w-Tiflin / e-Draconate ")
raza = input() 
if raza == "a":
    vidajugador += vidaHumano
    manajugador += manaHumano
    ataquejugador += ataqueHumano
    energiajugador += energiaHumano
    print("Bienbenido " + humano)
    print("Tu vida: " + str(vidajugador))
    print("Tu ataque: " + str(ataquejugador))
    print("Tu energia: " + str(energiajugador))
    print("Tu mana: " + str(manajugador))
elif raza == "s":
    vidajugador += vidaDuende
    manajugador += manaDuende
    ataquejugador += ataqueDuende
    energiajugador += energiaDuende
    print("Bienbenido " + duende)
    print("Tu vida: " + str(vidajugador))
    print("Tu ataque: " + str(ataquejugador))
    print("Tu energia: " + str(energiajugador))
    print("Tu mana: " + str(manajugador))
elif raza == "d":
    vidajugador += vidaEnano
    manajugador += manaEnano
    ataquejugador += ataqueEnano
    energiajugador += energiaEnano
    print("Bienbenido " + enano)
    print("Tu vida: " + str(vidajugador))
    print("Tu ataque: " + str(ataquejugador))
    print("Tu energia: " + str(energiajugador))
    print("Tu mana: " + str(manajugador))
elif raza == "f":
    vidajugador += vidaElfo
    manajugador += manaElfo
    ataquejugador += ataqueElfo
    energiajugador += energiaElfo
    print("Bienbenido " + elfo)
    print("Tu vida: " + str(vidajugador))
    print("Tu ataque: " + str(ataquejugador))
    print("Tu energia: " + str(energiajugador))
    print("Tu mana: " + str(manajugador))
elif raza == "q":
    vidajugador += vidaOrco
    manajugador += manaOrco
    ataquejugador += ataqueOrco
    energiajugador += energiaOr
    print("Bienbenido " + orco)
    print("Tu vida: " + str(vidajugador))
    print("Tu ataque: " + str(ataquejugador))
    print("Tu energia: " + str(energiajugador))
    print("Tu mana: " + str(manajugador))
elif raza == "w":
    vidajugador += vidaTf
    manajugador += manaTf
    ataquejugador += ataqueTf
    energiajugador += energiaTf
    print("Bienbenido " + tiflin)
    print("Tu vida: " + str(vidajugador))
    print("Tu ataque: " + str(ataquejugador))
    print("Tu energia: " + str(energiajugador))
    print("Tu mana: " + str(manajugador))
elif raza == "e":
    vidajugador += vidaDr
    manajugador += manaDr
    ataquejugador += ataqueDr
    energiajugador += energiaDr
    print("Bienbenido " + Draconate)
    print("Tu vida: " + str(vidajugador))
    print("Tu ataque: " + str(ataquejugador))
    print("Tu energia: " + str(energiajugador))
    print("Tu mana: " + str(manajugador))      
elif raza == "r":
    vidajugador += vidaHombre
    manajugador += manaHombre
    ataquejugador += ataqueHombre
    energiajugador += energiaHombre
    print("Bienbenido " + WolfMan)
    print("Tu vida: " + str(vidajugador))
    print("Tu ataque: " + str(ataquejugador))
    print("Tu energia: " + str(energiajugador))
    print("Tu mana: " + str(manajugador))      

print("Esta es tu historia " + nombre + " bienvidido a Corfty la ciudad..., bueno en realidad estas en una celda en el viejo manicomio de corfty. ")
print("Espera que es eso ... ¿Que es ese ruido?... sera mejor que salgas de aqui corre por la trampilla")
salida =""
salida = input("Que deseas hacer?? a-salir por la escotilla / s-revisar si hay algo en la celda: " )
if salida == "a":
    print("Has decidido salir por la trampilla. " )
elif salida == "s":
    print(" Has decidido buscar en la celda pero no has encontrado nada :(. ")    
    salida = input("Que deseas hacer?? a-salir por la escotilla / s-revisar si hay algo en la celda: " )
    if salida == "a":
        print("Has decidido salir por la trampilla. " )
    elif salida == "s":
        print(" Otra vez tu?!? toma tu objeto... Has recibido una pintada de dedo JAJAJAJA y has salido de la celda.")     

    
print("Al salir de la celda te has tropezado con una extraña criatura... ")
#Presentamos al enemigo
print("Ha aparecido un " + nombreGoblin)
respuesta = ""
respuesta = input("¿Que deseas hacer? a-Atacar / s-curar: ")
if respuesta == "a":
    print("¡Has decidido atacar!")
    VidaGoblin -= ataquejugador 
    print(VidaGoblin)
elif respuesta == "s":
    if vidajugador >= 100:
        print("¡No te puedes curar más!")
    elif vidajugador < 100:
        print("¡Has decidido curarte!")
        manajugador -= costeCuracion 
        vidajugador += curacion
    print("Tu vida: " + str(vidajugador))
    print("Tu energia: " + str(energiajugador))
    print("Tu mana: " + str(manajugador))
    print("Vida del enemigo: " + str(VidaGoblin))   
    print("El " + nombreGoblin + " te ataca por "+ str(ataqueGoblin))
    vidajugador -= ataqueGoblin
    print("Tu vida: " + str(vidajugador))
    print("Tu energia: " + str(energiajugador))
    print("Tu mana: " + str(manajugador))
    print("Vida del enemigo: " + str(VidaGoblin))
respuesta = input("¿Que deseas hacer? a-Atacar / s-curar: ")
if respuesta == "a":
    print("¡Has decidido atacar!")
    VidaGoblin -= ataquejugador 
    print(VidaGoblin)
elif respuesta == "s":
    if vidajugador >= 100:
        print("¡No te puedes curar más!")
    elif vidajugador < 100:
        print("¡Has decidido curarte!")
        manajugador -= costeCuracion 
        vidajugador += curacion
    print("Tu vida: " + str(vidajugador))
    print("Tu energia: " + str(energiajugador))
    print("Tu mana: " + str(manajugador))
    print("Vida del enemigo: " + str(VidaGoblin))   
    print("El " + nombreGoblin + " te ataca por "+ str(ataqueGoblin))
    vidajugador -= ataqueGoblin
    print("Tu vida: " + str(vidajugador))
    print("Tu energia: " + str(energiajugador))
    print("Tu mana: " + str(manajugador))
    print("Vida del enemigo: " + str(VidaGoblin))

print("Esa estuvo muy cera " + nombre + ", parece que ya estamos a salvo.")
print("Me presento yo soy Leeroy Jenkins!! y te estare acompañando en tu aventura")
print("¿Que te parece si salimos de aqui?")









