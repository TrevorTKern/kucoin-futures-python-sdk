from kucoin.base_request.base_request import KucoinBaseRestApi

class UserData(KucoinBaseRestApi):
    def getAccountOverview(self, currency=None):
        params = {}
        if currency:
            params['currency'] = currency
        return self.request('GET', '/api/v1/account-overview', params = params)

    def getTransactionHistory(self, **kwargs):
        params = {}
        if kwargs:
            params.update(kwargs)
        return self.request('GET', '/api/v1/transaction-history', params = params)

    def getDepositAddress(self, currency):
        
        params = {}
        if currency:
            params['currency'] = currency
        return self.request('GET', '/api/v1/deposit-address', params = params)

    def getDepositsList(self, **kwargs):
        params = {}
        if kwargs:
            params.update(kwargs)
        return self.request('GET', '/api/v1/deposit-list', params = params)

    def getWithdrawLimit(self, currency):
        params = {'currency': currency}
        return self.request('GET', '/api/v1/withdrawals/quotas', params = params)
    
    def withdrawFunds(self, currency, address, amount, **kwargs):
        params = {
            'currency': currency,
            'address': address,
            'amount': amount
        }
        if kwargs:
            params.update(kwargs)
        return self.request('POST', '/api/v1/withdrawals', params = params)

    def getWithdrawList(self, **kwargs):
        params = {}
        if kwargs:
            params.update(kwargs)
        return self.request('GET', '/api/v1/withdrawal-list', params = params)

    def cancelWithdraw(self, id):
        url = '/api/v1/withdrawals/{}'.format(id)
        return self.request('DELETE', url)

    def transferToMainAccount(self, bizNo, amount):
        params = {
            'bizNo': bizNo,
            'amount': amount
        }
        return self.request('POST', '/api/v2/transfer-out', params = params)

    def transferToMainAccount(self, amount, currency):
        params = {
            'currecny': currency,
            'amount': amount
        }
        return self.request('POST', '/api/v2/transfer-out', params = params)
    
    def getTransferOutRecords(self, **kwargs):
        params = {}
        if kwargs:
            params.update(kwargs)
        return self.request('GET', '/api/v1/transfer-list', params = params)
    
    def cancelTransferOutRequest(self, id):
        params = {'applyId': id}
        return self.request('DELETE', '/api/v1/cancel/transfer-out', params = params)