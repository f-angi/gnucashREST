from piecash_util import PiecashUtil

from .ma_models import TransactionSchema


# def read_all():
#     # Create the list of transactions from our data
#     transactions = Transaction.query.order_by(Transaction.guid).all()
#
#     # Serialize the data for the response
#     transactions_schema = TransactionSchema(many=True)
#     return transactions_schema.dump(transactions)

def find_asset(description="", account=""):
    return _serialize_transactions(PiecashUtil().find_transactions_asset(description, account))


def find_expense(description="", account=""):
    return _serialize_transactions(PiecashUtil().find_transactions_expense(description, account))


def find_income(description="", account=""):
    return _serialize_transactions(PiecashUtil().find_transactions_income(description, account))


def _serialize_transactions(transactions):
    transactions_schema = TransactionSchema(many=True)
    return transactions_schema.dump(transactions)
