import logging
from word_requests import GetWord


#create logger
logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('cache_log.log')

formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formater)

logger.addHandler(file_handler)

file_name ='3000 most common words in English.txt'

# open file go trough each lien 
def get_word(file_name: str) :
    with open(file_name, 'r') as file:
        for line in file:
            yield line.strip()

# call get_word() to get 1 word each time             
def get_word():        
    for word in get_word(file_name=file_name):
        return word




    
    

    
    


            
