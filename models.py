from .extensions import db

class Url(db.Model):
    __tablename__ = 'URL_db'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    shortCode = db.Column(db.String(12), unique=True, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated = db.Column(db.DateTime, nullable=True, default=db.func.now(), onupdate=db.func.now())
    accessCount = db.Column(db.Integer, defualt=0)

    def __repr__(self):
        return f'<Short url {self.shortCode} with id {self.id}>'

