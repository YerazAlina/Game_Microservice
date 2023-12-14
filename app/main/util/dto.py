from flask_restx import Namespace, fields


class GameDto:
    api = Namespace('game', description='game related operations')
    game = api.model('game', {
        #TODO: add some fields here like gameName
        'game_name': fields.String(required=True, description='game name'),
    })

