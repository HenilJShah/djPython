from django import forms

from .models import RegisterUser

class StuUser(forms.ModelForm):
    class Meta:
        model = RegisterUser
        fields = ['stu', 'email']


# model save bt form inheritance
class StaffUser(StuUser):
    class Meta(StuUser.Meta):
        fields = ['staff', 'email']