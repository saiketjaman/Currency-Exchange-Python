import requests
import json

class Currency_convertor: 
    # empty dict to store the conversion rates 
    rates = {}  
    def __init__(self, url): 
        data = requests.get(url).json() 
  
        # Extracting only the rates from the json data 
        self.rates = data["rates"]
    
    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'EUR' : 
            amount = amount / self.rates[from_currency] 
  
        # limiting the precision to 2 decimal places 
        amount = round(amount * self.rates[to_currency], 2)
        result = ('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
        
        data_dict = {
            "initial_amount": initial_amount,
            "from_currency": from_currency,
            "amount": amount,
            "to_currency": to_currency,
        }
        results = {
        "message": "Successfully converted.",
        "converted_results": data_dict,
        "result" : result
        }
        data = json.dumps(results)
        print(data)

# Driver code
if __name__ == "__main__": 
  
    # YOUR_ACCESS_KEY = 'GET YOUR ACCESS KEY FROM fixer.io' 
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', '4ecaac801205c0cc9d409ffe6a471d25')   
    response = Currency_convertor(url) 
    from_country = input("From Country: ") 
    to_country = input("TO Country: ") 
    amount = int(input("Amount: ")) 
    response.convert(from_country, to_country, amount)