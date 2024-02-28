from django.contrib import admin

from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
# class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        ("Question Information", {"fields": ["question_text"]}),
        # (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

# class ChoiceAdmin(admin.ModelAdmin):
#     fields = ['choice_text', 'question', 'votes']
#     # pass


# Register your models here.
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceAdmin)
