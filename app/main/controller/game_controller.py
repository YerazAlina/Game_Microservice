from flask import request
from flask_restx import Resource

from ..util.dto import GameDto 
from ..service.game_service import save_new_game, get_all_games, get_a_game
from typing import Dict, Tuple

api = GameDto.api
_game = GameDto.game
 
@api.route('/')
class GameList(Resource):
    @api.doc('list_of_registered_games')
    @api.marshal_list_with(_game, envelope='data')
    def get(self):
        """List all registered games"""
        return get_all_games()

    @api.expect(_game, validate=True)
    @api.response(201, 'A game successfully created.')
    @api.doc('create a new game')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new game"""
        data = request.json
        return save_new_game(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Game identifier')
@api.response(404, 'Game not found.')
class Game(Resource):
    @api.doc('get a game')
    @api.marshal_with(_game)
    def get(self, public_id):
        """get a game given its identifier"""
        game = get_a_game(public_id)
        if not game:
            api.abort(404)
        else:
            return game

#TODO:get all games by start day 
#TODO:get all games by status
#TODO:trow dice 
#TODO:pick card? > we moved this to the answer microservice