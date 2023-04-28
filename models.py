from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import uuid

ma = Marshmallow()
db = SQLAlchemy()

class Advice_Collection(db.Model):
    id = db.Column(db.String, primary_key = True)
    advice_ID = db.Column(db.String(150), nullable=False)
    advice = db.Column(db.String(500), nullable=False)

    def __init__(self,advice,advice_ID, id=''):
        self.id = self.set_id()
        self.advice_ID=advice_ID
        self.advice = advice

    def set_id(self):
        return str(uuid.uuid4())

class AdviceSchema(ma.Schema):
    class Meta:
        fields = ['id', 'advice_ID', 'advice']

advice_schema = AdviceSchema()
advices_schema = AdviceSchema(many=True)