from guerrero import Guerrero
from bala import Bala, bala_dura
from botiquin import Botiquin
import random


valid_responses = ["1", "2", "tanque", "atacante"]
valid_botiquines = ["basico", "grande"]

def batalla():
    print("Bienvenido al cod!")
    print("elige la clase de tu personaje:")
    selection = False
    while (not selection):
        print("clase 1. tanque")
        print(" Cuenta con 100 puntos de vida, 100 puntos de escudo, 50 balas, con balas tipo normal las cuales quitan 5 puntos de vida")
        print()
        print("clase 2. atacante")
        print(" Cuenta con 50 puntos de vida, 80 puntos de escudo, 40 balas, con balas tipo dura las cuales quitan 10 puntos de vida")
        print()
        response = input("selecciona una clase: ")
        if response.lower() in valid_responses:
            name = input("Ingresa tu nombre: ")
            if response.lower() in ["1", "tanque"]:
                personaje  = Guerrero(name, 50, "normal", 100, 100)
            elif response.lower() in ["2", "atacante"]:
                personaje  = Guerrero(name, 40, "dura", 50, 80)
            selection = True
        else: print("respuesta invalida!")
    print("Seleccion echa")
    print()
    print("empieza la ronda de enemigos, a ver cuantos derrotas!!")
    alive = False
    while (not alive):
        print("Aparecio un enemigo!")
        enemigo = Guerrero("rival", 20, "normal", 30, 40)
        num = random.randint(0,1)
        if num > 0:
            enemigo.disparar(personaje)
        else:
            personaje.disparar(enemigo)
        rival_alive = False
        while (not rival_alive):
            num2 = random.randint(0, 10)
            if num2 > 9:
                num2 = random.randint(0, 10)
                if num2 >= 7:
                    print("encontraste un botiquin grande!!!")
                    personaje.botiquines.append(Botiquin(20, 40))
                else:
                    print("encontraste un botiquin basico!!!")
                    personaje.botiquines.append(Botiquin(10, 20))
            else: pass
            print(f"balas disponibles: {personaje.municion} botiquines disponibles: basicos{personaje.cantidad_botiquines_basicos} y grandes: {personaje.cantidad_botiquines_grandes}")
            response = input("¿disparar o curarte?")
            if response.lower() == "disparar":
                personaje.disparar(enemigo)
                if enemigo.vida <= 0:
                    rival_alive = True
            elif response.lower() == "curarte":
                
        

if __name__ == "__main__":
    batalla()