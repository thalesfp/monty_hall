import sys
import random


class MontyHall:
    def __init__(self):
        self.number_of_doors = 3
        self.winner_prize = "car"
        self.loser_prize = "goat"

    def create_doors(self):
        doors = [self.loser_prize] * self.number_of_doors
        random_position = random.randint(0, 2)
        doors[random_position] = self.winner_prize

        return doors

    def get_random_door(self):
        return random.randint(0, self.number_of_doors - 1)

    def choose_door(self, doors, position):
        return True if doors[position] == self.winner_prize else False


class PlayMontyHall:
    def __init__(self):
        self.monty_hall = MontyHall()
        self.wins = 0
        self.loss = 0

    def start_game(self):
        doors = self.monty_hall.create_doors()
        chosen_door = self.monty_hall.get_random_door()

        result = self.monty_hall.choose_door(doors, chosen_door)

        # If you guess the answer you will fail because
        # you will change to the wrong door
        if result:
            self.loss = self.loss + 1
        else:
            self.wins = self.wins + 1

    def get_wins(self):
        return self.wins

    def get_loss(self):
        return self.loss


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        number_of_attempts = int(sys.argv[1])
    else:
        number_of_attempts = 250000

    play_monty_hall = PlayMontyHall()
    for n in range(0, number_of_attempts):
        play_monty_hall.start_game()

    print "The wins should be about twice the losses:"
    print "Wins: %s" % play_monty_hall.get_wins()
    print "Loss: %s" % play_monty_hall.get_loss()
