from flask import Flask, render_template
from jinja2 import Template
import json

app = Flask(__name__)


@app.route('/')
def home():
    # return render_template('rightTemplate.html')
    with open('templates/rightTemplate.json') as file:
        json_data = json.load(file)

    with open('templates/rightTemplate.html') as file:
        template = Template(file.read())
    
    return template.render(data=json_data)

# TIME LINE TEMAPLTE CODE RENDER
    # with open('templates/time_line.json') as file:
    #     json_data = json.load(file)

    # with open('templates/timelineTemplate.html') as file:
    #     template = Template(file.read())
    
    # return template.render(data=json_data)


@app.route('/storyTemplate.html')
def story():
    with open('templates/story.json') as file:
        json_data = json.load(file)

    with open('templates/storyTemplate.html') as file:
        template = Template(file.read())
    
    return template.render(data=json_data)


if __name__ == "__main__":
    app.run(debug=True)