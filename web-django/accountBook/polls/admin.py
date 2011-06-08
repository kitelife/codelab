from polls.models import Poll
from polls.models import Choice

from django.contrib import admin

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

#admin.site.register(Poll)
class PollAdmin(admin.ModelAdmin):
	#fields = ['pub_state','question']
	fieldsets = [
			(None,{'fields':['question']}),
			('Date information',{'fields':['pub_state'],'classes':['collapse']}),
			]
	inlines = [ChoiceInline]

	list_display = ('question','pub_state','was_published_today')

	list_filter = ['pub_state']
	search_fields = ['question']
	date_hierarchy = 'pub_state'

admin.site.register(Poll,PollAdmin)
#admin.site.register(Choice)
