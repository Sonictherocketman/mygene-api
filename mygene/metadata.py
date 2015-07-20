""" Models the metadata results of the MyGene API. """


import json

from api import get, endpoints


class Metadata(object):
    """ Models the MyGene metadata API results,
    and associated methods.
    """

    def __init__(self, entries):
        self.__dict__.update(entries)

    @staticmethod
    def get_metadata():
        """ Retrieves the metadata from the MyGene API.
        :returns metadata:
        """
        data = get(endpoints['get-metadata'])
        return Metadata(data)
