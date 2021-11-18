from exts import db


class Record(db.Model):
    __tablename__  = 'record'
    Username = db.Column(db.String(255, 'utf8_general_ci'), primary_key=True)
    reposurl = db.Column(db.String(255, 'utf8_general_ci'), nullable=True)

