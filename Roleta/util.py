AMERICAN_ROULETTE = 1
EUROPEAN_ROULETTE = 2
CUCK_ROULETTE = 3

def showRouletteTypes():
    print('+====================================+')
    print('+ 1 - Americana                      +')
    print('+ 2 - Europeia                       +')
    print('+ 3 - Francesa                       +')
    print('+====================================+')

def getRouletteType():
    print("Escolha o tipo da roleta")
    showRouletteTypes()
    return int(input())