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

    def get_winner_prize_position(self, doors):
        for n in xrange(self.number_of_doors + 1):
            if n < len(doors) and doors[n] == self.winner_prize:
                return n


class PlayMontyHall:
    def __init__(self):
        self.monty_hall = MontyHall()
        self.win = 0
        self.loose = 0

    def start_game(self):
        doors = self.monty_hall.create_doors()
        chosen_door = self.monty_hall.get_random_door()

        result = self.monty_hall.choose_door(doors, chosen_door)

        # If you guess the answer you will fail because
        # you will change to the wrong door
        if result:
            self.loose = self.loose + 1
        else:
            self.win = self.win + 1

    def get_win(self):
        return self.win

    def get_loose(self):
        return self.loose

import unittest


class MontyHallTest(unittest.TestCase):
    def setUp(self):
        self.monty_hall = MontyHall()
        self.door_options = [self.monty_hall.winner_prize,
                             self.monty_hall.loser_prize]

    def test_monty_hall_create_doors(self):
        doors = self.monty_hall.create_doors()
        assert_message = "Door one should contain %s or %s"\
                         % (self.monty_hall.winner_prize,
                            self.monty_hall.loser_prize)

        for door in doors:
            self.assertIn(door, self.door_options, assert_message)

    def test_monty_hall_get_random_door(self):
        self.assertIn(self.monty_hall.get_random_door(), range(0, 3))

    def test_monty_hall_choose_door(self):
        doors = ["goat", "car", "goat"]
        self.assertFalse(self.monty_hall.choose_door(doors, 0))
        self.assertTrue(self.monty_hall.choose_door(doors, 1))
        self.assertFalse(self.monty_hall.choose_door(doors, 2))

        doors = ["car", "goat", "goat"]
        self.assertTrue(self.monty_hall.choose_door(doors, 0))
        self.assertFalse(self.monty_hall.choose_door(doors, 1))
        self.assertFalse(self.monty_hall.choose_door(doors, 2))

    def test_monty_hall_get_winner_prize_position(self):
        doors = ["goat", "car", "goat"]
        self.assertEqual(self.monty_hall.get_winner_prize_position(doors), 1)

        doors = ["goat", "goat", "car"]
        self.assertEqual(self.monty_hall.get_winner_prize_position(doors), 2)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        number_of_attempts = int(sys.argv[1])
    else:
        number_of_attempts = 250000

    play_monty_hall = PlayMontyHall()
    for n in range(0, number_of_attempts):
        play_monty_hall.start_game()

    print "Winners: %s" % play_monty_hall.get_win()
    print "Looses: %s" % play_monty_hall.get_loose()