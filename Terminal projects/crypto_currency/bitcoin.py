#   Importing Resposories
import sys
import json
import requests


def main():
    '''
        #   Title   :   Crypto Currency
        #   Description :
                Command-line program to calculate usd price for crypto currency

        #   Author : krigjo25
        #   Date :  23.09-22


    '''

    #   Initializing Classes
    req = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    jsonData = json.loads(req.text)

    try:

        #   Ensure the data provided is floating
        if len(sys.argv) != 2: raise Exception("Invalid command-line arguments")
        if sys.argv[1].isalpha(): raise Exception("Useage numberic values")

    except Exception as e:
        sys.exit(f"{e}, Useage : python bitcoin.py [numberic value]")

    #   Initialize variables
    usd = float(sys.argv[1])
    #   Calculate exchangerate
    usd *= jsonData['bpi']['USD']['rate_float']

    print(f'${usd:,.4f}')

    #   Clear memories
    del usd, jsonData, req
    return


if __name__ == '__main__':
    main()
