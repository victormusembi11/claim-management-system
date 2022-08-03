from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username', 'email'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control'
                }
            )

    def clean(self) -> dict:
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email', ValidationError('Email address already exists!')
            )
        return super().clean()
