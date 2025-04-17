from django.contrib import admin
from .models import Conversation

# Register your models here.
admin.site.register(Conversation)

class ConversationAdmin(admin.ModelAdmin):
    list_display = ('user_input', 'response', 'timestamp')
    search_fields = ('user_input', 'response')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)