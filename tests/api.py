import unittest
import carseour

"""
Run tests from the main carseour directory: python -m unittest tests.api
"""
class TestAPI(unittest.TestCase):
    def setUp(self):
        self.data = carseour.live()

    def tearDown(self):
        pass

    def test_valid_api(self):
        self.assertEqual(self.data.mVersion, carseour.definitions.SHARED_MEMORY_VERSION)

    def test_wheels(self):
        wheels = self.data.wheels()
        idx = 0

        for wheel in wheels:
            self.assertEqual(wheel['tyre']['rps'], self.data.mTyreRPS[idx])
            idx += 1

    def test_players(self):
        players = self.data.players()

        self.assertGreater(len(players), 0)
        self.assertEqual(len(players), self.data.mNumParticipants)
