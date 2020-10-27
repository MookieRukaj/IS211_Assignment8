import random
import datetime
import argparse


class Die(object):
    def __init__(self, seed):
        if seed is not None:
            random.seed(seed)

    def roll(self):
        return random.randint(1, 6)



def player_factory(player):
    if player == 'human':
        return HumanPlayer(player)
    if player == 'computer':
        return ComputerPlayer(player)
    else:
        print("invalid input")
        exit()




class Player(object):
    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.turns_score = 0



class ComputerPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.strategy = True




class HumanPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.strategy = False



def game_factory(player1, player2, timed=False, seed=None):
    if timed:
        return TimedGame(player1, player2, seed)
    else:
        return Game(player1, player2, seed)




class Game(object):
    def __init__(self, player1, player2, seed=None):
        self.player1 = player1
        self.player2 = player2
        self.die = Die(seed)




def turn(self, player):
        print('\nit is Player {}\'s turn'.format(player.name))
        r = self.die.roll()
        print('\nyou rolled a {}\n'.format(r))
        if r == 1:
            player.turns_score = 0
            print('oops! you rolled a 1, next player.\n'.format(
                player.name, player.total_score))
            print('-' * 60, '\n')
            self.next_player(player)
        else:
            player.turns_score += r
            player.total_score += r
            print('your total this turn is {}\n'.format(player.turns_score))
            if player.total_score >= 100:
                print('{} is the winner with a score of {}!'.format(
                    player.name, player.total_score))
                exit()
            if player.strategy:
                self.strategy(player)
            else:
                self.player_answer(player)


def strategy(self, player):
        if player.turns_score < 25:
            self.turn(player)
        else:
            print('\nyour turn is now over.\n')
            player.turns_score = 0
            print('{}\'s total score is now {}.\n\n'.format(
                player.name, player.total_score))
            print('-' * 60, '\n')
            self.next_player(player)



def player_answer(self, player):
        print('The total for this player is ' + str(player.total_score))
        answer = input(
            'would you like to roll again? r = roll h = hold ').lower()
        if answer == 'h':
            print('\nyour turn is now over.\n')
            player.turns_score = 0
            print('{}\'s total score is now {}.\n\n'.format(
                player.name, player.total_score))
            print('-' * 60, '\n')
            self.next_player(player)
        elif answer == 'r':
            self.turn(player)
        else:
            print('Invalid option, r = roll h = hold')
            self.player_answer(player)




class TimedGame(Game):
    def __init__(self, player1, player2, seed):
        Game.__init__(self, player1, player2, seed)
        self.startTime = datetime.datetime.now()

    def determine_winner(self):
        if self.player1.total_score > self.player2.total_score:
            print('{} is the winner with a score of {}!'.format(
                self.player1.name, self.player1.total_score))
            exit()
        else:
            print('{} is the winner with a score of {}!'.format(
                self.player2.name, self.player2.total_score))
            exit()



def time_out(self):
       stop_time = datetime.datetime.now()
       elapsed_time = stop_time - self.startTime
       if elapsed_time > datetime.timedelta(minutes=1):
           return True
       else:
           return False


def turn(self, player):
        if self.time_out():
            self.determine_winner()
        super(TimedGame, self).turn(player)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--player1')
    parser.add_argument('--player2')
    parser.add_argument('--timed')
    args = parser.parse_args()
    player1 = player_factory(args.player1)
    player2 = player_factory(args.player2)
    game = game_factory(player1, player2, args.timed, 0)
    print('Welcome to pig')
    game.turn(game.player1)




if __name__ == '__main__':
    main()
