from datetime import datetime
from app.main import db

from app.main.model.game import Game
from typing import Dict, List, Tuple

#save_new_game, get_all_games, get_a_game, delete_a_game, update_a_game 
def save_new_game(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    new_game = Game(
            gamename=data['gamename'],
            gamedescription=data['gamedescription'],
            gamelocation=data['gamelocation'],
            gamestarttime= datetime.now(),
            gamemaster=data['gamemaster'],
            gameassistant=data['gameassistant']
        )
    save_changes(new_game)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered.',
    }
    return response_object, 201
    
def get_all_games() -> List[Dict[str, str]]:
    return Game.query.all()

def get_a_game(id: int) -> Dict[str, str]:
    return Game.query.filter_by(id=id).first()

def delete_a_game(id: int) -> Tuple[Dict[str, str], int]:
    game = Game.query.filter_by(id=id).first()
    if not game:
        response_object = {
            'status': 'fail',
            'message': 'Game with id ' + str(id) + ' does not exists.',
        }
        return response_object, 409
    else:
        db.session.delete(game)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Game successfully deleted.',
        }
        return response_object, 204
    
def update_a_game(id: int, data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    game = Game.query.filter_by(id=id).first()
    if not game:
        response_object = {
            'status': 'fail',
            'message': 'Game with id ' + str(id) + ' does not exists.',
        }
        return response_object, 409
    else:
        game.gamename = data['gamename']
        game.gamedescription = data['gamedescription']
        game.gamelocation = data['gamelocation']
        game.gamestarttime = game.gamestarttime
        game.gamemaster = data['gamemaster']
        game.gameassistant = data['gameassistant']
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Game successfully updated.',
        }
        return response_object,

def save_changes(data: Game) -> None:
    db.session.add(data)
    db.session.commit()