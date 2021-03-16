from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # SQLAlchemyをインスタンス化し、何も引数に渡さない

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app) # DBオブジェクトを作成し、init_app()を使用し、appオブジェクトを渡す。

    from .views import main
    app.register_blueprint(main)

    return app