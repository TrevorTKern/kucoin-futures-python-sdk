from kucoin.base_request.base_request import KucoinBaseRestApi

class TradeData(KucoinBaseRestApi):
    def placeMarketOrder(self,side, symbol, leverage, clientOid='', **kwargs):
        params = {
            'clientOid': clientOid,
            'side': side,
            'symbol': symbol,
            'leverage': leverage,
            'type': 'market'
        }
        if kwargs:
            params.update(kwargs)
        return self.request('POST', '/api/v1/orders', params = params)
    
    def placeLimitOrder(self, price, size, **kwargs):
        params = {
            'price': price,
            'size': size,
            'type': 'limit'
        }
        if kwargs:
            params.update(kwargs)
        return self.request('POST', '/api/v1/orders', params = params)

    def cancelOrder(self, id):
        return self.request('DELETE', '/api/v1/orders/{}'.format(id))

    def limitMassCancel(self, symbol=None):
        params = {}
        if symbol:
            params['symbol'] = symbol
        return self.request('DELETE', '/api/v1/orders', params = params)

    def stopMassCancel(self, symbol=None):
        params = {}
        if symbol:
            params['symbol'] = symbol
        return self.request('DELETE', '/api/v1/stopOrders', params = params)

    def getOrderList(self, **kwargs):
        params = {}
        if kwargs:
            params.update(kwargs)
        return self.request('GET', '/api/v1/orders', params = params)

    def getUntriggeredStops(self, **kwargs):
        params = {}
        if kwargs:
            params.update(kwargs)
        return self.request('GET', '/api/v1/stopOrders', params = params)
    
    def getRecentOrders(self):
        return self.request('GET', '/api/v1/recentDoneOrders')

    def getOrderDetails(self, id):
        return self.request('GET', '/api/v1/orders/{}'.format(id))

    def getFills(self, **kwargs):
        params = {}
        if kwargs:
            params.udpate(kwargs)
        return self.request('GET', '/api/v1/fills', params = params)

    def getRecentFills(self):
        return self.request('GET', '/api/v1/recentFills')

    def activeOrderValue(self, symbol):
        params = {'symbol': symbol}
        return self.request('GET', '/api/v1/openOrderStatistics', params = params)

    def getPositionDetails(self, symbol):
        params = {'symbol': symbol}
        return self.request('GET', '/api/v1/position', params = params)

    def getPositionList(self):
        return self.request('GET', '/api/v1/positions')

    def autoDepositMargin(self, symbol, status):
        params = {
            'symbol': symbol,
            'status': status
        }
        return self.request('POST', '/api/v1/position/margin/auto-deposit-status', params = params)

    def addMarginManually(self, symbol, margin, bizNo):
        params = {
            'symbol': symbol,
            'margin': margin,
            'bizNo': bizNo
        }
        return self.request('POST', '/api/v1/position/margin/deposit-margin', params = params)

    def getFundingHistory(self, symbol, **kwargs):
        params = {'symbol': symbol}
        if kwargs:
            params.update(kwargs)
        return self.request('GET', '/api/v1/funding-history', params = params)