from pydantic import (
    AnyUrl,
    BaseModel,
    model_validator
    ValueError
) 

from json_examples import (
    examples_response, phrases_response, definition_response, audio_response
    )

import logging

# create logger
logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)

#create stream logging
stream =logging.StreamHandler()
formater = logging.Formatter('%(levelname)s - %(message)s')

# register handler
stream.setFormatter(formater)
logger.addHandler(stream)


class WordValidator(BaseModel):
    text: str | None = None
     
# class DefinitionValidator(BaseModel):
#     text: str | None = None
#     partOfSpeech: str | None = None
    
#     @model_validator(mode='before')
#     def check_model_structure(cls, value):
#         if 'text' not in value or 'partOfSpeech' not in value:
#             return None
        
#         if not isinstance(
#             value.get('text', ''), str) or \
#             not isinstance(value.get('partOfSpeech', ''), str):
#             return None 
        
class ExamplesValidator(BaseModel):
    text: str | None = None
    
    
class PhraseValidator(BaseModel):
    gram1: str | None = None
    gram2: str | None = None
    
    
class ExampleValidator(BaseModel):
    examples: list[ExamplesValidator] | None

    
class AudioValidator(BaseModel):
    fileUrl: AnyUrl | None = None
    
class SynonymValidator(BaseModel):
    text: str
 
class AntonymValidator(BaseModel):
    text: str


if __name__=='__main__':
    
    # for example in examples_response:
    #     result = ExampleValidator(**example)
    #     print(result)
    #     break
    
    # for definition in definition_response:
    #     result = DefinitionValidator(**definition)
    #     print(result)
    
    # for audio in audio_response:
    #     result = AudioValidator(**audio)
    #     print(result)

    
    for phrases in phrases_response:
        result = PhraseValidator(**phrases)
        print(result)