from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    title = {'string': 'And for my next trick I will make this CSV into a gra-<”ParserError: Expected 1 fields in line 34, saw 2”>'}
    slides = [
    {
        'title': {'title': 'Slide 1'},
        'body': 'The first slide of the presentation'
    },
    {
        'title': {'title': 'Slide 2'},
        'body': 'The second slide of the presentation'
    }
    ]
    return render_template('index.html', title=title, slides=slides)
