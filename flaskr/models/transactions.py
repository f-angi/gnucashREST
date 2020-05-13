from config import app
from flask import request
from piecash_util import PiecashUtil

from .ma_models import TransactionSchema


@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())


# def read_all():
#     # Create the list of transactions from our data
#     transactions = Transaction.query.order_by(Transaction.guid).all()
#
#     # Serialize the data for the response
#     transactions_schema = TransactionSchema(many=True)
#     return transactions_schema.dump(transactions)

def new(body):
    date = body['date'] if 'date' in body else None
    transaction = PiecashUtil().new_transaction(body['from_account'], body['to_account'], body['description'],
                                                body['amount'], date)
    return transaction.guid, 201, {'Content-Type': 'text/plain'}


def find_asset(description="", account=""):
    return _serialize_transactions(PiecashUtil().find_transactions_asset(description, account))


def find_expense(description="", account=""):
    return _serialize_transactions(PiecashUtil().find_transactions_expense(description, account))


def find_income(description="", account=""):
    return _serialize_transactions(PiecashUtil().find_transactions_income(description, account))


def _serialize_transactions(transactions):
    transactions_schema = TransactionSchema(many=True)
    return transactions_schema.dump(transactions)
