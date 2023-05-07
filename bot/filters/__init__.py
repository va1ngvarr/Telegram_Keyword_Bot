from aiogram import Dispatcher
from .is_admin import IsAdmin


def register_all_filters(dp: Dispatcher):
    # todo: register all filters - dp.bind_filter()
    filters = (IsAdmin,)
    for filter in filters:
        dp.bind_filter(filter)
