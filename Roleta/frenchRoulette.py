from roulette import Roulette
from bet import Bet

class FrenchRoulette(Roulette):
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
        print('Selecione um número entre 0 e 36')
        selected = int(input())
        self.resultRange = [selected]

    def neighborsOfZero(self):
        options = [[0, 1], [0, 2], [0, 3],
                   [0,1,2], [0,2,3], [0,1,2,3]]
        print('Selecione a coluna')

        for num, row in enumerate(options):
            print('{} - {}'.format(num, row))

        selected = int(input())
        self.resultRange = options[selected]
