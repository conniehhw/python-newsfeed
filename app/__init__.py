from flask import Flask
from app.routes import home, dashboard

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

  return app                                    # return becomes the route's response

## creating same route by using Express.js:
# app.get('/hello', (req, res) => { 
# });
