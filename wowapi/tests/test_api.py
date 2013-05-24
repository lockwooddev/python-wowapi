from wowapi.api import WowAPIResource

import unittest


class WowAPIResourceTest(unittest.TestCase):

    def setUp(self):
        self.host = "eu.battle.net"

    def test_get_query_parameters(self):
        instance = WowAPIResource(self.host, locale="en_GB", custom="test")
        instance.allowed_filters = ["locale", ]
        url_parameters = instance.get_query_parameters()
        self.assertEqual(1, len(url_parameters))
        self.assertNotIn("custom", url_parameters)

    def test_get_url(self):
        instance = WowAPIResource(self.host, "guild", "player")
        url = instance.get_url()
        self.assertEqual("http://api/wow/guild/player", url)

    def test_https(self):
        instance = WowAPIResource(self.host, "guild", "player", secure=True)
        self.assertEqual("https://", instance.protocol)



# if __name__ == '__main__':
#     unittest.main()