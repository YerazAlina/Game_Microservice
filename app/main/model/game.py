from .. import db
import datetime

class Game(db.Model):
    __tablename__ = 'game'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gamename = db.Column(db.String(50), nullable=False)
    starttime = db.Column(db.DateTime, nullable=True)
    gamestatus = db.Column(db.String(50), nullable=True)
    #gameName and gameId are in the answer microservice 

    def __repr__(self):
        return '<id: {}, gamename: {}, starttime: {}, gamestatus: {}>'.format(self.id, self.starttime, self.gamestatus)

