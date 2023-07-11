import contextlib
import logging


def stop() -> None:
    """
    Logging stop
    :return: None
    """
    logging.warning("stop")


def start() -> None:
    """
    Logging start
    :return: None
    """
    logging.warning(f"start")


# *** First example of context manager *** #
class DBHandler:
    def __enter__(self):
        stop()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if any((exc_tb, exc_type, exc_tb)):
            logging.error(f"{exc_tb}\n{exc_type}\n{exc_tb}")
        start()


def db_backup_1():
    logging.warning("starting backup")


def main():
    with DBHandler():
        db_backup_1()


# *************************************** #


# *** Second example of context manager *** #
@contextlib.contextmanager
def db_handler():
    try:
        stop()
        yield
    finally:
        start()


with db_handler():
    db_backup_1()
# *************************************** #


# *** 3th example of context manager by decorator *** #
class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        start()


@dbhandler_decorator()
def offline_backup():
    logging.warning(f"offline backup")
