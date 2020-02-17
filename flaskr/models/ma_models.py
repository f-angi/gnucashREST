from flaskr.config import db, ma
from .db_models import Transaction


class TransactionSchema(ma.ModelSchema):
    class Meta:
        model = Transaction
        sqla_session = db.session
