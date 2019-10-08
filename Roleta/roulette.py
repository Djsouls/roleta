from bank import Bank

class Roulette:
    def __init__(self, players):
        self.players = players
        
        self.bank = Bank()
        self.winningRange = []

    def bet(self, player):
        while True:
            self.showBets(player)
            betType = int(input("Escolha a aposta: "))
            self.betType = betType

            if betType == 0 and player.skippedBets >= 3:
                print("Você já passou seu máximo")
                continue
            elif betType == 0:
                player.skippedBets += 1
                return
            break

        while True:
            betValue = int(input("Valor da aposta: "))
            if betValue > player.chips:
                print("Isso é mais do que você pode apostar")
            elif betValue <= 0:
                print("Ha")
            else:
                self.betValue = betValue
                player.chips -= betValue
                break

    def altoBaixo(self):
        options = [list(range(1, 19)), list(range(19, 37))]

        print('Selecione o intervalo')
        print('0 - Baixo')
        print('1 - Alto')
        
        betRange = int(input())
        self.winningRange = options[betRange]

    def vermelhoPreto(self):
        options = [[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36], 
                   [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35],]

        print('Selecione o intervalo')
        print('0 - Vermelho')
        print('1 - Preto')

        betRange = int(input())
        self.winningRange = options[betRange]

    def parImpar(self):
        options = [[i for i in range(1, 37) if i % 2 == 0],
                   [i for i in range(1, 37) if i % 2 == 1],]

        print('Selecione o intervalo')
        print('0 - Par')
        print('1 - Ímpar')

        betRange = int(input())
        self.winningRange = options[betRange]

    def duzia(self):
        options = [list(range(1, 13)), list(range(13, 25)), list(range(25, 37))]
        print('Selecione o intervalo')
        print('0 - 1 até 12')
        print('1 - 13 até 24')
        print('2 - 25 até 36')
        betRange = int(input())
        self.winningRange = options[betRange]

    def coluna(self):
        options = [[3,6,9,12,15,18,21,24,27,30], 
                   [2,5,8,11,14,17,20,23,26,29], 
                   [1,4,7,10,13,16,19,22,25,28],]
        print('Selecione a coluna')

        for num, row in enumerate(options):
            print('{} - {}'.format(num, row))

        betRange = int(input())
        self.winningRange = options[betRange]
        
    def single(self):
        print('Selecione um numero entre 0 e 36')
        betRange = int(input())
        self.winningRange = [betRange]

    def split(self):
        print('Selecione um numero entre 0 e 36')
        firstNumber = int(input())
        options = self.__split_options__(firstNumber)
        
        print('Selecione o segundo número')
        for num, row in enumerate(options):
            print('{} - {}'.format(num, row))

        betRange = int(input())
        self.winningRange = [firstNumber] + options[betRange]
    
    def street(self):
        options = [[i+1, i+2, i+3] for i in range(0, 36, 3)]
        print('Selecione o intervalo')

        for num, row in enumerate(options):
            print('{} - {}'.format(num, row))

        betRange = int(input())
        self.winningRange = options[betRange]

    def square(self):
        print('Selecione um numero entre 1 e 36')
        firstNumber = int(input())
        options = self.__square_options__(firstNumber)
        
        print('Selecione o quadrado que você quer')
        for num, row in enumerate(options):
            print('{} - {}'.format(num, row))

        betRange = int(input())
        self.winningRange = [firstNumber] + options[betRange]

    def __split_options__(self, firstNumber):
        options = []

        if firstNumber % 3 != 0:
            options.append(firstNumber - 1)

        if firstNumber % 3 != 1:
            options.append(firstNumber + 1)

        if firstNumber < 34:
            options.append(firstNumber - 3)

        if firstNumber > 3:
            options.append(firstNumber + 3)
            
        return options

    def __square_options__(self, firstNumber):
        options = []

        upper_left = (firstNumber % 3) != 1 and firstNumber > 3
        upper_right = (firstNumber % 3) != 0 and firstNumber > 3
        lower_left = (firstNumber % 3) != 1 and firstNumber < 34
        lower_right = (firstNumber % 3) != 1 and firstNumber < 34

        if upper_left:
            options = [firstNumber-4, firstNumber-3, firstNumber-1, firstNumber]

        if upper_right:
            options = [firstNumber-3, firstNumber-2, firstNumber, firstNumber+1]

        if lower_left:
            options = [firstNumber-1, firstNumber, firstNumber+2, firstNumber+3]

        if lower_right:
            options = [firstNumber, firstNumber+1, firstNumber+3, firstNumber+4]
        
        return options

    def getWinningPrize(self):
        return self.betValue * (36 // len(self.winningRange))

    def showBets(self, player):
        print('Dinheiro da banca: {}'.format(self.bank.chips))
        print('Jogador: {}'.format(player.name))
        print('Seu dinheiro: {}'.format(player.chips))
        print('Rounds passados: {}'.format(player.skippedBets))
        print('********************************')
        print('Selecione o tipo de aposta:     ')
        print('                                ')
        print('0 - Passar                      ')
        print('1 - Alto ou baixo               ')
        print('2 - Vermelho ou preto           ')
        print('3 - Par ou ímpar                ')
        print('4 - Dúzia                       ')
        print('5 - Coluna                      ')
        print('6 - Single                      ')
        print('7 - Split                       ')
        print('8 - Street                      ')
        print('9 - Quadrado                    ')

        print('10 - Vizinho do zero            ')
        print('********************************')