import keyword


class APIResource(object):

    def __init__(self, response_dict, all_keywords=False):
        self.data = response_dict

        # set all first row keys as attribute
        if all_keywords:
            for key in self.data:
                if key in keyword.kwlist:
                    setattr(self, key+"_", self.data[key])
                else:
                    setattr(self, key, self.data[key])
