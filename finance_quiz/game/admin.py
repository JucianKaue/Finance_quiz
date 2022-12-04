from django.contrib import admin
from .models import User, Question, Ranking

# Register your models here.
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Ranking)
