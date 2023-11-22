import time
import logging

from functools import wraps


def backoff(error, start_sleep_time: float = 0.1, factor: int = 2, border_sleep_time: int = 10):
    def func_wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            n = 1
            t = start_sleep_time
            while True:
                try:
                    return func(*args, **kwargs)
                except error:
                    t = start_sleep_time * factor**n if t < border_sleep_time else border_sleep_time
                    n += 1
                    time.sleep(t)
                    logging.error("Connection is broken. Reconnection after %s seconds")

        return inner

    return func_wrapper
