import requests
from requests.exceptions import RequestException


def get_an_image(url: str):
    """
    Get the content of an image with requests library.

    :param url: URL pointing to the image.
    :return: an array of strings, each representing a line.
    """
    try:
        response = requests.get(url)
        data = response.text
        data_array = data.split("\n")
        return [data_point for data_point in data_array if data_point]
    except RequestException as err:
        raise ValueError(str(err))


def get_upper_frame(array_: list):
    """
    Construct a frame for an ASC-II image.

    :param array_: the data array of an ASC-II image.
    :return: The upper and lower frame, in the string format of '+-----+'.
    """
    width = len(array_[0])
    return '+' + '-' * width + '+'
