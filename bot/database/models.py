from peewee import (
    Model,
    CharField,
    SqliteDatabase,
)

conn = SqliteDatabase("sqlite3.db")


class BaseModel(Model):
    class Meta:
        database = conn


class Channels(BaseModel):
    channel = CharField(max_length=255, unique=True)


class Words(BaseModel):
    word = CharField(max_length=255, unique=True)


class Recipients(BaseModel):
    user = CharField(max_length=255, unique=True)
