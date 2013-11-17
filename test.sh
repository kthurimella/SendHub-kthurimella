#!/bin/bash
clear
python generate_phone_numbers.py $1 $2
curl -i -F input=@input.txt http://sendhub-kthurimella.herokuapp.com
