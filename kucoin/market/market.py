from kucoin.base_request.base_request import KucoinBaseRestApi


class MarketData(KucoinBaseRestApi):
    def getOpenContracts(self):
        return self.request('GET', '/api/v1/contracts/active')

    def getContractInfo(self, symbol):
        return self.request('GET', '/api/v1/contracts/{}'.format(symbol))

    def getTicker(self, symbol):
        params = {'symbol': symbol}
        return self.request('GET', '/api/v1/ticker', params = params)

    def getFullOrderBook(self, symbol):
        params = {'symbol': symbol}
        return self.reqest('GET', '/api/v1/level2/snapshot', params = params)

    def getPartOrderBook(self, symbol, depth=20):
        params = {'symbol': symbol}
        if depth == 100:
            return self.request('GET', '/api/v1/level2/depth100', params = params)
        else:
            return self.request('GET', '/api/v1/level2/depth20', params = params)

    def pullMessages(self, symbol, start, end):
        params = {
            'symbol': symbol,
            'start': start,
            'end': end
        }
        return self.request('GET', '/api/v1/level2/message/query', params = params)

    def transactionHistory(self, symbol):
        params = {'symbol': symbol}
        return self.request('GET', '/api/v1/trade/history', params = params)

    def getInterestRateList(self, symbol, **kwargs):
        params = {'symbol': symbol}
        if kwargs:
            params.udpate(kwargs)
        return self.request('GET', '/api/v1/interest/query', params = params)

    def getIndexList(self, symbol, **kwargs):
        params = {'symbol': symbol}
        if kwargs:
            params.udpate(kwargs)
        return self.request('GET', '/api/v1/index/query', params = params)
    
    def getMarketPrice(self, symbol):
        return self.request('GET', '/api/v1/mark-price/{}}/current'.format(symbol))
    
    def getPremiumIndex(self, symbol, **kwargs):
        params = {'symbol': symbol}
        if kwargs:
            params.update(kwargs)
        return self.request('GET', '/api/v1/premium/query', params = params)

    def getCurrentFundingRate(self, symbol):
        return self.request('GET', '/api/v1/funding-rate/{}/current'.format(symbol))

    def getServerTime(self):
        return self.request('GET', '/api/v1/status')

    def getKline(self, symbol, granularity, **kwargs):
        params = {
            'symbol': symbol,
            'granularity': granularity
        }
        if kwargs:
            params.update(kwargs)
        return self.request('GET', '/api/v1/kline/query', params = params)