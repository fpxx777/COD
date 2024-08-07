from bala import comprobar_bala
from botiquin import Botiquin
import random

class Guerrero:
    def __init__(self,nombre, municion, tipo_bala, vida, escudo):
        self.nombre = nombre
        self.municion = municion
        self.tipo_bala = tipo_bala
        self.vida = vida
        self.escudo = escudo
        self.maxvida = vida
        self.maxescudo = escudo
        self.botiquines = []

    def disparar(self, guerrero):
        self.municion -= 1
        if self.municion == 0:
            print(f"{self.nombre} no tiene municion! Esta recargando")
            return
        else:
            num = random.randint(0, 10)
            if num <= comprobar_bala(self.tipo_bala).prob:
                print(f"{self.nombre} disparo a {guerrero.nombre}")
                guerrero.recibir_bala(comprobar_bala(self.tipo_bala))
            else:
                print(f"{self.nombre} fallo la bala!")
            print(f"a {self.nombre} le quedan {self.municion} balas")
            return
    def recibir_bala(self, dano):
        if self.escudo == 0:
            self.vida -= dano.dano_vida
        else: 
            self.escudo -= dano.dano_escudo
            if self.escudo <= 0:
                self.vida = self.vida - self.escudo
                self.escudo = 0
        print(f"{self.nombre} tiene {self.escudo} puntos de escudo y {self.vida} puntos de vida")

    def usar_botiquin(self, botiquin):
        if self.escudo == self.maxescudo:
            if self.vida == self.maxvida:
                print("No es necesario usar un botiquin")
            else:
                self.vida += botiquin.cura_vida
                if self.vida > self.maxvida:
                    self.vida - self.maxvida
                    self.escudo += self.vida
                    self.vida = self.maxvida
                print(f"{self.nombre} ahora tiene {self.escudo} puntos de escudo y {self.vida} puntos de vida")
        elif self.escudo == 0:
            if self.vida < self.maxvida:
                self.vida += botiquin.cura_vida
                if self.vida > self.maxvida:
                    self.vida = self.maxvida
                print(f"{self.nombre} ahora tiene {self.escudo} puntos de escudo y {self.vida} puntos de vida")
            else:
                self.escudo += botiquin.cura_escudo
                if self.escudo > self.maxescudo:
                    self.escudo = self.maxescudo
                print(f"{self.nombre} ahora tiene {self.escudo} puntos de escudo y {self.vida} puntos de vida")                                                                                                             

    def info(self):
        print(f"El Guerrero tiene {self.vida} puntos de vida, {self.escudo} puntos de escudo, cuenta con la bala tipo {self.tipo_bala} y tiene {self.municion} balas")
        return self
    
    
personaje = Guerrero("Yo", 50, "normal", 100, 100)
enemigo = Guerrero("Yatin", 50, "normal", 100, 100)

personaje.disparar(enemigo)
personaje.disparar(enemigo)
personaje.disparar(enemigo)
personaje.disparar(enemigo)
personaje.disparar(enemigo)
personaje.disparar(enemigo)
personaje.disparar(enemigo)
personaje.disparar(enemigo)
personaje.disparar(enemigo)
enemigo.usar_botiquin("basico")
enemigo.usar_botiquin("basico")
