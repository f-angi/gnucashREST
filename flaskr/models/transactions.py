from piecash_util import PiecashUtil

from .ma_models import TransactionSchema


# def read_all():
#     # Create the list of transactions from our data
#     transactions = Transaction.query.order_by(Transaction.guid).all()
#
#     # Serialize the data for the response
#     transactions_schema = TransactionSchema(many=True)
#     return transactions_schema.dump(transactions)


def find(description="", account=""):
    transactions = PiecashUtil().find_transactions(description)

    for t in transactions:
        for s in t.splits:
            if s.value >= 0:
                t.amount = s.value
                t.account = s.account.name

    if account:
        transactions = [t for t in transactions if account.lower() in t.account.lower()]

    # Serialize the data for the response
    transactions_schema = TransactionSchema(many=True)
    return transactions_schema.dump(transactions)
