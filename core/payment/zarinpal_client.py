import requests
import json

class ZarinPalSandbox:
    _payment_request_url = "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
    _payment_verify_url = "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
    _payment_page_url = "https://sandbox.zarinpal.com/pg/StartPay"
    _callback_url = "https://redreseller.com/verify"

    def __init__(self, merchant_id):
        self.merchant_id = merchant_id

    def payment_request(self,amount, callback_url, description="پرداختی کاربر"):
        payload = {
            "MerchantID": self.merchant_id,
            "Amount": str(amount),
            "CallbackURL": self._callback_url,
            "Description": description,
        }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(
            self._payment_request_url, headers=headers, data=json.dumps(payload)
        )

        return response.json()

    def payment_verify(self,amount, authority):
        payload = {
            "MerchantID": self.merchant_id,
            "Amount": amount,
            "Authority": authority
        }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(
            self._payment_verify_url, headers=headers, data=json.dumps(payload)
        )
        return response.json()
        

    def generate_payment_url(self, authority):
        return self._payment_page_url + authority
    

if __name__ == "__main__":
    zarinpal = ZarinPalSandbox(merchant_id="4ced0ale-4ad8-4309-9668-3ea3ae8e8897")
    print(zarinpal.payment_request(15000))
