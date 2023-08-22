from .models import Channels, Words, Recipients


def register_all_models():
    models = (
        Channels,
        Words,
        Recipients,
    )

    for model in models:
        model.create_table()
