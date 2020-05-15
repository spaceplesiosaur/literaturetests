from django.contrib import admin
from .models import Source, Character, Quiz, CharacterDescription, Question, Answer

admin.site.register(Source)
admin.site.register(Character)
admin.site.register(Quiz)
admin.site.register(CharacterDescription)
admin.site.register(Question)
admin.site.register(Answer)
