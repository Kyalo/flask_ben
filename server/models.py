from . import db

class User(db.Model):
    __tablename__ = 'users' 

    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    age = db.Column(db.Integer)
    location = db.Column(db.String(255))
    whatsapp_number = db.Column(db.String(255), unique=True)
    num_texts = db.Column(db.Integer, default=0)


class ChatData(db.Model):
    __tablename__ = 'chat_data'

    id = db.Column(db.Integer, primary_key=True)
    whatsapp_number = db.Column(db.String(255))
    message_sent = db.Column(db.Text)
    response_sent = db.Column(db.Text)
    time_sent = db.Column(db.DateTime)
    day_sent = db.Column(db.Date)
    initial_context = db.Column(db.Text)
    updated_context = db.Column(db.Text)
    user_conditions_id = db.Column(db.Integer, db.ForeignKey('user_conditions.id'))


class UserConditions(db.Model):
    __tablename__ = 'user_conditions'

    id = db.Column(db.Integer, primary_key=True)
    whatsapp_number = db.Column(db.String(255))
    disease = db.Column(db.String(255))
    description = db.Column(db.Text)
    prevention = db.Column(db.Text)
    cure = db.Column(db.Text)
    probability = db.Column(db.Float)

