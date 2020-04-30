from flask import (
    Blueprint, request, current_app, make_response
)

from .request_handler import RequestHandler
from .orm.rating import Rating
from .orm.score import Score

bp = Blueprint('worker', __name__)


# Handle POST to the /worker/message endpoint that contains the required output
@bp.route('/worker/message', methods=['POST'])
def add_worker_and_messages():
    if request.is_json:
        request_output = request.get_json()
        current_app.logger.info(f'New POST received')

        try:
            current_app.logger.info(f'POST request as JSON:\n{request_output}\n')
            handler = RequestHandler(request=request_output)
            handler.handle_request()
        except KeyError as ke:
            current_app.logger.exception(str(ke))
    else:
        current_app.logger.info(f'POST request:\n{request.data}\n')
        return make_response('', 400)

    # return successfully
    return make_response('', 200)


@bp.route('/score', methods=['GET'])
def get_scores():
    scores = Score.query.all()
    return make_response(str(scores), 200)


@bp.route('/rating', methods=['GET'])
def get_ratings():
    ratings = Rating.query.all()
    return make_response(str(ratings), 200)
