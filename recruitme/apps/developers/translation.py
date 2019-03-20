from modeltranslation.translator import translator, TranslationOptions
from .models import Developer

class DeveloperTranslationOptions(TranslationOptions):
    fields = ('bio',)

translator.register(Developer, DeveloperTranslationOptions)