from abc import ABC, abstractmethod

class LegacyPaymentGateway:
    def process_credit_card_payment(self, credit_card_number: str, expiration_date: str, cvv: str, amount: float) -> bool:
        print("Simulates processing a credit card payment ...")
        return True

class PayPalPaymentGateway(ABC):
    @abstractmethod
    def process_paypal_payment(self, email_address: str, amount: float) -> bool:
        pass

class PaymentAdapter(PayPalPaymentGateway):
    def __init__(self, obj: LegacyPaymentGateway) -> None:
        self.__obj = obj

    def process_paypal_payment(self, email_address: str, amount: float) -> bool:
        credit_card_number = self.get_credit_card_number(email_address)
        expiration_date = self.get_expiration_date(email_address)
        cvv = self.get_cvv(email_address)
        status = self.__obj.process_credit_card_payment(credit_card_number, expiration_date, cvv, amount)
        if status is True:
            print("Seccess!")
        else:
            print("Fail!")

        return status

    def get_credit_card_number(self, email_address):
        return "1234-5678-9012-3456"
    
    def get_expiration_date(self, email_address):
        return "12/34"
    
    def get_cvv(self, email_address):
        return "567"

class PaymentFactory:
    @staticmethod
    def get_payment_system() -> PayPalPaymentGateway:
        obj = LegacyPaymentGateway()
        return PaymentAdapter(obj)

def main():
    obj = LegacyPaymentGateway()
    payment_adapter = PaymentAdapter(obj)

    paypal_email = "deposit@bank.com"
    payment_amount = 100.0
    if payment_adapter.process_paypal_payment(paypal_email, payment_amount):
        print("PayPal payment processed successfully through the adapter.")
    else:
        print("PayPal payment failed !")

if  __name__ == "__main__":
   main()
