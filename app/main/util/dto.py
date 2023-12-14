from flask_restx import Namespace, fields


class GameDto:
    api = Namespace('game', description='game related operations')
    game = api.model('game', {
        #TODO: add some fields here like gamename
        'gamename': fields.String(required=True, description='gamename'),
    })

