from FabricaCachorroFactory import FabricaDeCachorroQuente, CachorroQuenteAbstrato, BatataFritaAbstrato

class CachorroQuenteCalabresa(CachorroQuenteAbstrato):

    def __init__(self):
        self.pao()
        self.molho()
        self.salsicha()
        self.batataPalha()

    def pao(self):
        print("o pao do cahorro é francês")
    
    def molho(self):
        print("o molho é de salsa com tomate")

    def salsicha(self):
        print("é com calabresa")

    def batataPalha(self):
        print("e com batata palha")

class CachorroQuenteSalsicha(CachorroQuenteAbstrato):

    def __init__(self):
        self.pao()
        self.molho()
        self.salsicha()
        self.batataPalha()

    def pao(self): 
        print("o pao do cachorro é inglês")
    
    def molho(self):
        print("o cachorro é com molho de tomate")

    def salsicha(self):
        print("cachorro com salsicha")

    def batataPalha(self):
        print("e sem batata palha")

class BatataFritaRustica(BatataFritaAbstrato):

    def __init__(self):
        self.batata()
        self.queijo()
        self.bacon()
    
    def batata(self):
        print("com batata rustica")
    
    def queijo(self):
        print("batata com quejo")

    def bacon(self):
        print("batata com bacon")

class BatataFritaNormal(BatataFritaAbstrato):

    def __init__(self):
        self.batata()
        self.queijo()
        self.bacon()
    
    def batata(self):
        print("com batata frita")
    
    def queijo(self):
        print("batata com quejo cheddar")

    def bacon(self):
        print("batata com bacon")