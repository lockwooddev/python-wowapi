from .exceptions import APIError

import logging
import requests


logger = logging.getLogger("wowapi")


class APIConnector(object):

    allowed_filters = []
    resource = ""

    def __init__(self, host, *args, **kwargs):
        self.kwargs = kwargs
        self.args = args
        self.protocol = "https://" if self.kwargs.get("secure") else "http://"

    def get_query_parameters(self):
        params = {}
        for f in self.kwargs:
            if f in self.allowed_filters:
                params[f] = self.kwargs[f]
        return params

    def get_url(self):
        base = self.protocol + "api/wow/" + self.resource
        url = base + "/".join(self.args)
        return url

    def get_resource(self):
        url = self.get_url()
        params = self.get_query_parameters()

        try:
            response = requests.get(url, params=params)
        except requests.Timeout, e:
            logger.error("Timeout for %s" % url)
            raise APIError(e)
        except requests.ConnectionError, e:
            logger.error("ConnectionError for %s" % url)
            raise APIError(e)
        except requests.HTTPError, e:
            logger.error("HTTPError for %s" % url)
            raise APIError(e)

        if not response.ok:
            logger.error("API response (%i) not okay for %s" %
                (response.status_code, url))
            raise APIError(response.status_code, response.json()["reason"])

        try:
            json_response = response.json()
        except ValueError, e:
            logger.error("No JSON object could be decoded for %s" % url)
            raise APIError(e)

        return json.loads(json_response)


class AuctionConnector(APIConnector):
    allowed_filters = []
    resource = "auction/data/"


class ItemConnector(APIConnector):
    allowed_filters = ['locale']
    resource = "item/"