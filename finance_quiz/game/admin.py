from django.contrib import admin
from .models import User, Question, Options, Ranking

# Register your models here.
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Options)
admin.site.register(Ranking)
