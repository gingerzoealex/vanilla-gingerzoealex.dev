from app import app
from flask import render_template
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    title = {'string': 'gingerzoealex: Home'}
    # slides = [
    # {
        # 'title': {'title': 'Slide 1'},
        # 'body': 'The first slide of the presentation'
    # },
    # {
        # 'title': {'title': 'Slide 2'},
        # 'body': 'The second slide of the presentation'
    # }
    # ]
    info = {'string': 'The website content \n Line break????'}
    return render_template('index.html', title=title, info=info)


@app.route('/blogs')
@app.route('/blog')
def blogs():
    title = {'string': "For Blog's Sake"}
    slides = [
    {
        'title': {'title': 'Blog post 1'},
        'body': 'Blah blah blaj oweufnhoewfn owefowinefw \n weiufewofinewfpnwefw \n oewqifnewfw'
    },
    {
        'title': {'title': 'Blog post 2'},
        'body': 'Blah blah blaj oweufnhoewfn owefowinefw \n weiufewofinewfpnwefw \n oewqifnewfw'
    }
    ]
    # content = {'string': 'The website content \n Line break????'}
    return render_template('blog.html', title=title, slides=slides)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
