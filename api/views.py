from flask import Blueprint, jsonify, request
from . import db # .からdbをインポート
from .models import Movie #.modelsからMovieをインポート、.がプロジェクトに関連

main = Blueprint('main', __name__)

@main.route('/add_movie', methods=['POST'])
def add_movie():
    movie_data = request.get_json() # JSONデータを取得する。

    new_movie = Movie(title=movie_data['title'], rating=movie_data['rating']) # new_movie呼び出し

    db.session.add(new_movie) # db追加、new_movieを追加
    db.session.commit() # db.sessionをコミット

    return 'Done', 201

@main.route('/movies')
def movies():
    # movie_list = Movie.query.all()
    movies = []

    # for movie in movie_list:
        # movies.append({'title' : movie.title, 'rating' : movie.rating})

    return jsonify({'movies' : movies})