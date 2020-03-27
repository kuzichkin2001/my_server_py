from flask import Flask, request
import vk_api
import json
from settings import *


vk_session = vk_api.VkApi(token=API_TOKEN)
api = vk_session.get_api()
app = Flask(__name__)


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
        if data['object']['body'] == '1':
            api.messages.send(
                peer_id=data['object']['user_id'],
                random_id=0,
                attachment='photo295713804_457254696'
            )
        else:
            api.messages.send(
                peer_id=data['object']['user_id'],
                random_id=0,
                message='hoola hoola get a doolar')
        return 'ok'



if __name__ == '__main__':
    app.run()