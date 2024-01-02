import unittest
from unittest.mock import Mock
from app.main.controller.game_controller import Game, GameList

class TestGameController(unittest.TestCase):

    def setUp(self):
        self.mock_game_service = Mock()
        self.game_controller_gamelist = GameList(self.mock_game_service)

    def test_get_all_games(self):
        expected_games = [{'id': 1, 'gamename': 'test', 'gamedescription': 'test', 'gamelocation': 'test', 'gamestarttime': 'test', 'gamemaster': 'test', 'gameassistant': 'test'}]
        self.mock_game_service.list_of_games.return_value = expected_games

        result = self.game_controller_gamelist.get()

        self.assertEqual(result, expected_games)
        self.mock_game_service.get_all_games.assert_called_once_with()

if __name__ == '__main__':
    unittest.main()
