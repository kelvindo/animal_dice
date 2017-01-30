import random
from numpy import mean
from numpy import std

# Define the number of times you want to play the game
NUM_ITERATIONS = 1000000

# Generic Player Class
class Player:

  def __init__(self):
    self.winnings = []


# Specific implementations of different playing strategies

# Bet all your money on 1
class SingleBetPlayer(Player):

  def name(self):
    return "Single Bet Player"

  def bet(self):
    return {1: 3}

# Split your bet into three equal bets on 1, 2, 3
class TripleBetPlayer(Player):

  def name(self):
    return "Triple Bet Player"

  def bet(self):
    return {1: 1, 2: 1, 3: 1}

# Bet two on 1 and one on 2
class TwoOnePlayer(Player):

  def name(self):
    return "Two One Player"

  def bet(self):
    return {1: 2, 2: 1}

# Randomly choose different bets every turn
class RandomPlayer(Player):

  def name(self):
    return "Random Player"

  def bet(self):
    bet_map = {}
    for i in range (0, 3):
      rand_int = random.randint(1, 6)
      if rand_int not in bet_map:
        bet_map[rand_int] = 0

      bet_map[rand_int] += 1

    return bet_map

# Bet 50 cents on all 6
class AllBetPlayer(Player):

  def name(self):
    return "All Bet Player"

  def bet(self):
    return {1: .5,
            2: .5,
            3: .5,
            4: .5,
            5: .5,
            6: .5}

# Game Class that holds all the players and iteration info
class Game:
  def __init__(self, num_iterations):
    self.num_iterations = num_iterations
    self.games_played = 0
    self.players = [SingleBetPlayer(), 
                    TripleBetPlayer(),
                    TwoOnePlayer(),
                    RandomPlayer(),
                    AllBetPlayer()]
    self.dice_dist = {1: 0,
                      2: 0,
                      3: 0,
                      4: 0,
                      5: 0, 
                      6: 0}

  # rolls 3 random dice and return them as a map of number occurences
  def roll_dice(self):
    dice_map = {1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0, 
                6: 0}
    for i in range (0, 3):
      rand_int = random.randint(1, 6)
      dice_map[rand_int] += 1
      self.dice_dist[rand_int] += 1

    return dice_map

  # play one iterations of the game for all players
  def play_iteration(self):
    dice_map = self.roll_dice()

    for player in self.players:
      payout = -3
      bet = player.bet()
      for number, amount in bet.iteritems():
        if dice_map[number] > 0:
          payout += amount * (dice_map[number] + 1)

      player.winnings.append(payout)

    self.games_played += 1
    if self.games_played % 10000 == 0:
      print self.games_played * 1.0 / self.num_iterations


  # play all iterations of the game and print the results
  def play(self):
    for i in range(0, self.num_iterations):
      self.play_iteration()

    print "Num Iterations: " + str(self.num_iterations)

    for player in self.players:
      print "---------------------------------------"
      print player.name()
      print "Total Net: " + str(sum(player.winnings))
      print "Average: " + str(mean(player.winnings))
      print "Payout: " + str((mean(player.winnings) + 3) / 3)
      print "Standard Dev: " + str(std(player.winnings))
      print "---------------------------------------"


    print self.dice_dist

game = Game(NUM_ITERATIONS)
game.play()
