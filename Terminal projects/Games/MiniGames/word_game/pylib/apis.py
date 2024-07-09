# Python Repositories
import os, sys
import random as r
import requests as req

class NinjaAPI():

    #   API-Ninja
    def Check(self, word):

        """
            #   API by API-Ninja
            # Using an api to check if the word exist in the online dictionary.
        """

        parse = f'https://api.api-ninjas.com/v1/dictionary?word={word}'
        response = req.get(parse, headers={'X-Api-Key': os.getenv("Ninja-Api-Token")})

        try:
            if response.text["valid"] == False: raise ValueError()

        except Exception : return False

        #   Clear some space
        del word
        del parse
        del response

        return 

    def Choice(self):

        '''
            #   API by API-Ninja
            #   API to choose a randomly generated word
        '''

        parse = 'https://api.api-ninjas.com/v1/randomword'
        response = req.get(parse, headers={'X-Api-Key': os.getenv("Ninja-Api-Token")})
        string = ""

        try:

            if response.status_code != req.codes.ok: raise Exception("Something went wrong with the connection to Ninja API")
        except Exception as e : return e
        else:

            for i in response.text:
                if i.isalpha(): string += i

        #   Clear some space
        del parse, response

        return string
    
    def Definition(self, word):

        """
            #   API by API-Ninja
            # Using an api to check wether the word exist or not.
        """

        parse = f'https://api.api-ninjas.com/v1/dictionary?word={word}'
        response = req.get(parse, headers={'X-Api-Key': os.getenv("Ninja-Api-Token")})
        json = dict(response.json())

        try:
            if response.status_code != req.codes.ok: raise Exception(response.status_code)

        except Exception as e: return e
        else:

            for i, j in json.items(): 
                if "valid" in i :  json = j

        #   Clear some memory
        del word, parse, response

        return json

class GenerateNames():
        def GenerateRandomNames(self, total):

            """
                Generates only firstnames
                API by RandomUserGenerator
            """

            parse = f'https://randomuser.me/api/?results={total}'
            response = req.get(parse)
            json = response.json()
            string = ""

            try:
                if response.status_code != req.codes.ok:
                    raise Exception(response.status_code)

            except Exception as e: 
                return e

            for i in json['results']:
    
                return i['name']['first']
