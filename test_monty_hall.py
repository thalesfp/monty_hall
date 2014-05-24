import unittest

from monty_hall import MontyHall


class MontyHallTest(unittest.TestCase):
    def setUp(self):
        self.monty_hall = MontyHall()
        self.door_options = [self.monty_hall.winner_prize,
                             self.monty_hall.loser_prize]

    def test_monty_hall_create_doors(self):
        doors = self.monty_hall.create_doors()
        assert_message = "The doors should contain only %s or %s"\
                         % (self.monty_hall.winner_prize,
                            self.monty_hall.loser_prize)
        for door in doors:
            self.assertIn(door, self.door_options, assert_message)

        assert_message = "The doors should contain a winner prize door"
        self.assertIn(self.monty_hall.winner_prize, doors, assert_message)

        assert_message = "The doors should contain only one winner prize door"
        doors.remove(self.monty_hall.winner_prize)
        self.assertNotIn(self.monty_hall.winner_prize, doors, assert_message)

    def test_monty_hall_get_random_door(self):
        assert_message = "The random door method should return a number " \
                         "between 0 and %s" % self.monty_hall.number_of_doors

        for n in range(0, 100):
            self.assertIn(self.monty_hall.get_random_door(),
                          range(0, self.monty_hall.number_of_doors),
                          assert_message)

    def test_monty_hall_choose_door(self):
        assert_true_message = "The winner prize door should return True"
        assert_false_message = "The loser prize door should return False"

        doors = [self.monty_hall.loser_prize,
                 self.monty_hall.winner_prize,
                 self.monty_hall.loser_prize]

        self.assertFalse(self.monty_hall.choose_door(doors, 0),
                         assert_false_message)
        self.assertTrue(self.monty_hall.choose_door(doors, 1),
                        assert_true_message)
        self.assertFalse(self.monty_hall.choose_door(doors, 2),
                         assert_false_message)

        doors = [self.monty_hall.winner_prize,
                 self.monty_hall.loser_prize,
                 self.monty_hall.loser_prize]

        self.assertTrue(self.monty_hall.choose_door(doors, 0),
                        assert_true_message)
        self.assertFalse(self.monty_hall.choose_door(doors, 1),
                         assert_false_message)
        self.assertFalse(self.monty_hall.choose_door(doors, 2),
                         assert_false_message)

if __name__ == '__main__':
    unittest.main(verbosity=2)