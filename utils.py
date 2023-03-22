import requests
import json

from config import keys

class APIException(Exception):
    pass

class CryptoConverter:

    @staticmethod
    def convert(from_: str, to_: str, amount_: str):

        if from_ == to_:
            raise APIException("Невозможно перевести одинаковые валюты")
        try:
            from_ticker = keys[from_]
        except KeyError:
            raise APIException(f"*{from_}* - данная валюта не найдена в списке возможных для конвертации")

        try:
            to_ticker = keys[to_]
        except KeyError:
            raise APIException(f"*{to_}* - данная валюта не найдена в списке возможных для конвертации")
        try:
            amount_ = float(amount_)
        except ValueError:
            raise APIException(f'Не удалось обработать количество *{amount_}*')

        r = requests.get(
            f"https://min-api.cryptocompare.com/data/price?fsym={from_ticker}&tsyms={to_ticker}")

        answer_to_user = json.loads(r.content)[keys[to_]]
        return answer_to_user