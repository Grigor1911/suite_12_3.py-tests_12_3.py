import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_challenge(self):
        self.assertEqual(1 + 1, 2)

    def test_run(self):
        self.assertTrue(True)

    def test_walk(self):
        self.assertFalse(False)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    def test_first_tournament(self):
        self.assertEqual(2 * 2, 4)

    def test_second_tournament(self):
        self.assertTrue(False)

    def test_third_tournament(self):
        self.assertIn(1, [1, 2, 3])