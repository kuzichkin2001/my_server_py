from flask import Flask, request
import vk_api
import json
from settings import *


vk_session = vk_api.VkApi(token=API_TOKEN)
api = vk_session.get_api()
app = Flask(__name__)


def message_handler(n_type, uid):
    if n_type in ans.keys():
        api.messages.send(
            peer_id=uid,
            random_id=0,
            attachment='photo185419301_457239034'
        )
    else:
        api.messages.send(
            peer_id=uid,
            random_id=0,
            message='hoola hoola get a doolar'
        )


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/', methods=["POST"])
def handling_post():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk request'
    if data['type'] == 'confirmation':
        return CONFIRMATION_TOKEN
    elif data['type'] == 'message_new':
        message_handler(data['object']['body'], data['object']['user_id'])
        return 'ok'


if __name__ == '__main__':
    app.run()