from flask import Flask
from app.routes import home, dashboard, api
from app.db import init_db
from app.utils import filters

def create_app(test_config=None):               # python uses indent vs. ; and {}
  # set up app config 
  app = Flask(__name__, static_url_path='/')    # declare  new app variable (no need for var, const), app to serve up any static resources from root directory
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'               # creating server-side sessions
  )
  
  @app.route('/hello')                          # @app.route turns hello() function into a route
  def hello():                                  # this is an inner function called hello(), returns a string
    return 'hello world'

  # register routes
  app.register_blueprint(home)
  app.register_blueprint(dashboard)
  app.register_blueprint(api)
  app.jinja_env.filters['format_url'] = filters.format_url
  app.jinja_env.filters['format_date'] = filters.format_date
  app.jinja_env.filters['format_plural'] = filters.format_plural

  init_db(app)

  return app                                    # return becomes the route's response

## creating same route by using Express.js:
# app.get('/hello', (req, res) => { 
# });
