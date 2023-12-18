from datetime import datetime
from app.main import db

from app.main.model.game import Game
from typing import Dict, List, Tuple

def save_new_game(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    game = Game.query.filter_by(gamename=data['gamename']).first()
    if not game:
        new_game = Game(
            gamename=data['gamename'],
            starttime=datetime.utcnow(),
            isactive=True
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

def get_all_games() -> List[Game]:
    return Game.query.all()

def get_a_game(id: int) -> Game:
    return Game.query.filter_by(id=id).first()

def delete_a_game(id: int) -> None:
    game = Game.query.filter_by(id=id).first()
    db.session.delete(game)
    db.session.commit()

def update_a_game(id: int, data: Dict[str, str]) -> None:
    game = Game.query.filter_by(id=id).first()
    if game.gamename != data['gamename']:
        game.gamename = data['gamename']
    if game.isactive != data['isactive']:
        game.isactive = data['isactive']
    db.session.commit()

def save_changes(data: Game) -> None:
    db.session.add(data)
    db.session.commit()

