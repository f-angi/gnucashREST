from .db_models import Transaction
from .ma_models import TransactionSchema


def read_all():
    # Create the list of transactions from our data
    transactions = Transaction.query.order_by(Transaction.guid).all()

    # Serialize the data for the response
    transactions_schema = TransactionSchema(many=True)
    return transactions_schema.dump(transactions)
