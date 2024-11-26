from cryptocontroller import CryptoController
from cryptomodel import CryptoModel
from cryptoview import CryptoView


def main():
    cryptos_dict = {
        'Bitcoin': 'bitcoin',
        'Ethereum': 'ethereum',
        'Ripple': 'ripple',
        'Cardano': 'cardano',
        'Tether': 'tether',
        'Solana': 'solana',
        'Bnb': 'binancecoin'
    }
    currencies_dict = {
        'Dollaro Americano': 'usd',
        'Euro': 'eur',
        'Sterlina Britannica': 'gbp',
        'Yen Giapponese': 'jpy',
        'Dollaro Australiano': 'aud'
    }
    model = CryptoModel(cryptos_dict, currencies_dict)
    view = CryptoView(cryptos_dict, currencies_dict)
    controller = CryptoController(model, view)
    controller.run()


if __name__ == "__main__":
    main()
