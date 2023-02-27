#!/usr/bin/python3
from flask import Flask
import datetime 
app = Flask(__name__)

@app.route('/')
def listen():
    # Takes the day from the time zone running on the machine
    day = datetime.datetime.now().strftime("%A")
    # Takes the date from the time zone running on the machine
    date = datetime.datetime.now().strftime("%d.%m.%Y")
    # Prepare
    update = "Today is "+day+"\nThe current date is "+date
    # Insert
    with open("fileListen.txt", "w") as f:
        f.write(update)
    return update


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)