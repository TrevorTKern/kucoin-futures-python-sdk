===============================
Welcome to python-kucoin-futures-sdk
===============================

.. image:: https://img.shields.io/pypi/l/python-kucoin
    :target: https://github.com/Kucoin/kucoin-python-sdk/blob/master/LICENSE

.. image:: https://img.shields.io/badge/python-3.6%2B-green
    :target: https://pypi.org/project/python-kucoin


Features
--------

- Implementation of REST endpoints
- Simple handling of authentication
- Response exception handling
- Implement websockets (note only python3.6+)

Quick Start
-----------

Register an account with `KuCoin <https://futures.kucoin.com/signup>`_.

To test on the Sandbox  with `KuCoin Sandbox <https://sandbox-futures.kucoin.com>`_.

`Generate an API Key <https://futures.kucoin.com/api>`_
or `Generate an API Key in Sandbox <hhttps://sandbox.kucoin.com/api?lang=en_US>`_ and enable it.

.. code:: python

    #Get open contracts
    from kucoin.client import Market

    #Create client
    client = Market()

    #contracts = client.getOpenContracts('https://api-futures.kucoin.com')
    #also works but 'https://api-futures.kucoin.com' is default unless is_sandbox=True

    #or connect to sandbox
    #client = Market(is_sandbox=True)
    #client = Market('https://api-sandbox-futures.kucoin.com')

    #Get open contracts
    openContracts = client.getOpenContracts()
    print(openContracts)

    from kucoin.client import User

    api_key = '<api_key>'
    api_secret = '<api_secret>'
    api_passphrase = '<api_passphrase>'

    #Create User client
    client = User(api_key, api_secret, api_passphrase)

    #Sandbox
    #client = User(api_key, api_secret, api_passphrase, is_sandbox=True)

    #getAccountOverview takes an optional currency, default BTC
    #overview = client.getAccountOverview('USDT')
    overview = client.getAccountOverview()
    print(overview)

    from kucoin.client import Trade

    #Create Trade client
    client = Trade(api_key, api_secret, api_passphrase)

    # or connect to Sandbox
    # client = Trade(api_key, api_secret, api_passphrase, is_sandbox=True)

    #place order
    orderId = client.placeMarketOrder('buy', 'XBTUSDM', '1', clientOid='', size='8000')

    #cancel open order
    client.cancelOrder('<clientOid>')

Websockets
----------

.. code:: python

    import asyncio
    from kucoin.client import WsToken
    from kucoin.ws_client import KucoinWsClient

    async def main():
        async def deal_msg(msg):
            if msg['topic'] == '/contract/instrument:XBTUSDM':
                print(msg["data"])
            elif msg['topic'] == '/contract/instrument:XBTUSDM':
                print(f'Get KCS level3:{msg["data"]}')

        client = WsToken()
        ws_client = await KucoinWsClient.create(None, client, deal_msg, private=False)
        await ws_client.subscribe('/contract/instrument:XBTUSDM')
        while True:
            await asyncio.sleep(60, loop=loop)

    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
