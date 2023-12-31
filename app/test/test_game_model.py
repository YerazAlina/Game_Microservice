import unittest

import datetime

from app.main import db
from app.main.model.game import Game
from app.test.base import BaseTestCase

class TestGameModel(BaseTestCase):
    
    def test_game_creation(self):
        game = Game(
            game_name='test',
            game_description='test',
            game_location='test',
            game_start_time=datetime.datetime.utcnow(),
            game_master='test',
            game_assistant='test'
        )
        db.session.add(game)
        db.session.commit()
        self.assertTrue(game.id)
        self.assertEqual(game.game_name, 'test')
        self.assertEqual(game.game_description, 'test')
        self.assertEqual(game.game_location, 'test')
        self.assertEqual(game.game_start_time, datetime.datetime.utcnow())
        self.assertEqual(game.game_master, 'test')
        self.assertEqual(game.game_assistant, 'test')  
    
if __name__ == '__main__':
    unittest.main()