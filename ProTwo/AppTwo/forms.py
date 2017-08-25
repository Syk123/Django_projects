from django.forms import ModelForm
from AppTwo.models import User



class FormName(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
