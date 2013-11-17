#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import render_template
from jsonschema import validate
import json

app = Flask(__name__)

schema = {
    "title": "SendHub Challenge Schema",
    "type": "object",
    "properties": {
        "message": {
            "type": "string"
            },
        "recipients": {
            "type": "array",
            "minItems": 1,
            "items": {"type": "string"},
            "uniqueItems": True
            }
        },
    "required": ["message", "recipients"]
}


@app.route('/', methods=['POST'])
def create_routes():
    ip_list = []

    input_f = request.files['input']
    
    input_dict = json.loads(input_f.read())
    phone_list = input_dict['recipients']

    print len(phone_list[0])
    exit()

    error_checking(phone_list)
    
    no_of_recipients = len(input_dict['recipients'])

    host_small = 1
    host_medium = 1
    host_large = 1
    host_super = 1
    
    ip_list = count_senders(no_of_recipients)
    no_of_categories = len(ip_list)

    small_prefix = "10.0.1."
    medium_prefix = "10.0.2."
    large_prefix = "10.0.3."
    super_prefix = "10.0.4."

    output_dict = {}
 
    routes_list = []
    ip_recipient = {}
    counter = 0

    for i in xrange(no_of_categories):
        while ip_list[i] > 0:
            if i == 3:
                ip_recipient['ip'] = small_prefix + str(host_small)
                host_small += 1

                ip_recipient['recipients'] = phone_list[counter]
                counter += 1
            if i == 2:
                ip_recipient['ip'] = medium_prefix + str(host_medium)
                host_medium += 1

                ip_recipient['recipients'] = phone_list[counter:counter+5]
                counter += 5
            if i == 1:
                ip_recipient['ip'] = large_prefix + str(host_large)
                host_large += 1

                ip_recipient['recipients'] = phone_list[counter:counter+10]
                counter += 10
            if i == 0:
                ip_recipient['ip'] = super_prefix + str(host_super)
                host_super += 1

                ip_recipient['recipients'] = phone_list[counter:counter+25]
                counter += 25
            
            ip_list[i] -= 1
            routes_list.append(ip_recipient)
            ip_recipient = {}

    output_dict['routes'] = routes_list     
    output_dict['message'] = input_dict['message']      
    output_json = json.dumps(output_dict)

    return output_json

def error_checking(phone_numbers):
    unique = test_unique(phone_numbers)
    ten_digits = test_ten_digits(phone_numbers)

    if unique == False:
        print "Please provide unique phone numbers!"
        exit()
    elif ten_digits == False:
        print "Please provide 10-digit phone numbers i.e. 1234567890"
        exit()
    
def test_ten_digits(no_list):
    for i in no_list:
        if len(i) != 10:
            return False
    return True

def test_unique(no_list):
    s = set()
    for x in no_list:
        if x in s: 
            return False
        s.add(x)
    return True

def count_senders(number):
    req = [25, 10, 5, 1]
    
    ip_used = []

    for i in req:
        div = number/i
        ip_used.append(div)
        number = number - (div*i)
    
    return ip_used

if __name__ == '__main__':
    app.debug = True
    app.run()
