# coding: UTF-8
# !/usr/bin/python

import requests, json
import os

def notify(content):
    main_content = {'content': content}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(os.environ["WEBHOOK_URL"], json.dumps(main_content), headers=headers)