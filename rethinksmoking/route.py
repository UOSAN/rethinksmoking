import sys

from flask import (
    Blueprint, request, current_app, make_response
)
from flask.json import dumps

from .custom_encoder import CustomEncoder
from .orm.message import Message
from .orm.mturk_worker import MturkWorker
from .orm.rating import Rating
from .orm.score import Score
from .request_handler import RequestHandler

bp = Blueprint('worker', __name__)

headers = {'Content-Type': 'application/json'}


# Handle POST to the /worker endpoint that contains the required output
@bp.route('/worker', methods=['GET', 'POST'])
def add_worker_and_messages():
    if request.method == 'GET':
        print(f'RS GET /worker')
        sys.stdout.flush()
        workers = MturkWorker.query.all()
        return make_response((dumps(workers, cls=CustomEncoder), 200, headers))
    elif request.method == 'POST':
        print(f'RS POST /worker')
        sys.stdout.flush()
        if request.is_json:
            request_output = request.get_json()
            print(f'POST request as JSON:\n{request_output}\n')
            sys.stdout.flush()

            try:
                handler = RequestHandler(request=request_output)
                handler.handle_request()
            except (KeyError, TypeError, ValueError) as err:
                print(err)
                return make_response('', 400)
        else:
            current_app.logger.info(f'POST request:\n{request.data}\n')
            return make_response('', 400)

        # return successfully
        return make_response(('', 200, headers))


@bp.route('/message', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return make_response((dumps(messages, cls=CustomEncoder), 200, headers))


@bp.route('/score', methods=['GET'])
def get_scores():
    scores = Score.query.all()
    return make_response((dumps(scores, cls=CustomEncoder), 200, headers))


@bp.route('/score', methods=['POST'])
def post_scores():
    print(f'RS POST /score')
    sys.stdout.flush()
    if request.is_json:
        request_output = request.get_json()
        print(f'POST request as JSON:\n{request_output}\n')
        sys.stdout.flush()

        try:
            handler = RequestHandler(request=request_output)
            handler.post_score()
        except (KeyError, TypeError, ValueError) as err:
            print(err)
            return make_response('', 400)
    else:
        current_app.logger.info(f'POST request:\n{request.data}\n')
        return make_response('', 400)

    # return successfully
    return make_response(('', 200, headers))


@bp.route('/rating', methods=['GET'])
def get_ratings():
    ratings = Rating.query.all()
    return make_response((dumps(ratings, cls=CustomEncoder), 200, headers))
