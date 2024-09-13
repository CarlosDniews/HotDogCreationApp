from FabricaCachorroFactory import FabricaDeCachorroQuente, CachorroQuenteAbstrato, BatataFritaAbstrato
from ProdutosConcretos import CachorroQuenteCalabresa, CachorroQuenteSalsicha, BatataFritaRustica, BatataFritaNormal

class DogaoLanches(FabricaDeCachorroQuente):

    def __init__(self, combo):
        self.criaCachorro(combo)
        self.prepara()
        self.assa()
        self.empacota()

    def criaCachorro(self, modelo):
        if (modelo == 1):
            self.cachorros = CachorroQuenteCalabresa()

        elif (modelo == 2):
            self.cachorros = CachorroQuenteCalabresa()
            self.batata = BatataFritaRustica()

        elif (modelo == 3):
            self.cachorros = CachorroQuenteSalsicha()

        elif (modelo == 4):
            self.cachorros = CachorroQuenteSalsicha()
            self.batata = BatataFritaNormal()

    def prepara(self): 
        print("preparando pedido do dogão")

    def assa(self): 
        print("seu pedido do dogão está no forno")

    def empacota(self):
        print("empacotando seu pedido do dogão") 
        
class AhmannLanches(FabricaDeCachorroQuente):

    def __init__(self, combo):
        self.criaCachorro(combo)
        self.prepara()
        self.assa()
        self.empacota()
    

    def criaCachorro(self, modelo):
        if(modelo == 1):
            self.dog = CachorroQuenteCalabresa()
            self.batata = BatataFritaNormal()

        elif (modelo == 2):
            self.dog = CachorroQuenteCalabresa()
            self.batata = BatataFritaRustica()

        elif (modelo == 3):
            self.dog = CachorroQuenteSalsicha()
            self.batata = BatataFritaRustica()

        elif (modelo == 4):
            self.dog = CachorroQuenteSalsicha()
            self.batata = BatataFritaNormal()

    def prepara(self): 
        print("preparando pedido do Ahmann Lanches")

    def assa(self): 
        print("seu pedido do Ahmann Lanches está no forno")

    def empacota(self):
        print("empacotando seu pedido do Ahmann Lanches") 