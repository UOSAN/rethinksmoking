from flask import (
    Blueprint, request, current_app, make_response
)

bp = Blueprint('worker', __name__)


# Handle POST to the /worker/message endpoint that contains the required output
@bp.route('/worker/message', methods=['POST'])
def add_worker_and_messages():
    if request.is_json:
        request_output = request.get_json()
        current_app.logger.info(f'New POST received')

        try:
            current_app.logger.info(f'POST request as JSON:\n{request_output}\n')
        except KeyError as ke:
            current_app.logger.exception(str(ke))
    else:
        current_app.logger.info(f'POST request:\n{request.data}\n')
        return make_response('', 400)

    # return successfully
    return make_response('', 200)
