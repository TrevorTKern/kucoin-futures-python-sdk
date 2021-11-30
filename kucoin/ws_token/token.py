from kucoin.base_request.base_request import KucoinBaseRestApi


class GetToken(KucoinBaseRestApi):

    def get_ws_token(self, is_private=False):
        uri = '/api/v1/bullet-public'
        if is_private:
            uri = '/api/v1/bullet-private'

        return self.request('POST', uri, auth=is_private)


