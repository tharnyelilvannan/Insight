from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# initialize the database and login manager
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///insight.db'

    # initialize the app with db and login_manager
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'routes.login'  # Specify the login route

    # import User model before defining the user_loader
    from app.models import User

    # define user_loader after importing User model
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # register blueprint for routes
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    print("Blueprints registered:", app.blueprints)

    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint}: {rule}")


    print("Registered URL rules:")
    print(app.url_map)

    return app
