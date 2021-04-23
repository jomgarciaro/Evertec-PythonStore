from dotenv import load_dotenv
from pathlib import Path
from os import getenv
from datetime import datetime, timedelta
from random import random
from base64 import b64encode
from hashlib import sha1

import requests

base_dir = Path(__file__).resolve().parent / ".env"
load_dotenv(base_dir)
print(base_dir)


class Connection:

    """
    This class creates connection type objects that allow the payment
    request to be made through PlaceToPay's web-checkout service.
    In addition, the connection type objects can request information
    about the payment status.
    """

    __login = getenv("LOGIN")
    __secret_key = getenv("SECRET_KEY").encode("utf-8")
    nonce = str(random()).encode("utf-8")

    def make_payment(
        self,
        costumer_id,
        costumer_name,
        costumer_email,
        costumer_mobile,
    ):
       
        """
        This method allows the request of a payment session through PlaceToPlay's 
        web-checkout service.
        """

        seed = (
            datetime.now()
            .astimezone()
            .replace(microsecond=0)
            .isoformat()
            .encode("utf-8")
        )
        tran_key = b64encode(sha1(self.nonce + seed + self.__secret_key).digest())
        expiration = (
            datetime.now().astimezone().replace(microsecond=0) + timedelta(days=1)
        ).isoformat()

        payment_data = {
            "auth": {
                "login": self.__login,
                "tranKey": tran_key.decode("utf-8"),
                "nonce": b64encode(self.nonce).decode("utf-8"),
                "seed": seed.decode("utf-8"),
            },
            "locale": "es_CO",
            "buyer": {
                "name": costumer_name,
                "surname": costumer_name,
                "email": costumer_email,
                "document": "1040035000",
                "documentType": "CC",
                "mobile": costumer_mobile,
            },
            "payment": {
                "reference": costumer_id,
                "description": f"Pago básico de prueba {costumer_id}",
                "amount": {"currency": "COP", "total": "10000"},
                "allowPartial": False,
            },
            "expiration": expiration,
            "returnUrl": f"http://localhost:8000/order_status/{costumer_id}",
            "ipAddress": "127.0.0.1",
            "userAgent": "PlacetoPay Sandbox",
        }

        response = requests.post(
            "https://test.placetopay.com/redirection/api/session", json=payment_data
        )

        return response

    def payment_status(self, request_id):

        """
        This method allows requesting information about the payment status using the value 
        of the requestId provided in the response to the original payment request.
        """

        seed = (
            datetime.now()
            .astimezone()
            .replace(microsecond=0)
            .isoformat()
            .encode("utf-8")
        )
        tran_key = b64encode(sha1(self.nonce + seed + self.__secret_key).digest())
        expiration = (
            datetime.now().astimezone().replace(microsecond=0) + timedelta(days=1)
        ).isoformat()

        payment_data = {
            "auth": {
                "login": self.__login,
                "tranKey": tran_key.decode("utf-8"),
                "nonce": b64encode(self.nonce).decode("utf-8"),
                "seed": seed.decode("utf-8"),
            },
        }

        response = requests.post(
            f"https://test.placetopay.com/redirection/api/session/{request_id}",
            json=payment_data,
        )

        return response
