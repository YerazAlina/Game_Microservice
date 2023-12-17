from flask_restx import Namespace, fields


class GameDto:
    api = Namespace('game', description='game related operations')
    game = api.model('game', {
        'id': fields.Integer(required=True, description='game id'),
        'gamename': fields.String(required=True, description='game name'),
        'starttime': fields.DateTime(required=True, description='start time'),
        'gamestatus': fields.String(required=True, description='game status')
    })

