from flask_restx import Namespace, fields


class GameDto:
    api = Namespace('game', description='game related operations')
    game = api.model('game', {
        'starttime': fields.String(required=True, description='start time game'),
        'gamestatus': fields.String(required=True, description='status'),
    })

