from flask import Flask, url_for


def create_app():
    app = Flask(__name__)

    # Function to easily find your assets
    # In your template use <link rel=stylesheet href="{{ static('filename')
    # }}">
    app.jinja_env.globals['static'] = (
        lambda filename: url_for('static', filename=filename)
    )

    # Config defines which packages are loaded.
    app.config['PACKAGES'] = [
        'app'
    ]

    if 'app' in app.config['PACKAGES']:
        from app.views import blueprint as bp
        app.register_blueprint(bp)

    return app
