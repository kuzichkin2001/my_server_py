from flask import Flask, request
import vk_api
import json
from settings import *


vk_session = vk_api.VkApi(token=API_TOKEN)
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


if __name__ == '__main__':
    app.run()