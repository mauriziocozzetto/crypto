import streamlit as st
import matplotlib.pyplot as plt


class CryptoView:

    def __init__(self, cryptos_dict, currencies_dict):
        st.title("Crypto Price History")
        self.crypto = st.selectbox("Select a cryptocurrency:", cryptos_dict)
        self.currency = st.selectbox("Select a currency:", currencies_dict)
        self.days = st.number_input("Enter number of days:",
                                    min_value=3,
                                    max_value=50,
                                    value=10,
                                    step=1)
        self.plot_button = st.button("Plot Price History")

    def is_plot_button_clicked(self):
        """ serve a gestire il click sul pulsante """
        return self.plot_button

    def display_plot(self, data, crypto_name, currency_name):
        """ visualizza il diagramma a linee con le date su X e i prezzi su Y """
        dates = data.keys()
        prices = data.values()
        plt.figure(figsize=(10, 5))
        plt.plot(dates, prices, marker='o')
        plt.title(f'{crypto_name.capitalize()} Price History')
        plt.xlabel('Date')
        plt.ylabel(f'Price ({currency_name.upper()})')
        plt.xticks(rotation=90)
        plt.tight_layout()
        st.pyplot(plt)

    def get_crypto(self):
        return self.crypto

    def get_currency(self):
        return self.currency

    def get_days(self):
        return self.days

    def display_error(self, error_message):
        st.error(error_message)
