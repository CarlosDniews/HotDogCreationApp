from abc import ABCMeta, abstractmethod

class FabricaDeCachorroQuente(metaclass=ABCMeta):

    @abstractmethod
    def criaCachorro(self, tipo): pass

    @abstractmethod
    def prepara(self): pass

    @abstractmethod
    def assa(self): pass

    @abstractmethod
    def empacota(self): pass

class CachorroQuenteAbstrato(metaclass=ABCMeta):

    @abstractmethod
    def pao(self, pao): pass

    @abstractmethod
    def molho(self, molho): pass

    @abstractmethod
    def salsicha(self, salsicha): pass

    @abstractmethod
    def batataPalha(self, batata): pass

class BatataFritaAbstrato(metaclass=ABCMeta):

    @abstractmethod
    def batata(self, batata): pass

    @abstractmethod
    def queijo(self, queijo): pass

    @abstractmethod
    def bacon(self, bacon): pass