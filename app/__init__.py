from flask_restx import Api
from flask import Blueprint, request
from prometheus_flask_exporter import PrometheusMetrics


from .main.controller.game_controller import api as game_ns


blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Swagger Documentation',
    version='1.0',
    description='Swagger Documentation for Game Microservice',
)


api.add_namespace(game_ns, path='/game')

metrics = PrometheusMetrics(blueprint, endpoint='/metrics')