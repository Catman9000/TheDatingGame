from application import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(75))
    password = db.Column(db.String(20))
    partner = db.Column(db.Boolean)
    dater = db.Column(db.Boolean)


personofinterest = db.relationship( 'Interest', foreign_keys='Interest.personofinterest_id', backref='Interester', lazy=True)



class Questions(db.Model):
    questions_id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
    personofinterest_id = db.Column(db.Integer, db.ForeignKey('user.id'))
