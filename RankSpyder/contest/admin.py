from django.contrib import admin

# Register your models here.

from .models import Contest, Submition, Rank

class ContestAdmin(admin.ModelAdmin):
    list_display = ('id', 'contestId', 'contestName','platform', 'problemNum', 'hint') # list
class SubmitionAdmin(admin.ModelAdmin):
    list_display = ('localContestId', 'userId', 'problemId', 'submitTime', 'status')
class RankAdmin(admin.ModelAdmin):
    list_display = ('localContestId', 'userId', 'ac', 'rank')

admin.site.register(Contest, ContestAdmin)
admin.site.register(Submition, SubmitionAdmin)
admin.site.register(Rank, RankAdmin)
