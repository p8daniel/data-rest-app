from peewee import CharField, AutoField, ForeignKeyField, IntegerField, \
    FloatField, BooleanField, Model
from playhouse.shortcuts import model_to_dict

from .database import db


class CommonModel(Model):
    def get_small_data(self):
        return model_to_dict(self, recurse=True, backrefs=True)

    class Meta:
        database = db


class HatColor(CommonModel):
    label = CharField(primary_key=True)


class Hat(CommonModel):
    id = AutoField()
    color = ForeignKeyField(HatColor)


class Character(CommonModel):
    id = AutoField()
    name = CharField()
    age = IntegerField()
    weight = FloatField()
    human = BooleanField()
    hat = ForeignKeyField(Hat, backref='hat', unique=True, null=True)


with db:
    HatColor.create_table(safe=True)
    Hat.create_table(safe=True)
    Character.create_table(safe=True)
    if not HatColor.select().exists():
        defaults = ["PURPLE", "YELLOW", "GREEN"]
        HatColor.insert_many(
            [{'label': label} for label in defaults]).execute()
