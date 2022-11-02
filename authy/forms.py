from django import forms
from authy.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EditProfileForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}),
                                 required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}),
                                required=True)
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Bio'}), required=True)
    url = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'URL'}), required=True)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Address'}),
                               required=True)

    locationY = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'locationY'}),
                                required=True)
    locationX = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'locationX'}),
                                required=True)
    serch = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'serch'}),
                               required=True)





    im_on = forms.BooleanField(label=forms.RadioSelect(attrs={'class': 'input', 'placeholder': 'im_on'}), required=False)

    castmr_on = forms.BooleanField(label=forms.RadioSelect(attrs={'class': 'input', 'placeholder': 'castmr_on'}), required=False)




    t = forms.BooleanField(label=forms.RadioSelect(attrs={'class': 'input', 'placeholder': 't'}), required=False)

    w = forms.BooleanField(label=forms.RadioSelect(attrs={'class': 'input', 'placeholder': 'w'}), required=False)
    g = forms.BooleanField(label=forms.RadioSelect(attrs={'class': 'input', 'placeholder': 'g'}), required=False)
    b = forms.BooleanField(label=forms.RadioSelect(attrs={'class': 'input', 'placeholder': 'b'}), required=False)
    a = forms.BooleanField(label=forms.RadioSelect(attrs={'class': 'input', 'placeholder': 'a'}), required=False)




    class Meta:
        model = Profile
        fields = ['image', 'first_name', 'last_name', 'bio', 'url', 'location' , 'locationY'  , 't', 'w', 'g', 'b' , 'a' , 'locationX' , 'im_on', 'castmr_on', 'serch'  ]


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'prompt srch_explore'}), max_length=50,
        required=True)
    # username = forms.EmailInput(widget=forms.TextInput(attrs={'placeholder': 'Username'}), max_length=50, required=True)

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'prompt srch_explore'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'prompt srch_explore'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'prompt srch_explore'}))

    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
