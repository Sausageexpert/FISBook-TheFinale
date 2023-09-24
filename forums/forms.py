from .models import Events,Notices, Forum
from django import forms

class ScheduleForm(forms.ModelForm):
    class Meta():
        model = Events
        fields = ['forum', 'title', 'about', 'date', 'is_public', 'users_added']
        
class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notices
        fields = ['forum','title','about']
        
class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['name','about','is_public','pic']