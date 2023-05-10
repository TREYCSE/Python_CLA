from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
print('no issues!')

class BaseModel(db.Model):
    class Meta:
        database = db
usr = User()

class Question(BaseModel):
    question = CharField()
    answer = CharField()

db.create_tables([Question])

artificial = Question(question='What is Artificial Intelligence?', answer='the theory and development of computer systems able to perform tasks that normally require human intelligence, such as visual perception, speech recognition, decision-making, and translation between languages.')
artificial.save()

app = Question(question='Is Machine Learning a form of Artificial Intelligence?', answer='yes')
app.save()

robotics = Question(question="How does robotics work?", answer='To function, a combination of computer programming and algorithms, a remotely controlled manipulator, actuators, control systems -- action, processing and perception -- real-time sensors and an element of automation helps to inform what a robot or robotic system does.')
robotics.save()

