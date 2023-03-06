#!/usr/bin/python3
from flask import Flask
import datetime 
app = Flask(__name__)

def replace_placeholders(content):
    content = content.replace("[DAY_OF_WEEK]", day_of_week)
    content = content.replace("[CURRENT_DATE]", current_date)
    return content

@app.route('/')
def listen():
    with open("file.txt", "r") as f:
        file_content = f.read()
    # Takes the day from the time zone running on the machine
    day = datetime.datetime.now().strftime("%A")
    # Takes the date from the time zone running on the machine
    date = datetime.datetime.now().strftime("%d.%m.%Y")
    # Prepare
    res=replace_placeholders(file_content)
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)