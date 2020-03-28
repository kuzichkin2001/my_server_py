## Rauf's and Pasha's bot

from flask import Flask, request
import vk_api
import json
import random
from settings import *


vk_session = vk_api.VkApi(token=API_TOKEN)
api = vk_session.get_api()
app = Flask(__name__)


def message_handler(n_type, uid):
    rand_id = random.randint(0, 10000000)
    if n_type in answers.keys():
        for i, answer in enumerate(answers[n_type], start=1):
            api.messages.send(
                peer_id=uid,
                random_id=rand_id + i,
                attachment=answer
            )
    elif n_type == 'secret-message':
        api.messages.send(
            peer_id=uid,
            random_id=rand_id,
            attachment='photo534733700_457242449'
        )
    else:
        api.messages.send(
            peer_id=uid,
            random_id=rand_id,
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