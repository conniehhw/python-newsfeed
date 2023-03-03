from flask import Blueprint, render_template

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')
# This time, using the url_prefix argument, we prefix every route in the blueprint with /dashboard. 
# The routes thus become /dashboard and /dashboard/edit/<id> when registered with the app.

@bp.route('/')
def dash():
  return render_template('dashboard.html')

@bp.route('/edit/<id>')
def edit(id):
  return render_template('edit-post.html')

  # no need to explicity declare the properties you want to expose with module.exports = { bp }; with Node.js
  # as we have the ability in python to import every var or function in a module