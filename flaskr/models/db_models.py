# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Float, Integer, String, Table, text
from sqlalchemy.ext.declarative import declarative_base
from config import db

Base = declarative_base()
metadata = Base.metadata


class Account(Base):
    __tablename__ = 'accounts'

    guid = Column(String(32), primary_key=True)
    name = Column(String(2048), nullable=False)
    account_type = Column(String(2048), nullable=False)
    commodity_guid = Column(String(32))
    commodity_scu = Column(Integer, nullable=False)
    non_std_scu = Column(Integer, nullable=False)
    parent_guid = Column(String(32))
    code = Column(String(2048))
    description = Column(String(2048))
    hidden = Column(Integer)
    placeholder = Column(Integer)


class Billterm(Base):
    __tablename__ = 'billterms'

    guid = Column(String(32), primary_key=True)
    name = Column(String(2048), nullable=False)
    description = Column(String(2048), nullable=False)
    refcount = Column(Integer, nullable=False)
    invisible = Column(Integer, nullable=False)
    parent = Column(String(32))
    type = Column(String(2048), nullable=False)
    duedays = Column(Integer)
    discountdays = Column(Integer)
    discount_num = Column(BigInteger)
    discount_denom = Column(BigInteger)
    cutoff = Column(Integer)


class Book(Base):
    __tablename__ = 'books'

    guid = Column(String(32), primary_key=True)
    root_account_guid = Column(String(32), nullable=False)
    root_template_guid = Column(String(32), nullable=False)


class BudgetAmount(Base):
    __tablename__ = 'budget_amounts'

    id = Column(Integer, primary_key=True, server_default=text("nextval('budget_amounts_id_seq'::regclass)"))
    budget_guid = Column(String(32), nullable=False)
    account_guid = Column(String(32), nullable=False)
    period_num = Column(Integer, nullable=False)
    amount_num = Column(BigInteger, nullable=False)
    amount_denom = Column(BigInteger, nullable=False)


class Budget(Base):
    __tablename__ = 'budgets'

    guid = Column(String(32), primary_key=True)
    name = Column(String(2048), nullable=False)
    description = Column(String(2048))
    num_periods = Column(Integer, nullable=False)


class Commodity(Base):
    __tablename__ = 'commodities'

    guid = Column(String(32), primary_key=True)
    namespace = Column(String(2048), nullable=False)
    mnemonic = Column(String(2048), nullable=False)
    fullname = Column(String(2048))
    cusip = Column(String(2048))
    fraction = Column(Integer, nullable=False)
    quote_flag = Column(Integer, nullable=False)
    quote_source = Column(String(2048))
    quote_tz = Column(String(2048))


class Customer(Base):
    __tablename__ = 'customers'

    guid = Column(String(32), primary_key=True)
    name = Column(String(2048), nullable=False)
    id = Column(String(2048), nullable=False)
    notes = Column(String(2048), nullable=False)
    active = Column(Integer, nullable=False)
    discount_num = Column(BigInteger, nullable=False)
    discount_denom = Column(BigInteger, nullable=False)
    credit_num = Column(BigInteger, nullable=False)
    credit_denom = Column(BigInteger, nullable=False)
    currency = Column(String(32), nullable=False)
    tax_override = Column(Integer, nullable=False)
    addr_name = Column(String(1024))
    addr_addr1 = Column(String(1024))
    addr_addr2 = Column(String(1024))
    addr_addr3 = Column(String(1024))
    addr_addr4 = Column(String(1024))
    addr_phone = Column(String(128))
    addr_fax = Column(String(128))
    addr_email = Column(String(256))
    shipaddr_name = Column(String(1024))
    shipaddr_addr1 = Column(String(1024))
    shipaddr_addr2 = Column(String(1024))
    shipaddr_addr3 = Column(String(1024))
    shipaddr_addr4 = Column(String(1024))
    shipaddr_phone = Column(String(128))
    shipaddr_fax = Column(String(128))
    shipaddr_email = Column(String(256))
    terms = Column(String(32))
    tax_included = Column(Integer)
    taxtable = Column(String(32))


