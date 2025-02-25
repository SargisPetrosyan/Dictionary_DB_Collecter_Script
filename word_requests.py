import httpx

from validation import Validator

import logging

API_KEY = 'baw9pp5ghw4ffoewy3ovzfjnvdh4cco2eud5qcx6zcfx2218i'
BASE_URL = 'https://api.wordnik.com/v4'

logger = logging.getLogger("__name__")

class GetWord:
    @staticmethod
    def fetch_data(url: str, params: dict) -> dict:
        """Helper function to make a GET request and return the response data."""
        try:
            with httpx.Client() as client:
                response = client.get(url, params=params)
                response.raise_for_status()
                logger.info(f"word request code is 200 DONE SUCCESSFUL!!!")
                return response.json()
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP {e.response.status_code}: {e.response.text}")
            return {'error': f"HTTP {e.response.status_code}: {e.response.text}"}
        except httpx.RequestError as e:
            logger.error(f"Request failed: {e}")
            return{"error": f"Request failed: {e}"}
        
    @staticmethod
    def get_word_definitions(word: str) -> list[dict]:
        url = f"{BASE_URL}/word.json/{word}/definitions"

        logger.info(f"word '{word}' request")
        # request settings
        params = {
        'limit': 20,
        'includeRelated': 'false',
        'useCanonical': 'true',
        'includeTags': 'false',
        'api_key': API_KEY
        }
        
        # GetWord function handling request with error
        definition_response = GetWord.fetch_data(url=url,params=params)

        logger.info(f"word '{word}' validation started")
        
        # validation definition
        validation = Validator.definition_validator(definition_response)

        return validation
    
    @staticmethod
    def get_word_audio(word: str) -> list[dict]:
        url = f"{BASE_URL}/word.json/{word}/definitions"

        # request settings
        params = {
        'limit': 5,
        'useCanonical': 'true',
        'api_key': API_KEY
        }

        return GetWord.fetch_data(url=url,params=params)


    @staticmethod
    def get_word_examples(word: str, top_example: bool)-> dict:
        '''Get word examples'''
        url = f"{BASE_URL}/word.json/{word}/examples"

        params = {
        'limit': 20,
        'includeRelated': 'false',
        'useCanonical': 'true',
        'includeTags': 'false',
        'api_key': API_KEY
        }

        return GetWord.fetch_data(url=url,params=params)
    
    @staticmethod
    def get_word_audio(word: str) -> list[dict]:
        url = f"{BASE_URL}/word.json/{word}/definitions"

        # request settings
        params = {
        'limit': 20,
        'useCanonical': 'true',
        'api_key': API_KEY
        }

        return GetWord.fetch_data(url=url,params=params)


if __name__=='__main__':
    GetWord.get_word_definitions(word='apple')