from flask import request
from flask_restx import Resource

from ..util.dto import GameDto 
from ..service.game_service import save_new_game, get_all_games, get_a_game
from typing import Dict, Tuple
import random

api = GameDto.api
_game = GameDto.game
_newgame = GameDto.newgame

@api.route('/')
class GameList(Resource):
    @api.doc('list_of_registered_games')
    @api.marshal_list_with(_game, envelope='data')
    def get(self):
        """List all registered games"""
        return get_all_games()

    @api.expect(_newgame)
    @api.response(201, 'A game successfully created.')
    @api.doc('create a new game')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new game"""
        data = request.json
        return save_new_game(data=data)


@api.route('/<id>')
@api.param('id', 'The Game identifier')
@api.response(404, 'Game not found.')
class Game(Resource):
    @api.doc('get a game')
    @api.marshal_with(_game)
    def get(self, id):
        """get a game given its identifier"""
        game = get_a_game(id)
        if not game:
            api.abort(404)
        else:
            return game
    @api.doc('delete a game')
    @api.marshal_with(_game)
    def delete(self, id):
        """delete a game given its identifier"""
        game = get_a_game(id)
        if not game:
            api.abort(404)
        else:
            api.session.delete(game)
            api.session.commit()
            return game
    @api.doc('update a game')
    @api.marshal_with(_game)
    def put(self, id):
        """update a game given its identifier"""
        game = get_a_game(id)
        if not game:
            api.abort(404)
        else:
            data = request.json
            game.gamename = data['gamename']
            game.starttime = data['starttime']
            game.gamestatus = data['gamestatus']
            api.session.commit()
            return game

@api.route('/dice')
@api.doc('get a random number between 1 and 6 from a dice')
@api.response(404, 'Dice not available.')
class DiceController(Resource):
    @api.doc('get a random number between 1 and 6 from a dice')
    def get(self):
        return random.randint(1,6)
    
#TODO:get all games by start day 
#TODO:get all games by status
