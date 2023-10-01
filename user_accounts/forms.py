from django import forms
from .models import Profile
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm




STATE_CHOICES = [
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal')
]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        
        name = forms.CharField(max_length=100, label="Name", required=True)
        state = forms.ChoiceField(choices=STATE_CHOICES, label="State")
        city = forms.CharField(max_length=100, required=True, label="City")
        landmark = forms.CharField(max_length=100, label="Landmark", required=True)
        phone = forms.IntegerField(required=True, label="Contact")
        pincode = forms.CharField( required=True, label="Pincode")      
        profile_pic = forms.ImageField(required=True, label="Profile")

        fields = ('name', 'state', 'city', 'landmark', 'phone', 'pincode', 'profile_pic')
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'autofocus':'True'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'landmark': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'pincode': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        

class ForgotPasswordForm(PasswordResetForm):
    email = forms.EmailField(max_length=100, label = "Email", widget = forms.EmailInput(attrs={'class': 'form-control', 'autofocus':'True'}))
  
    

class NewPasswordForm(SetPasswordForm):
  
    
    new_password1 = forms.CharField(max_length=100, label="New Password",widget= forms.PasswordInput(attrs={'class': 'form-control', 'autofocus':'True'}))
    new_password2 = forms.CharField(max_length=100, label="Confirm Password",widget= forms.PasswordInput(attrs={'class': 'form-control', 'autofocus':'True'}))
    
    fields = ['new_password1', 'new_password2']
    