from flask_restx import Namespace, fields

class GameDto:
    api = Namespace('game', description='game related operations')
    game = api.model('game', {
        'id': fields.Integer(required=False, description='game id', attribute='id', readonly=True),
        'gamename': fields.String(required=True, description='game name'),
        'gamedescription': fields.String(required=True, description='game description'),
        'gamelocation': fields.String(required=True, description='game location'),
        'gamestarttime': fields.DateTime(required=False, description='game start time', readonly=True),
        'gamemaster': fields.String(required=True, description='game master'),
        'gameassistant': fields.String(required=True, description='game assistant')
    })


