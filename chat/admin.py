from django.contrib import admin
from .models import Chat
# Register your models here.
class ChatAdmin(admin.ModelAdmin):
	list_display = ['usuario', 'mensagem', 'data_registro']
	
admin.site.register(Chat, ChatAdmin)	

