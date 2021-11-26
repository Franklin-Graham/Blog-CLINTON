from django.contrib import admin
from .models import Detail,Telegram_project,Github_project,Account,File
# Register your models here.
admin.site.register(Detail)
admin.site.register(Telegram_project)
admin.site.register(Github_project)
admin.site.register(Account)
admin.site.register(File)