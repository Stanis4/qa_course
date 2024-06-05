from typing import Optional

import requests
from requests import Response

import homework_15.config as config


class APIInterface:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
        }

    def _get(self, endpoint: str, params=None, **kwargs) -> Response:
        return requests.get(config.api.url + endpoint, headers=self.headers, params=params)

    def _post(self, endpoint: str, json=None, timeout: int = None, files: dict = None, data: dict = None) -> Response:
        return requests.post(config.api.url + endpoint, json=json, data=data, headers=self.headers, files=files,
                             timeout=timeout)

    def _put(self, endpoint: str, body=None) -> Response:
        return requests.put(config.api.url + endpoint, json=body, headers=self.headers)

    def _patch(self, endpoint: str, body=None) -> Response:
        return requests.patch(config.api.url + endpoint, data=body, headers=self.headers)

    def _delete(self, endpoint: str, params: Optional[dict] = None, body=None) -> Response:
        return requests.delete(config.api.url + endpoint, data=body, headers=self.headers, params=params)
