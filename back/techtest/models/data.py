import time
from peewee import CharField, AutoField, FloatField, Model, DateTimeField

from .database import db


class Data(Model):
    id = AutoField()
    created_date = DateTimeField(default=time.strftime("%Y-%m-%d %H:%M:%S"))
    name = CharField()
    value = FloatField()

    class Meta:
        database = db


with db:
    Data.create_table(safe=True)
