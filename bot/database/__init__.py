from .models import Profile, Channels, Words, Recipients


def register_all_models():
    models = (
        Profile,
        Channels,
        Words,
        Recipients,
    )

    for model in models:
        model.create_table()
