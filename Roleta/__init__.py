from util import *

from player import Player
from game import Game

rouletteType = getRouletteType()

players = []
nOfPlayer = int(input("Digite o número de jogadores: "))
for i in range(nOfPlayer):
    playerName = input("Nome do jogador {}: ".format(i+1))
    players.append(Player(playerName))

game = Game(players, rouletteType)

game.start()