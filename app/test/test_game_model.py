import unittest

import datetime

from app.main import db
from app.main.model.game import Game
from app.test.base import BaseTestCase

class TestGame(BaseTestCase):
    
    def test_create_game(self):
        game = Game(
            gamename='test',
            gamedescription='test',
            gamelocation='test',
            gamestarttime=datetime.datetime.utcnow(),
            gamemaster='test',
            gameassistant='test'
        )
        db.session.add(game)
        db.session.commit()
        self.assertTrue(game.id)
        self.assertEqual(game.gamename, 'test')
        self.assertEqual(game.gamedescription, 'test')
        self.assertEqual(game.gamelocation, 'test')
        self.assertEqual(game.gamestarttime, game.gamestarttime)
        self.assertEqual(game.gamemaster, 'test')
        self.assertEqual(game.gameassistant, 'test')

    def test_get_all_games(self):
        game1 = Game(
            gamename='test',
            gamedescription='test',
            gamelocation='test',
            gamestarttime=datetime.datetime.utcnow(),
            gamemaster='test',
            gameassistant='test'
        )
        game2 = Game(
            gamename='test',
            gamedescription='test',
            gamelocation='test',
            gamestarttime=datetime.datetime.utcnow(),
            gamemaster='test',
            gameassistant='test'
        )
        db.session.add(game1)
        db.session.add(game2)
        db.session.commit()
        games = Game.query.all()
        self.assertEqual(len(games), 2)
        self.assertEqual(games[0].gamename, 'test')
        self.assertEqual(games[0].gamedescription, 'test')
        self.assertEqual(games[0].gamelocation, 'test')
        self.assertEqual(games[0].gamestarttime, games[0].gamestarttime)
        self.assertEqual(games[0].gamemaster, 'test')
        self.assertEqual(games[0].gameassistant, 'test')
        self.assertEqual(games[1].gamename, 'test')
        self.assertEqual(games[1].gamedescription, 'test')
        self.assertEqual(games[1].gamelocation, 'test')
        self.assertEqual(games[1].gamestarttime, games[1].gamestarttime)
        self.assertEqual(games[1].gamemaster, 'test')
        self.assertEqual(games[1].gameassistant, 'test')
    
    def test_get_all_games_empty(self):
        games = Game.query.all()
        self.assertEqual(len(games), 0)

    def test_get_game_by_id(self):
        game = Game(
            gamename='test',
            gamedescription='test',
            gamelocation='test',
            gamestarttime=datetime.datetime.utcnow(),
            gamemaster='test',
            gameassistant='test'
        )
        db.session.add(game)
        db.session.commit()
        game = Game.query.filter_by(id=game.id).first()
        self.assertEqual(game.gamename, 'test')
        self.assertEqual(game.gamedescription, 'test')
        self.assertEqual(game.gamelocation, 'test')
        self.assertEqual(game.gamestarttime, game.gamestarttime)
        self.assertEqual(game.gamemaster, 'test')
        self.assertEqual(game.gameassistant, 'test')

    def test_get_game_by_nonexisting_id(self):
        game = Game.query.filter_by(id=0).first()
        self.assertEqual(game, None)
    
    def test_delete_game(self):
        game = Game(
            gamename='test',
            gamedescription='test',
            gamelocation='test',
            gamestarttime=datetime.datetime.utcnow(),
            gamemaster='test',
            gameassistant='test'
        )
        db.session.add(game)
        db.session.commit()
        game = Game.query.filter_by(id=game.id).first()
        db.session.delete(game)
        db.session.commit()
        game = Game.query.filter_by(id=game.id).first()
        self.assertEqual(game, None)

    def test_delete_nonexisting_game(self):
        game = Game.query.filter_by(id=0).first()
        self.assertEqual(game, None)
    
    def test_update_game(self):
        game = Game(
            gamename='test',
            gamedescription='test',
            gamelocation='test',
            gamestarttime=datetime.datetime.utcnow(),
            gamemaster='test',
            gameassistant='test'
        )
        db.session.add(game)
        db.session.commit()
        game = Game.query.filter_by(id=game.id).first()
        game.gamename = 'test2'
        game.gamedescription = 'test2'
        game.gamelocation = 'test2'
        game.gamestarttime = game.gamestarttime
        game.gamemaster = 'test2'
        game.gameassistant = 'test2'
        db.session.commit()
        game = Game.query.filter_by(id=game.id).first()
        self.assertEqual(game.gamename, 'test2')
        self.assertEqual(game.gamedescription, 'test2')
        self.assertEqual(game.gamelocation, 'test2')
        self.assertEqual(game.gamestarttime, game.gamestarttime)
        self.assertEqual(game.gamemaster, 'test2')
        self.assertEqual(game.gameassistant, 'test2')
    
    def test_update_nonexisting_game(self):
        game = Game.query.filter_by(id=0).first()
        self.assertEqual(game, None)
    
    def test_update_game_with_empty_data(self):
        game = Game(
            gamename='test',
            gamedescription='test',
            gamelocation='test',
            gamestarttime=datetime.datetime.utcnow(),
            gamemaster='test',
            gameassistant='test'
        )
        db.session.add(game)
        db.session.commit()
        game = Game.query.filter_by(id=game.id).first()
        game.gamename = ''
        game.gamedescription = ''
        game.gamelocation = ''
        game.gamestarttime = game.gamestarttime
        game.gamemaster = ''
        game.gameassistant = ''
        db.session.commit()
        game = Game.query.filter_by(id=game.id).first()
        self.assertEqual(game.gamename, '')
        self.assertEqual(game.gamedescription, '')
        self.assertEqual(game.gamelocation, '')
        self.assertEqual(game.gamestarttime, game.gamestarttime)
        self.assertEqual(game.gamemaster, '')
        self.assertEqual(game.gameassistant, '')
        
if __name__ == '__main__':
    unittest.main()