class CryptoController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        # se l'utente ha fatto click sul pulsante
        if self.view.is_plot_button_clicked():
            crypto_name = self.view.get_crypto(
            )  # prende dalla view il nome della criptovaluta
            days = self.view.get_days(
            )  # dalla view prende il numero di giorni
            currency_name = self.view.get_currency()  # e il nome della valuta
            history = self.model.get_crypto_history(
                crypto_name, currency_name,
                days)  # ottiene il dizionario dal modello

            if history:
                self.view.display_plot(
                    history, crypto_name,
                    currency_name)  # la view visualizza il diagramma a linee
            else:
                self.view.display_error('Problemi con la history')
