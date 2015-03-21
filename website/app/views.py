from flask import Blueprint, render_template

blueprint = Blueprint('base', __name__, template_folder='templates')


@blueprint.route('/')
def index():
    return render_template('index.html')

@blueprint.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')