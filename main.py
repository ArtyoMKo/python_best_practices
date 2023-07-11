"""
Docstrings and annotations
"""

from dataclasses import dataclass
from datetime import date
from typing import List
import logging

from helpers.iterables import DateRangeIterable


def first_example_of_docstring_usage():
    """
    First example of usage docstrings
    :return: None
    """
    return None


@dataclass
class Point:
    """
    Providing latitude and longitude
    """

    lat: float
    long: float


def locate(latitude: float, longitude: float) -> Point:
    """
    Finding object in a map
    ----------------------
    :param latitude: float
    :param longitude: float
    :return: Point
    """
    return Point(latitude, longitude)


def get_data_from_response(response: dict) -> dict:
    """
    If the response status is OK, return its payload.
    - response: A dict like::
    {
        "status": 200,
        "timestamp": "....",
        "payload": { ... }
    }
    - Returns a dict like::
    {"data": { ... }}

    - Raises:
    - ValueError if the HTTP status code is != 200
    """
    if response["status"] != 200:
        raise ValueError
    return {"data": response["payload"]}


def print_some_notifications(log: str, list_of_users: List[str]):
    """
    Logging message per each user
    :param log: str
    :param list_of_users: list
    :return: None
    """
    for user in list_of_users:
        logging.warning(f"{log}: {user}")


if __name__ == "__main__":
    print_some_notifications("log", ["Artyom"])
    print(get_data_from_response.__doc__)
    print(locate.__doc__)
    print(locate.__annotations__)
    print(locate(1, 1))
    datetime_range = DateRangeIterable(date(2023, 3, 3), date(2023, 3, 9))
    print(f"max: {max(datetime_range)}")
    print(next(datetime_range))
    print(next(datetime_range))
