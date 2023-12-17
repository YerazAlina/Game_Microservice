from flask_restx import Namespace, fields


class GameDto:
    api = Namespace('game', description='game related operations')
    newgame = api.model('newgame', {
        'gamename': fields.String(required=True, description='game name'),
        'gamestatus': fields.String(required=True, description='game status')
    })
    game = api.model('game', {
        'id': fields.Integer(required=True, description='game id'),
        'gamename': fields.String(required=True, description='game name'),
        'starttime': fields.DateTime(required=True, description='game start time'),
        'gamestatus': fields.String(required=True, description='game status')
    })


