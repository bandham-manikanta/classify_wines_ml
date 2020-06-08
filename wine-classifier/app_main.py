from flask import Flask

def create_app(config_file):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    with app.app_context():
        import routes  # Register routes/controllers here.
        import error_handlers  # Register error handlers here.
    return app
