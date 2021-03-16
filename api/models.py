from . import db 

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True) #整数値、主キー指定
    title = db.Column(db.String(50)) #50文字の長さの文字列
    rating = db.Column(db.Integer) # 整数値