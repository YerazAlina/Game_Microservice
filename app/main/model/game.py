from .. import db
import datetime

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    startTime = db.Column(db.DateTime, nullable=False)
    gameStatus = db.Column(db.String(50), nullable=False)
    #gameName and gameId are in the answer microservice 

    def __init__(self):
        self.startTime = datetime.datetime.now()
        self.gameStatus = "in progress"

    def __repr__(self):
        return '<id: {}, startTime: {}, gameStatus: {}>'.format(self.id, self.startTime, self.gameStatus)
    
    #GameId
    def get_game_id(self):
        return self.id  
    
    def set_game_id(self, id):
        self.id = id
   
    #GameStatus
    def get_game_status(self):
        return self.gameStatus

    def set_game_status(self, status):
        self.gameStatus = status

    #StartTime
    def get_start_time(self):   
        return self.startTime
        
    def set_start_time(self, time):
        self.startTime = time



    
    

