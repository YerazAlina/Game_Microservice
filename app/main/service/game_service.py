from app.main import db

from app.main.model.game import Game
from typing import Dict, Tuple

def get_a_game(public_id):
    return Game.query.filter_by(public_id=public_id).first()

def get_all_games():
    return Game.query.all()

def save_new_game(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    game = Game.query.filter_by(gameName=data['gameName']).first()
    if not game:
        new_game = Game(
            gameName=data['gameName'],
        )
        save_changes(new_game)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Game already exists.',
        }
        return response_object, 409
    
def save_changes(data: Game) -> None:
    db.session.add(data)
    db.session.commit()

#TODO: maybe rethink this one.....
def delete_game(public_id):
    game = Game.query.filter_by(public_id=public_id).first()
    if game:
        db.session.delete(game)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted.',
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Game not found.',
        }
        return response_object, 409