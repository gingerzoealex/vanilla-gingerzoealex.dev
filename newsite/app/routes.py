from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    title = {'string': 'Title hello'}
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
