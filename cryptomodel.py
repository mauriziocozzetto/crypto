from datetime import datetime
import requests


class CryptoModel:

    def __init__(self, cryptos_dict, currencies_dict):
        self.history_url = 'https://api.coingecko.com/api/v3/coins/{id}/market_chart'
        self.cryptos_dict = cryptos_dict
        self.currencies_dict = currencies_dict

    def get_crypto_history(self, crypto_name, currency_name, days):
        """ crea un dizionario che sarà la base per il diagramma a linee """
        crypto_id = self.cryptos_dict.get(crypto_name)
        currency_id = self.currencies_dict.get(currency_name)
        params = {'vs_currency': currency_id, 'days': days - 1}
        response = requests.get(self.history_url.format(id=crypto_id),
                                params=params)

        # se la chiamata sincrona fallisce, ritorno None, se è ok, il valore di ritorno è 200
        if response.status_code != 200:
            #raise Exception(f"Failed to retrieve data: {response.status_code}")
            return None

        data = response.json()
        #print('data:', data)  # è un dizionario con 3 chiavi

        # creo il dizionario con le coppie del tipo data: prezzo
        daily_prices = {}

        for price_data in data.get('prices'):
            timestamp = datetime.fromtimestamp(price_data[0] / 1000)
            date = timestamp.strftime('%Y-%m-%d')
            daily_prices[date] = price_data[1]

        #print('daily_prices:', daily_prices)
        return daily_prices


def main():
    cryptos_dict = {'bitcoin': 'bitcoin', 'ethereum': 'ethereum'}
    currencies_dict = {'usd': 'usd', 'eur': 'eur'}
    crypto_model = CryptoModel(cryptos_dict, currencies_dict)
    crypto_name = 'bitcoin'
    currency_name = 'usd'
    days = 2
    daily_prices = crypto_model.get_crypto_history(crypto_name, currency_name,
                                                   days)
    print('daily_prices:', daily_prices)


main()
