class Bala:
    def __init__(self, nombre, dano_vida, dano_escudo, prob):
        self.nombre = nombre
        self.dano_vida = dano_vida
        self.dano_escudo = dano_escudo
        self.prob = prob
bala_dura = Bala("dura", 20, 40, 4)
bala_normal = Bala("normal", 10, 20, 6)

def comprobar_bala(bala):
    if bala == "dura":
        return bala_dura
    elif bala == "normal":
        return bala_normal