from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:96234737@localhost/surveydb'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(200), unique=True)
    artist = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, fullname, artist, rating, comments):
        self.fullname = fullname
        self.artist = artist
        self.rating = rating
        self.comments = comments


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        fullname = request.form.get('fullname', '')
        artist = request.form.get('artist', '')
        rating = request.form.get('rating', '')
        comments = request.form.get('comments', '')
        # print(fullname, artist, rating, comments)
        if fullname == '' or artist == '':
            return render_template('index.html', message='Please input all the fields')
        if db.session.query(Feedback).filter(Feedback.fullname == fullname).count() == 0:
            data = Feedback(fullname, artist, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(fullname, artist, rating, comments)
            return render_template('success.html')
        return render_template('index.html', message='You have already given a feedback!')



if __name__ == '__main__':
    app.run()
