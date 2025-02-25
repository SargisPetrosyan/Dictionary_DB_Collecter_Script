from pydantic import (
    AnyUrl,
    BaseModel,
    ValidationError,
    model_validator,
    Field,
    HttpUrl
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
    
class ExamplesValidator(BaseModel):
    text: str = Field(min_length = 1,  max_length = 500)
    word: str = Field(min_length = 1, max_length = 50)
    
    
class ExampleValidator(BaseModel):
    examples: list[ExamplesValidator]
    
    @model_validator(mode='before')
    def empty_validate(cls, value: dict[list] ) -> list[dict]:
        
        logger.info('checking example empty text before validation')
        
        """Filter out any examples with an empty 'text' field before validation."""
        examples = value.get('examples',[])
        
        # Filter out examples with empty 'text' before passing to validation
        filtered_examples = [ex for ex in examples if ex.get('text')]
        
        value['examples'] = filtered_examples
    
        if not value['examples']:
            logger.error(f"word explanations 'text' are empty or field docent exist")
            raise ValueError("response data has no examples data.")
        
        logger.info(f"examples data validated, examples count: {len(value['examples'])}")   
        return value
    
class DefinitionsValidator(BaseModel):
    text: str = Field(min_length = 1, max_length=50)
    partOfSpeech: str = Field(title='part_of_speech', min_length = 1, max_length=50)
    
    
class DefinitionValidator(BaseModel):
    definitions: list[DefinitionsValidator]
    
    @model_validator(mode='before')
    def empty_validate(cls, value: list[dict] ) -> list[dict]:
        
        logger.info('checking definition empty text before validation')
        
        """Filter out any definition with an empty 'text' field before validation."""
        definition = value.get('definitions',[])
        
        # Filter out examples with empty 'text' before passing to validation
        filtered_definition = [
            i for i in definition if i.get('text') and i.get('partOfSpeech')
        ]
        
        value['definitions'] = filtered_definition
    
        if not value['definitions']:
            logger.error(f"word definition data 'text' are empty or field doesn't exist")
            raise ValueError("response data has no definition data.")
        
        logger.info(f"definition data validated, definition count: {len(value['definitions'])}")   
        return value

class PhrasesValidator(BaseModel):
    gram1: str = Field(min_length = 1, max_length=50)
    gram2: str = Field(min_length = 1, max_length=50)
    count: int 
        
class PhrasesValidator(BaseModel):
    phrases: list[PhrasesValidator]
    
    @model_validator(mode='before')
    def empty_validate(cls, value: list[dict] ) -> dict:
        
        logger.info("checking phrases empty fields before validation")
        
        """Filter out any definition with an empty 'text' field before validation."""
        phrases = value.get('phrases', [])
        
        # Filter out phrases with empty 'text' before passing to validation
        filtered_definition = [
            i for i in phrases if i.get('gram1') and i.get('gram2') and i.get('count')
        ]
        
        value['phrases'] = filtered_definition
    
        if not value['phrases']:
            logger.error(f"word phrases are empty or field doesn't exist")
            raise ValueError("response data has no definition data.")
        
        logger.info(f"phrases data validated, definition count: {len(value['phrases'])}")   
        return value
    
    
class AudiosValidation(BaseModel):
    fileUrl: HttpUrl = Field(title = 'file_url')
    
    
class AudioValidator(BaseModel):
    audios: list[AudiosValidation]

    @model_validator(mode='before')
    def empty_validate(cls, value: dict[list] ) -> dict[list]:
        
        logger.info("checking Audio empty fields before validation")
        
        """Filter out any Audio with an empty 'text' field before validation."""
        audios = value.get('audios', [])
        
        # Filter out phrases with empty 'text' before passing to validation
        filtered_definition = [i for i in audios if i.get('fileUrl')]
        
        value['audios'] = filtered_definition

        if not value['audios']:
            logger.error(f"word fileUrl are empty or field doesn't exist")
            raise ValueError("response data has no url data.")
        
        logger.info(f"url data validated, urls count: {len(value['audios'])}")   
        return value

if __name__=='__main__':
    try:
        # Definition validation
        # wrap definition to response data for model_validate
        definition_wrapped = {'definitions': definition_response }
        definition_validated =DefinitionValidator.model_validate(definition_wrapped) 

        # Phrases validation
        phrases_warped = {'phrases': phrases_response}
        phrases_validated =PhrasesValidator.model_validate(phrases_warped) 
        
        # Examples validation
        examples_validate = ExampleValidator.model_validate(examples_response)
        
        # Audio validation
        audios_warped = {'audios': audio_response}
        audios_validated =AudioValidator.model_validate(audios_warped)

        
        
    except ValidationError as e:
        logger.error(f"validation error {e}")
        pass
    