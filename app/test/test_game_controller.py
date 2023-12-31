import unittest

import datetime

from app.main import db
from app.main.controller import game_controller
from app.test.base import BaseTestCase

class TestGameController(BaseTestCase):
    def get_by_id(self):
        game = game_controller.get_by_id(1)
        self.assertTrue(game.id)
        self.assertEqual(game.game_name, 'test')
        self.assertEqual(game.game_description, 'test')
        self.assertEqual(game.game_location, 'test')
        self.assertEqual(game.game_start_time, datetime.datetime.utcnow())
        self.assertEqual(game.game_master, 'test')
        self.assertEqual(game.game_assistant, 'test')

    def get_all(self):
        games = game_controller.get_all()
        self.assertTrue(games)
        self.assertEqual(games[0].game_name, 'test')
        self.assertEqual(games[0].game_description, 'test')
        self.assertEqual(games[0].game_location, 'test')
        self.assertEqual(games[0].game_start_time, datetime.datetime.utcnow())
        self.assertEqual(games[0].game_master, 'test')
        self.assertEqual(games[0].game_assistant, 'test')

    def update_a_game(self):
        game = game_controller.update_a_game(1, {
            'gamename': 'test',
            'gamedescription': 'test',
            'gamelocation': 'test',
            'gamemaster': 'test',
            'gameassistant': 'test'
        })
        self.assertTrue(game.id)
        self.assertEqual(game.game_name, 'test')
        self.assertEqual(game.game_description, 'test')
        self.assertEqual(game.game_location, 'test')
        self.assertEqual(game.game_start_time, datetime.datetime.utcnow())
        self.assertEqual(game.game_master, 'test')
        self.assertEqual(game.game_assistant, 'test')

    def delete_a_game(self):
        game = game_controller.delete_a_game(1)
        self.assertTrue(game.id)
        self.assertEqual(game.game_name, 'test')
        self.assertEqual(game.game_description, 'test')
        self.assertEqual(game.game_location, 'test')
        self.assertEqual(game.game_start_time, datetime.datetime.utcnow())
        self.assertEqual(game.game_master, 'test')
        self.assertEqual(game.game_assistant, 'test')
        
if __name__ == '__main__':
    unittest.main()
