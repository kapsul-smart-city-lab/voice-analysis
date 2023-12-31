from requests import request, Response


class Requests:
    def __init__(self, **default_params: dict) -> None:
        self.default_params = default_params

    def request(self, path: list = [], **params: dict) -> Response:
        params = {
            **self.default_params,
            **params
        }

        if 'url' not in params:
            raise "Url must be contain!"

        if 'json' not in params:
            params['json'] = {}

        params['url'] = params['url'] + '/' + "/".join(path)

        return request(**params)


interface = Requests(
    url="http://localhost:7001",
    headers={
        "Content-Type": "application/json"
    }
)