class Employee(Base):
    __tablename__ = 'employees'

    guid = Column(String(32), primary_key=True)
    username = Column(String(2048), nullable=False)
    id = Column(String(2048), nullable=False)
    language = Column(String(2048), nullable=False)
    acl = Column(String(2048), nullable=False)
    active = Column(Integer, nullable=False)
    currency = Column(String(32), nullable=False)
    ccard_guid = Column(String(32))
    workday_num = Column(BigInteger, nullable=False)
    workday_denom = Column(BigInteger, nullable=False)
    rate_num = Column(BigInteger, nullable=False)
    rate_denom = Column(BigInteger, nullable=False)
    addr_name = Column(String(1024))
    addr_addr1 = Column(String(1024))
    addr_addr2 = Column(String(1024))
    addr_addr3 = Column(String(1024))
    addr_addr4 = Column(String(1024))
    addr_phone = Column(String(128))
    addr_fax = Column(String(128))
    addr_email = Column(String(256))


class Entry(Base):
    __tablename__ = 'entries'

    guid = Column(String(32), primary_key=True)
    date = Column(DateTime, nullable=False)
    date_entered = Column(DateTime)
    description = Column(String(2048))
    action = Column(String(2048))
    notes = Column(String(2048))
    quantity_num = Column(BigInteger)
    quantity_denom = Column(BigInteger)
    i_acct = Column(String(32))
    i_price_num = Column(BigInteger)
    i_price_denom = Column(BigInteger)
    i_discount_num = Column(BigInteger)
    i_discount_denom = Column(BigInteger)
    invoice = Column(String(32))
    i_disc_type = Column(String(2048))
    i_disc_how = Column(String(2048))
    i_taxable = Column(Integer)
    i_taxincluded = Column(Integer)
    i_taxtable = Column(String(32))
    b_acct = Column(String(32))
    b_price_num = Column(BigInteger)
    b_price_denom = Column(BigInteger)
    bill = Column(String(32))
    b_taxable = Column(Integer)
    b_taxincluded = Column(Integer)
    b_taxtable = Column(String(32))
    b_paytype = Column(Integer)
    billable = Column(Integer)
    billto_type = Column(Integer)
    billto_guid = Column(String(32))
    order_guid = Column(String(32))


t_gnclock = Table(
    'gnclock', metadata,
    Column('hostname', String(255)),
    Column('pid', Integer)
)


class Invoice(Base):
    __tablename__ = 'invoices'

    guid = Column(String(32), primary_key=True)
    id = Column(String(2048), nullable=False)
    date_opened = Column(DateTime)
    date_posted = Column(DateTime)
    notes = Column(String(2048), nullable=False)
    active = Column(Integer, nullable=False)
    currency = Column(String(32), nullable=False)
    owner_type = Column(Integer)
    owner_guid = Column(String(32))
    terms = Column(String(32))
    billing_id = Column(String(2048))
    post_txn = Column(String(32))
    post_lot = Column(String(32))
    post_acc = Column(String(32))
    billto_type = Column(Integer)
    billto_guid = Column(String(32))
    charge_amt_num = Column(BigInteger)
    charge_amt_denom = Column(BigInteger)


class Job(Base):
    __tablename__ = 'jobs'

    guid = Column(String(32), primary_key=True)
    id = Column(String(2048), nullable=False)
    name = Column(String(2048), nullable=False)
    reference = Column(String(2048), nullable=False)
    active = Column(Integer, nullable=False)
    owner_type = Column(Integer)
    owner_guid = Column(String(32))


class Lot(Base):
    __tablename__ = 'lots'

    guid = Column(String(32), primary_key=True)
    account_guid = Column(String(32))
    is_closed = Column(Integer, nullable=False)


class Order(Base):
    __tablename__ = 'orders'

    guid = Column(String(32), primary_key=True)
    id = Column(String(2048), nullable=False)
    notes = Column(String(2048), nullable=False)
    reference = Column(String(2048), nullable=False)
    active = Column(Integer, nullable=False)
    date_opened = Column(DateTime, nullable=False)
    date_closed = Column(DateTime, nullable=False)
    owner_type = Column(Integer, nullable=False)
    owner_guid = Column(String(32), nullable=False)


class Price(Base):
    __tablename__ = 'prices'

    guid = Column(String(32), primary_key=True)
    commodity_guid = Column(String(32), nullable=False)
    currency_guid = Column(String(32), nullable=False)
    date = Column(DateTime, nullable=False)
    source = Column(String(2048))
    type = Column(String(2048))
    value_num = Column(BigInteger, nullable=False)
    value_denom = Column(BigInteger, nullable=False)


