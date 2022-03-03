import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_dir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Budget(db.Model):
    __tablename__ = "Budget"
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    sender = db.Column(db.String(80), nullable=True)
    extra_information = db.Column(db.String(200), nullable=True)
    payment_option = db.Column(db.String(100), nullable=True)
    bought_goods_or_services = db.Column(db.String(200), nullable=True)

    def __init__(
            self,
            entry,
            amount,
            sender=None,
            extra_information=None,
            payment_option=None,
            bought_goods_or_services=None,
    ):
        self.entry = entry
        self.amount = amount
        self.sender = sender
        self.extra_information = extra_information
        self.payment_option = payment_option
        self.bought_goods_or_services = bought_goods_or_services

    def __repr__(self):
        if self.entry == "Pajamos":
            return f"{self.entry}: {self.amount}, {self.sender}, {self.extra_information};"
        else:
            return f"{self.entry}: {self.amount}, {self.payment_option}, {self.bought_goods_or_services};"



