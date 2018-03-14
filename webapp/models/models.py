from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(64), unique=True)
    feature_vector = db.Column(db.String(255))

    def __str__(self):
        return self.query


class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(128))
    feedback_id = db.Column(db.Integer, db.ForeignKey('feedbacks.id'))
    feedback = db.relationship('Feedback', backref='feedback')

    def __str__(self):
        return self.image_url

class NeuralNetworkModel(db.Model):
    __tablename__ = 'neuralmodels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __str__(self):
        return self.name

class NeuralLayer(db.Model):
    __tablename__ = 'neurallayer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    extracted = db.Column(db.Boolean, default=False)
    neural_network_id = db.Column(db.Integer, db.ForeignKey('neuralmodels.id'))
    neural_network = db.relationship('NeuralNetworkModel', backref='neural_network')

    def __str__(self):
        return self.name

