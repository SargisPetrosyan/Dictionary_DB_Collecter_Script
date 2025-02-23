from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=50)
    phrases = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return (f"word: {self.word}")
    
class Definition(models.Model):
    word = models.ForeignKey(Word,related_name='definitions', on_delete=models.CASCADE)
    part_of_speech = models.CharField(max_length=50)
    definition = models.CharField(max_length=500)
    
    def __str__(self):
        return (f"word: {self.word.word}: definition: {self.definition}")
    
class Example(models.Model):
    word = models.ForeignKey(Word,related_name='examples', on_delete=models.CASCADE)
    example = models.CharField(max_length=500)
    
    
    def __str__(self):
        return (f"word: {self.word.word}: example: {self.example}")
    
class Synonym(models.Model):
    word = models.ForeignKey(Word,related_name='synonyms', on_delete=models.CASCADE)
    synonym = models.CharField(max_length=50)
    
    def __str__(self):
        return (f"word: {self.word.word}: synonym: {self.synonym}")
    
class Antonym(models.Model):
    word = models.ForeignKey(Word,related_name='antonyms', on_delete=models.CASCADE)
    antonym = models.CharField(max_length=50)
    
    def __str__(self):
        return (f"word: {self.word.word}: example: {self.antonym}")
    
class Phrase(models.Model):
    word = models.ForeignKey(Word,related_name='phrases', on_delete=models.CASCADE)
    phrases = models.CharField(max_length=50)
    
    def __str__(self):
        return (f"word: {self.word.word}: example: {self.phrases}")

class Audio(models.Model):
    word = models.ForeignKey(Word,related_name='audio', on_delete=models.CASCADE)
    title = models.URLField(max_length=200)
    audio_file = models.FileField(upload_to='audio_files/')
    
    def __str__(self):
        return (f"word: {self.word.word}: example: {self.title}")