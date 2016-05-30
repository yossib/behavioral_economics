
import json

from flask import Flask
import csv

app = Flask(__name__)
app.debug = True


from positions.Popsition import Position

app = Flask(__name__)


@app.route('/')

def hello_world():
    positions = []
    with open('/Users/yossi/PycharmProjects/untitled/sheet1.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            positions.append(Position(**row))

    return "Hello world"


if __name__ == '__main__':
    app.run()
