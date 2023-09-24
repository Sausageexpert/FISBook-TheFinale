from django.contrib import admin
from .models import Forum,Events,Notices,JoinReq

# Register your models here.

admin.site.register(Forum)
admin.site.register(Events)
admin.site.register(Notices)
admin.site.register(JoinReq)