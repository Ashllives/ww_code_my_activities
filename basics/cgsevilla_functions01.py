""" Mang Toto's ForEx Challenge
Author:
Description: Aling Nena's Sari-sari store just had a new neighbor! It's Mang Toto's ForEx!
Help Mang Toto to convert `USD, JPY, SGD` to `PHP` by:
* Asking the customer for their currency.
>> Welcome to Mang Toto's ForEx! What is your currency? We accept (usd, jpy, sgd):
* If they are not exchanging the currrency, notify the customer.
>> Welcome to Mang Toto's ForEx! What is your currency? We accept (usd, jpy, sgd):
>> aud
>> Sorry! We do not exchange aud!
* If they are in their currency list, ask for the amount and inform the original and equivalent PHP amount.
>> Welcome to Mang Toto's ForEx! What is your currency? We accept (usd, jpy, sgd):
>> usd
>> Your 100.50 usd is equivalent to 5069.22 PHP
"""

# import locale
# locale.setlocale(locale.LC_ALL, 'en_US')

PHP_EXCHANGE_RATE = {
  'usd': 50.44,
  'jpy': 0.45,
  'sgd': 36.25
}


def converter(currency, amount):
    # Replace pass with your block of code
    if currency == 'usd':
        return float(float(amount) * PHP_EXCHANGE_RATE['usd'])
    elif currency == 'jpy':
        return float(float(amount) * PHP_EXCHANGE_RATE['jpy'])
    elif currency == 'sgd':
        return float(float(amount) * PHP_EXCHANGE_RATE['sgd'])

currency = input("Welcome to Mang Toto's ForEx! What is your currency? We accept {}.".format(', '.join(list(PHP_EXCHANGE_RATE.keys())))).lower()
# print(currency)

if currency in list(PHP_EXCHANGE_RATE):
    amount = input("How much would you like to exchange?")
else:
    print("Sorry! We do not exchange " + currency + '.')



print("Your {} {} is equivalent to PHP {:,}".format(amount, currency.upper(), converter(currency, amount)))

#i used {:,} to put commas in my conversion amount