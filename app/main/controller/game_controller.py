from flask import request
from flask_restx import Resource

from ..util.dto import GameDto 
from ..service.game_service import save_new_game, get_all_games, get_a_game, delete_a_game, update_a_game 
from typing import Dict, Tuple

api = GameDto.api
_game = GameDto.game

@api.route('/')
class GameList(Resource):
    @api.doc('list_of_games')
    @api.marshal_list_with(_game, envelope='data')
    def get(self):
        """List all games"""
        return get_all_games()

    @api.response(201, 'Game successfully created.')
    @api.doc('create a new game')
    @api.expect(_game, validate=True)
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Game"""
        data = request.json
        return save_new_game(data=data)

@api.route('/<id>')
@api.param('id', 'The Game identifier')
@api.response(404, 'Game not found.')
class Game(Resource):
    @api.doc('get a game')
    @api.marshal_with(_game)
    def get(self, id):
        """Get a game given its identifier"""
        game = get_a_game(id)
        if not game:
            api.abort(404)
        else:
            return game

    @api.doc('delete a game')
    @api.response(204, 'Game successfully deleted.')
    def delete(self, id):
        """Delete a game given its identifier"""
        return delete_a_game(id)

    @api.doc('update a game')
    @api.expect(_game, validate=True)
    @api.response(204, 'Game successfully updated.')
    def put(self, id):
        """Update a game activity status given its identifier"""
        data = request.json
        update_a_game(id=id, data=data)
        if not data:
            api.abort(400)
        else:
            return '', 204