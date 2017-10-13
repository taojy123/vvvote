# coding: utf-8

import os
import hashlib
import json
import requests
from flask import Flask, request
import random
import time

BOT_URL = os.environ['BOT_URL']
WEBHOOK_SECRET_KEY = os.environ['WEBHOOK_SECRET_KEY']


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'


@app.route('/vote/', methods=['GET'])
def vote():

    n = request.args.get('n', 10)

    PARAMS = {'id': 279, 'act_id': 1}
    vote_url = "http://api2.cyzone.cn/v1/vote/submit"

    for i in range(int(n))
        r = requests.post(vote_url, params=PARAMS)
        print r.text

        t = random.random() + 1
        print t
        time.sleep(t)

    return 'finish'


if __name__ == '__main__':
    app.run(debug=True)
