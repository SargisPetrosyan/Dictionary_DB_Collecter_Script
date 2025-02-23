from pydantic import BaseModel, field_validator,HttpUrl

from .json_examples import (
    examples_response, phrases_response, definition_response, audio_response
    )

import logging

# create logger
logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)

#create stream logging
stream =logging.StreamHandler()
formater = logging.Formatter('%(levelname)s - %(name)s - %(message)s')

# register handler
stream.setFormatter(formater)
logger.addHandler(stream)


class WordValidator(BaseModel):
    text: str | None
     
class DefinitionValidator(BaseModel):
    text: str | None
    partOfSpeech: str | None
    
    @field_validator('text',mode='before')
    def save_not_empty(cls,definitions):
        if definitions and definitions.strip():
            logger.info(f"filed is not empty ")
            return definitions.strip()
        
        logger.info(f"filed is empty")
        return None
        
class ExamplesValidator(BaseModel):
    text: str | None
    
    @field_validator('text',mode='before')
    def save_not_empty(cls,examples):
        if examples and examples.strip():
            logger.info(f"filed is not empty") 
            return examples.strip()
        
        logger.info(f"filed is empty")
        return None
    
class PhraseValidator(BaseModel):
    gram1: str | None
    gram2: str | None
    
    @field_validator('gram1','gram2', mode='before')
    def save_not_empty(cls,phrases):
        if phrases and phrases.strip():
            logger.info(f"filed is not empty ")
            return phrases.strip()
        
        logger.info(f"filed is empty ")
        return None
     

class ExampleValidator(BaseModel):
    text: list[ExamplesValidator] | None

    
class AudioValidator(BaseModel):
    fileUrl: HttpUrl | None
    
    @field_validator('fileUrl',mode='before')
    def save_not_empty(cls,examples):
        if examples and examples.strip(): 
            logger.info(f"filed is not empty ")
            return examples.strip()
        return None


class SynonymValidator(BaseModel):
    text: str

    
class AntonymValidator(BaseModel):
    text: str


if __name__=='__main__':
    
    examples = ExampleValidator(**examples_response)
    print(examples)
    definition = DefinitionValidator(**definition_response)
    print(definition)
    audio = AudioValidator(**audio_response)
    phrases = PhraseValidator(**phrases_response)
    

    





 
