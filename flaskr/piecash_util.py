from datetime import datetime

from piecash import open_book, Transaction
from piecash.core.factories import single_transaction


class PiecashUtil(object):
    DB_CONN_STRING = 'mysql://gnucash:gnucash@localhost:3306/gnucash'
    GNUCASH_CURRENCY = 'EUR'
    GNUCASH_ACCOUNT_TYPE_ASSETS = 'ASSET'
    GNUCASH_ACCOUNT_TYPE_EXPENSES = 'EXPENSE'

    def __init__(self):
        self.book = open_book(uri_conn=self.DB_CONN_STRING, readonly=False, do_backup=False)

    def expense_transaction(self, asset_account_full_name, expense_account_full_name, description, value):
        today = datetime.now()

        single_transaction(
            post_date=today,
            enter_date=today,
            description=description,
            value=value,
            from_account=self.book.accounts(fullname=asset_account_full_name),
            to_account=self.book.accounts(fullname=expense_account_full_name))

        self.book.save()

    def find_transactions(self, description):
        if description:
            transactions = self.book.session.query(Transaction).filter(
                Transaction.description.like('%{}%'.format(description)))
        else:
            transactions = self.book.session.query(Transaction)

        return transactions.order_by(Transaction.post_date).all()
