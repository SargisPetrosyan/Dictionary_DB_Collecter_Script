from django.contrib import admin
from words_collector.models import Word,Definition,Example,Phrase,Antonym,Synonym

admin.site.register(Word)
admin.site.register(Definition)
admin.site.register(Example)
admin.site.register(Phrase)
admin.site.register(Antonym)
admin.site.register(Synonym)