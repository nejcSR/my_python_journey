import requests

url="https://v6.exchangerate-api.com/v6/c8becf87d8788d521596286b/latest/EUR"
API_KEY="64188d7c5bece2a8e5e3a968"

response=requests.get(url)
data=response.json()

def conversion_rates():
    rates=data["conversion_rates"]
    return rates

def convert_currency(amount, from_currency, to_currency):
    rates=conversion_rates()
    
    if from_currency !="EUR":
        if from_currency in rates:
            amount=amount / rates[from_currency]
        else:
            print(f"Unknown from_currency: {from_currency}")
            return None
        
    if to_currency in rates:
        converted_amount=amount*rates[to_currency]
        return converted_amount
    else:
        print(f"Unknown to_currency: {to_currency}")
        
def main():
    while True:
        amount=float(input("Enter amount: "))
        from_currency =input("convert from (currency code, example: EUR): ").upper()
        to_currency=input("Convert to(currency code, example: USD): USD): ").upper()
        
        result=convert_currency(amount, from_currency, to_currency)
        if result is not None:
            print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")

if __name__ == "__main__":
    main()
    