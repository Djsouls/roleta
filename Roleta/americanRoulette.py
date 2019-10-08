from roulette import Roulette
from bet import Bet

class AmericanRoulette(Roulette):
    def __init__(self, players):
        super().__init__(players)

    def getBets(self):
        for player in self.players:
            self.bet(player)

    def bet(self, player):
        super().bet(player)
        betTypes = ['', self.altoBaixo, self.vermelhoPreto, self.parImpar, 
                    self.duzia, self.coluna, self.single, self.split, 
                    self.street, self.square, self.neighborsOfZero]

        if self.betType == 0:
            player.bet = Bet(0, 0, '', '')
            return

        function = betTypes[self.betType]
        function()

        winningPrize = super().getWinningPrize()

        player.bet = Bet(self.betValue, self.betType, self.winningRange, winningPrize)

    def single(self):
        print('Selecione um número entre 0 e 36. Você pode escolher 00 também.')
        selected = input()
        if selected != '00':
            selected = int(selected)
        self.resultRange = [selected]

    def neighborsOfZero(self):
        options = [['00', 0], [0, 1], [0, 2], 
                   ['00', 2], 
                   ['00', 3], 
                   ['00', 0, 2],
                   ['00', 0, 1, 2, 3],]

        print('Selecione a coluna')

        for num, row in enumerate(options):
            print('{} - {}'.format(num, row))

        selected = int(input())
        self.resultRange = options[selected]
