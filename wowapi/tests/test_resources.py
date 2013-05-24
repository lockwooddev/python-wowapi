from wowapi.resources import APIResource

import json
from mock import patch
import unittest


class APIResourceTest(unittest.TestCase):

    def setup(self):
        pass

    def test_resource_properties(self):
        d = {
            "id": 9999,
            "name": "test",
            "container": [
                {"a": 1},
                {"b", 2}
            ]
        }
        resource = APIResource(d)
        self.assertTrue(hasattr(resource, "id"))
        self.assertTrue(hasattr(resource, "name"))
        self.assertTrue(hasattr(resource, "container"))