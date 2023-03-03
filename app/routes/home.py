# a single standalone file; a module - that belongws to the routes pkg. With __init__.py present, makes this routes directory a pkg.

from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/') #importing functions Blueprint() & render_template() from flask module

@bp.route('/')  #@bp.route() turned into a route by adding decorator "@", what the function returns becomes the response
def index():
  return render_template('homepage.html')

@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
  return render_template('single-post.html')