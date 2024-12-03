import unittest
from tests_12_3 import RunnerTest, TournamentTest

def skip_if_frozen(test_method):
    def wrapper(self):
        if getattr(self, 'is_frozen', False):
            raise unittest.SkipTest("Тесты в этом кейсе заморожены")
        return test_method(self)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        self.assertEqual(1 + 1, 2)

    @skip_if_frozen
    def test_run(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_walk(self):
        self.assertFalse(False)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertEqual(2 * 2, 4)

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertTrue(False)

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertIn(1, [1, 2, 3])

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(RunnerTest))
    test_suite.addTest(unittest.makeSuite(TournamentTest))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())