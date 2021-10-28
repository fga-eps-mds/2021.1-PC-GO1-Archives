from django.http import HttpResponseForbidden
import requests
from dotenv import load_dotenv
import os

VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN')


class IsTokenValidMiddleware(object):
    """
    Middleware class that intercepts all
    requisitios to perform a JWT token check
    and see if the user is logged in or not.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.url = 'api/token/verify/'
        load_dotenv()

    def __call__(self, response):
        response = self.get_response(response)
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        req = requests.post(VERIFY_TOKEN + self.url,
                            data={'token': request.META['HTTP_AUTHORIZATION'][3:]})
        if req.status_code == 401:
            return HttpResponseForbidden()
        return
