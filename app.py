from flask import Flask
from flask_login import LoginManager

from config import Config
from models.models import db, User, Equipment
from routes.routes import routes_bp


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    if config:
        app.config.update(config)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'routes.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(routes_bp)
    return app


app = create_app()

with app.app_context():
    db.create_all()

    if not User.query.filter_by(login='admin').first():
        admin = User(login='admin', senha='123')
        db.session.add(admin)
        db.session.commit()

    if Equipment.query.count() == 0:
        equipamentos = [
            Equipment(nome='Notebook Dell', status='Disponível'),
            Equipment(nome='Mouse Gamer', status='Disponível'),
            Equipment(nome='Projetor Epson', status='Disponível'),
        ]
        db.session.add_all(equipamentos)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
