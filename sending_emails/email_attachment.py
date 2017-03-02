# -*- coding: utf-8 -*-
# basic script to send an email
# add attachment
from flask import Flask 
from flask import render_template as html 


import requests
import html_email

# loading the info
from keys import *

subject = 'Hello there-with attachments'

at_file = "Alice.txt"
body_t = "Sending text and attachment!"

# formattting and sending message
request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key),
    files=[("attachment", open(at_file, 
    data={
    'from': sender,
    'to': recipient,
    'subject': subject,
    'text': body_t
    'html': <head> Python is awesome </head> 
    })


# checking the status
print ('Status: {0}'.format(request.status_code))
print ('Body:   {0}'.format(request.text))
