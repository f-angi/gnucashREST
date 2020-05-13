import datetime
from decimal import Decimal

from config import app
from piecash import open_book, Transaction, Account, Split
from piecash.core.account import expense_types, income_types, asset_types
from piecash.core.factories import single_transaction
from sqlalchemy import func


class PiecashUtil(object):
    DB_CONN_STRING = 'mysql://gnucash:gnucash@localhost:3306/gnucash'
    GNUCASH_CURRENCY = 'EUR'

    def __init__(self):
        self.book = open_book(uri_conn=self.DB_CONN_STRING, readonly=False, do_backup=False)

    def new_transaction(self, from_account, to_account, description, value, date=None):

        post_date = datetime.datetime.strptime(date, '%d%m%y').date() if date else datetime.date.today()
        enter_date = datetime.datetime.now().replace(microsecond=0)
        value = Decimal(value).quantize(Decimal('1.00'))

        transaction = single_transaction(
            post_date=post_date,
            enter_date=enter_date,
            description=description,
            value=value,
            from_account=self.book.accounts(name=from_account),
            to_account=self.book.accounts(name=to_account))

        self.book.save()

        app.logger.debug("new transaction guid: %s", transaction.guid)
        return transaction

    def find_transactions_asset(self, description="", account_name=""):
        return self._find_transactions(asset_types, description, account_name)

    def find_transactions_income(self, description="", account_name=""):
        return self._find_transactions(income_types, description, account_name)

    def find_transactions_expense(self, description="", account_name=""):
        return self._find_transactions(expense_types, description, account_name)

    def _find_transactions(self, account_types, description="", account_name=""):

        app.logger.debug("_find_transaction - account_types_set: %s, description: %s, account_name: %s", account_types,
                         description, account_name)

        transactions = self.book.session.query(Transaction.guid,
                                               Transaction.description,
                                               Transaction.enter_date.label("date"),
                                               func.abs(Split.value).label("amount"),
                                               Account.name.label("account_name"),
                                               Account.type.label("account_type")) \
            .join(Split, Split.transaction_guid == Transaction.guid) \
            .join(Account, Account.guid == Split.account_guid) \
            .filter(Account.type.in_(account_types))

        if account_name:
            transactions = transactions.filter(Account.name == account_name)

        if description:
            transactions = transactions.filter(Transaction.description.like('%{}%'.format(description)))

        transactions = transactions.order_by(Transaction.enter_date).all()

        app.logger.debug('Transactions: %s', [t._asdict() for t in transactions])

        return transactions
