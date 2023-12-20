from .. import db

class Game(db.Model):
    __tablename__ = 'game'

    #als ik camelcase gebruik neemt ie dat over in de database en krijg ik een error // str.lower() gebruiken? 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gamename = db.Column(db.String(50), nullable=False)
    gamedescription = db.Column(db.String(50), nullable=False)
    gamelocation = db.Column(db.String(50), nullable=False)
    gamestarttime = db.Column(db.DateTime, nullable=False)
    gamemaster = db.Column(db.String(50), nullable=False)
    gameassistant = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<id: {}, gamename: {}, gamedescription: {}, gamelocation: {}, gamestarttime: {}, gamemaster: {}, gameassistant {}'.format(self.id, self.gamename, self.gamedescription, self.gamelocation, self.starttime, self.gamemaster, self.gameassistants)

