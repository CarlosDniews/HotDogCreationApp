from FabricaConcreta import DogaoLanches, AhmannLanches

tipo = 0
tipos_validos = [1, 2]
while tipo not in tipos_validos:
    tipo =  int(input("Quer do dogão(1) ou Ahmann(2): "))

fabrica = None

if(tipo == 1):
    modelo = 0
    modelos_validos = [1, 2, 3, 4]
    while modelo not in modelos_validos:
        modelo =  int(input("\nEscolha o combo que você quer do Dogão Lanches (1, 2, 3 ou 4): "))

    fabrica = DogaoLanches(modelo)

elif(tipo == 2):
    modelo2 = 0
    modelos_validos = [1, 2, 3, 4]
    while modelo2 not in modelos_validos:
        modelo2 =  int(input("\nEscolha o combo que você quer do Ahmann Lanches (1, 2, 3 ou 4): "))

    fabrica = AhmannLanches(modelo2)

else:
    raise ValueError("Tipo inválido")
