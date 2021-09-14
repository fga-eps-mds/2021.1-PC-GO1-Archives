from django.http import HttpResponseForbidden
import requests
from dotenv import load_dotenv
import os


class IsTokenValidMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, response):
        response = self.get_response(response)
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        load_dotenv()
        VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN')
        req = requests.post(VERIFY_TOKEN + 'api/token/verify/',
                            data={'token': request.META['HTTP_AUTHORIZATION']})

        if req.status_code == 401:
            return HttpResponseForbidden()
        return
