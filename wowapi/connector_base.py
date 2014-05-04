from .exceptions import WowApiError, WowApiClientError

import requests


class APIConnector(object):

    filters = []
    resource = ""

    def __init__(self, host, *args, **kwargs):
        self.host = host
        self.kwargs = kwargs
        self.args = args
        self.protocol = "https://" if self.kwargs.get("secure") else "http://"

    def get_query_parameters(self):
        params = {}
        for _filter in self.kwargs:
            if _filter in self.filters:
                params[_filter] = self.kwargs[_filter]
        return params

    def get_url(self):
        base = self.protocol + self.host + "/api/wow/" + self.resource
        url = base + "/".join(self.args)
        return url

    def handle_request(self, url, params=None):
        try:
            response = requests.get(url, params=params)
        except requests.RequestException as e:
            raise WowApiClientError(e)

        try:
            json_data = response.json()
        except ValueError:
            raise WowApiClientError(
                '{} - Missing json - {}'.format(response.status_code, response.content))

        if not response.ok:
            if 'status' in json_data.keys():
                raise WowApiError(
                    response.status_code, json_data['status'], json_data.get('reason'))

            raise WowApiClientError(
                '{} - Something went wrong - {}'.format(
                    response.status_code, response.content))

        return json_data

    def get_resource(self):
        url = self.get_url()
        params = self.get_query_parameters()
        result = self.handle_request(url, params=params)
        return result
