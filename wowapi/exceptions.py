class WowApiError(Exception):

    def __init__(self, status_code, status, reason):
        self.status_code = status_code
        self.status = status
        self.reason = reason

    def __str__(self):
        return '{} - {} - {}'.format(self.status_code, self.status, self.reason)


class WowApiClientError(Exception):

    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return self.error_message
