from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    time = db.Column(db.String(80))
    plate = db.Column(db.String(80))


    #store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    #store = db.relationship('StoreModel')

    def __init__(self, name, time, plate):
        self.name = name
        self.time = time
        self.plate = plate

    def json(self):
        return {'name': self.name, 'time':self.time, 'plate':self.plate}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
