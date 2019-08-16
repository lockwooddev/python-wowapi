import os

import pytest

from wowapi import WowApi


class TestWowApiLive:

    COUNTRIES = ['us', 'eu', 'kr', 'tw']

    def setup_method(self, method):
        self.api = WowApi(os.environ['WOW_CLIENT_ID'], os.environ['WOW_CLIENT_SECRET'])
        for code in self.COUNTRIES:
            data = self.api.get_token(code, namespace='dynamic-{0}'.format(code))
            assert '_links' in data

        data = self.api.get_token('eu', namespace='dynamic-eu')

    @pytest.mark.parametrize('code', ['us', 'eu', 'kr', 'tw'])
    def test_get_achievement(self, code):
        assert self.api.get_achievement(code, 2144)

    # @pytest.mark.parametrize('code', ['us', 'eu', 'kr', 'tw'])
    # def test_get_auctions(self):
    #     assert self.api.get_auctions(code, '')