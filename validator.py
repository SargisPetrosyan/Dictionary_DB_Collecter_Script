from pydantic import (
    AnyUrl,
    BaseModel,
    ValidationError,
    model_validator,
    Field
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
    text: str = Field(min_length = 1)
    word: str = Field(min_length = 1, max_length = 50)
    
    
class ExampleValidator(BaseModel):
    examples: list[ExamplesValidator]
    
    @model_validator(mode='before')
    def empty_validate(cls, value: dict[list] ) -> dict[list]:
        
        logger.info('checking empty text before validation')
        
        """Filter out any examples with an empty 'text' field before validation."""
        examples = value.get('examples',[])
        
        # Filter out examples with empty 'text' before passing to validation
        filtered_examples = [ex for ex in examples if ex.get('text')]
        
        value['examples'] = filtered_examples
    
        if not value['examples']:
            logger.error(f"word: has no explanation data")
            raise ValueError("response data has no examples data.")
        
        logger.info(f"examples validated, examples count: {len(value['examples'])}")   
        return value
    
class DefinitionsValidator(BaseModel):
    text: str = Field(min_length = 1)
    partOfSpeech: str = Field(min_length = 1)
    
class DefinitionValidator(BaseModel):
    definitions: list[DefinitionsValidator]
    
    @model_validator(mode='before')
    def empty_validate(cls, value: dict[list] ) -> dict[list]:
        
        logger.info('checking empty text before validation')
        
        """Filter out any definition with an empty 'text' field before validation."""
        definition = value.get('definition',[])
        
        # Filter out examples with empty 'text' before passing to validation
        filtered_definition = [i for i in definition if i.get('text')]
        
        value['definition'] = filtered_definition
    
        if not value['definition']:
            logger.error(f"word: has no explanation data")
            raise ValueError("response data has no definition data.")
        
        logger.info(f"definition validated, definition count: {len(value['definition'])}")   
        return value
    
    
if __name__=='__main__':
    try:
        definition_wrapped = {'definitions': definition_response }
        definition_validated =DefinitionValidator.model_validate(definition_wrapped) 
        print(definition_validated)
        
        # examples_validate = ExampleValidator.model_validate(examples_response)
        # print(examples_validate)
        
        
    except ValidationError as e:
        logger.error(f"validation error {e}")
        pass
    