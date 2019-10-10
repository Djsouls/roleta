from random import randint

from util import *

from americanRoulette import AmericanRoulette
from europeanRoulette import EuropeanRoulette
from frenchRoulette import FrenchRoulette

class Game:
    def __init__(self, players, rouletteType):
        self.players = players
        self.roulette = self.getRoulette(rouletteType)

    def start(self):
        while self.roulette.bank.chips > 0 and self.players:
            self.getBets()
            self.getResults()
            self.eliminatePlayers()
        print("Acabou")

    def getBets(self):
        self.roulette.getBets()

    def getResults(self):
        bankProfit = 0
        result = randint(0, 36)
        msg = '\nResultado: {}\n'.format(result)
        for player in self.players:
            if player.bet.betType == 0:
                msg += 'Jogador {} passou\n'.format(player.name)
                pass
            elif result in player.bet.winningRange:
                player.chips += player.bet.winningPrize
                self.roulette.bank.chips -= player.bet.winningPrize
                msg += 'Jogador {} ganhou {}\n'.format(player.name, player.bet.winningPrize)
            else:
                self.roulette.bank.chips += player.bet.betValue
                bankProfit += player.bet.betValue
        msg += 'Banca ganhou {} nessa rodada de apostas'.format(bankProfit)

        print(msg)

    def eliminatePlayers(self):
        for i, player in enumerate(self.players):
            if player.chips <= 0:
                self.players.remove(player)
                print("{} removido do jogo".format(player.name))

    def getRoulette(self, rouletteType):
        if rouletteType == AMERICAN_ROULETTE:
            return AmericanRoulette(self.players)
        elif rouletteType == EUROPEAN_ROULETTE:
            return EuropeanRoulette(self.players)
        else:
            return FrenchRoulette(self.players)