from config import db, ma
from db-models import Transaction

class TransactionSchema(ma.ModelSchema):
    class Meta:
        model = Transaction
        sqla_session = db.session
