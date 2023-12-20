# Game Microservice

Personal guide for running the Game_Microservice locally for the first time:

Execute the following commands in the from the folder in the terminal:
1. python3.9 -m pip install flask
2. python3.9 -m virtualenv venv
3. source ./venv/bin/activate
4. python3.9 -m pip install -r requirements.txt
5. export FLASK_APP=manage.py
6. flask db init
7. flask db migrate
8. flask db upgrade
9. flask Run

