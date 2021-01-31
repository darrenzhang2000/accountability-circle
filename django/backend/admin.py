from django.contrib import admin
from .models import User, Feedback, Partnership, WeeklyGoals, Mission
# Register your models here.
admin.site.register(User)
admin.site.register(Feedback)
admin.site.register(Partnership)
admin.site.register(WeeklyGoals)
admin.site.register(Mission)
