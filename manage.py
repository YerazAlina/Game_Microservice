import os
import unittest
import datetime

from flask_migrate import Migrate

from app import blueprint
from app.main import create_app, db
from app.main.model import game

app = create_app(os.getenv('Swagger Documentation for Game Microservice') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Game=game)

@app.cli.command()
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1