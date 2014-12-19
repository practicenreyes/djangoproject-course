from django.contrib import admin
from polls.models import Choice, Question

# Register your models here.

class ChoiceInline(admin.TabularInline):
	'''
	    Tabular Inline View for Choice
	'''
	model = Choice
	min_num = 3
	max_num = 10
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
    '''
        Admin View for Question
    '''
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ('pub_date',)
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)