from mock import patch, Mock
from archives_app.middleware import IsTokenValidMiddleware
import unittest


class TestMiddleware(unittest.TestCase):

    @patch('archives_app.middleware.IsTokenValidMiddleware')
    def test_init(self, my_middleware_mock):
        my_middleware = IsTokenValidMiddleware('response')
        assert(my_middleware.get_response) == 'response'

    def test_mymiddleware(self):
        request = Mock()
        my_middleware = IsTokenValidMiddleware(Mock())
        my_middleware(request)
