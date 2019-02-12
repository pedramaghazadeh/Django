from django import forms
from .models import Product
from PIL import Image
from django.contrib.auth import authenticate, get_user_model, login, logout
User = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user     = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("This user does not exist")
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect password")
        if not user.is_active:
            raise forms.ValidationError("This user is not longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class ProductForm(forms.ModelForm):
    img         = forms.ImageField(label='Image')
    crop_up     = forms.IntegerField(required=False, label='X coordinate of upper left point')
    crop_left   = forms.IntegerField(required=False, label='Y coordinate of upper left point')
    crop_low    = forms.IntegerField(required=False, label='X coordinate of lower right point')
    crop_right  = forms.IntegerField(required=False, label='Y coordinate of lower right point')
    resize_x    = forms.IntegerField(required=False, label='X coordinate size')
    resize_y    = forms.IntegerField(required=False, label='Y coordinate size')
    rotate      = forms.DecimalField(required=False, label='Degree of rotation')
    bw          = forms.BooleanField(required=False, label='Black or White')
    class Meta:
        model  = Product
        fields = ['img', 'crop_up', 'crop_left', 'crop_low', 'crop_right', 'resize_x', 'resize_y', 'rotate', 'bw', 'share']