class Recurrence(Base):
    __tablename__ = 'recurrences'

    id = Column(Integer, primary_key=True, server_default=text("nextval('recurrences_id_seq'::regclass)"))
    obj_guid = Column(String(32), nullable=False)
    recurrence_mult = Column(Integer, nullable=False)
    recurrence_period_type = Column(String(2048), nullable=False)
    recurrence_period_start = Column(Date, nullable=False)
    recurrence_weekend_adjust = Column(String(2048), nullable=False)


class Schedxaction(Base):
    __tablename__ = 'schedxactions'

    guid = Column(String(32), primary_key=True)
    name = Column(String(2048))
    enabled = Column(Integer, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    last_occur = Column(Date)
    num_occur = Column(Integer, nullable=False)
    rem_occur = Column(Integer, nullable=False)
    auto_create = Column(Integer, nullable=False)
    auto_notify = Column(Integer, nullable=False)
    adv_creation = Column(Integer, nullable=False)
    adv_notify = Column(Integer, nullable=False)
    instance_count = Column(Integer, nullable=False)
    template_act_guid = Column(String(32), nullable=False)


class Slot(Base):
    __tablename__ = 'slots'

    id = Column(Integer, primary_key=True, server_default=text("nextval('slots_id_seq'::regclass)"))
    obj_guid = Column(String(32), nullable=False, index=True)
    name = Column(String(4096), nullable=False)
    slot_type = Column(Integer, nullable=False)
    int64_val = Column(BigInteger)
    string_val = Column(String(4096))
    double_val = Column(Float(53))
    timespec_val = Column(DateTime)
    guid_val = Column(String(32))
    numeric_val_num = Column(BigInteger)
    numeric_val_denom = Column(BigInteger)
    gdate_val = Column(Date)


class Split(Base):
    __tablename__ = 'splits'

    guid = Column(String(32), primary_key=True)
    tx_guid = Column(String(32), nullable=False, index=True)
    account_guid = Column(String(32), nullable=False, index=True)
    memo = Column(String(2048), nullable=False)
    action = Column(String(2048), nullable=False)
    reconcile_state = Column(String(1), nullable=False)
    reconcile_date = Column(DateTime)
    value_num = Column(BigInteger, nullable=False)
    value_denom = Column(BigInteger, nullable=False)
    quantity_num = Column(BigInteger, nullable=False)
    quantity_denom = Column(BigInteger, nullable=False)
    lot_guid = Column(String(32))


class TaxtableEntry(Base):
    __tablename__ = 'taxtable_entries'

    id = Column(Integer, primary_key=True, server_default=text("nextval('taxtable_entries_id_seq'::regclass)"))
    taxtable = Column(String(32), nullable=False)
    account = Column(String(32), nullable=False)
    amount_num = Column(BigInteger, nullable=False)
    amount_denom = Column(BigInteger, nullable=False)
    type = Column(Integer, nullable=False)


class Taxtable(Base):
    __tablename__ = 'taxtables'

    guid = Column(String(32), primary_key=True)
    name = Column(String(50), nullable=False)
    refcount = Column(BigInteger, nullable=False)
    invisible = Column(Integer, nullable=False)
    parent = Column(String(32))


class Transaction(db.Model):
    __tablename__ = 'transactions'

    guid = Column(String(32), primary_key=True)
    currency_guid = Column(String(32), nullable=False)
    num = Column(String(2048), nullable=False)
    post_date = Column(DateTime, index=True)
    enter_date = Column(DateTime)
    description = Column(String(2048))


class Vendor(Base):
    __tablename__ = 'vendors'

    guid = Column(String(32), primary_key=True)
    name = Column(String(2048), nullable=False)
    id = Column(String(2048), nullable=False)
    notes = Column(String(2048), nullable=False)
    currency = Column(String(32), nullable=False)
    active = Column(Integer, nullable=False)
    tax_override = Column(Integer, nullable=False)
    addr_name = Column(String(1024))
    addr_addr1 = Column(String(1024))
    addr_addr2 = Column(String(1024))
    addr_addr3 = Column(String(1024))
    addr_addr4 = Column(String(1024))
    addr_phone = Column(String(128))
    addr_fax = Column(String(128))
    addr_email = Column(String(256))
    terms = Column(String(32))
    tax_inc = Column(String(2048))
    tax_table = Column(String(32))


class Version(Base):
    __tablename__ = 'versions'

    table_name = Column(String(50), primary_key=True)
    table_version = Column(Integer, nullable=False)
