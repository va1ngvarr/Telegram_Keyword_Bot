from peewee import (
    Model,
    IntegerField,
    CharField,
    AutoField,
    ForeignKeyField,
    DateTimeField,
    BooleanField,
    SqliteDatabase,
)

conn = SqliteDatabase("sqlite3.db")


class BaseModel(Model):
    class Meta:
        database = conn


class Profile(BaseModel):
    user_id = IntegerField(unique=True)
    username = CharField(max_length=255, null=True)
    chat_id = IntegerField(unique=True)


class Channels(BaseModel):
    channel = CharField(max_length=255, unique=True)


class Words(BaseModel):
    word = CharField(max_length=255, unique=True)


class Recipients(BaseModel):
    user = CharField(max_length=255, unique=True)
