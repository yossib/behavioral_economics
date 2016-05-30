
import json

from flask import Flask
import csv

app = Flask(__name__)
app.debug = True


from positions.Popsition import Position

app = Flask(__name__)


@app.route('/')

def hello_world():
    teams = dict()
    positions = []
    with open('/Users/yossi/PycharmProjects/untitled/data/all_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            position =Position(**row)
            if not teams.get(position.team):
                teams[position.team] = []
            teams[position.team].append(position)

    return "Hello world"


if __name__ == '__main__':
    app.run()
