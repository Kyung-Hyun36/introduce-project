from django.forms import ModelForm
from django import forms
from introduce.models import People
from django.utils.translation import gettext_lazy as _

GENDER_CHOICES = (
    ('남자', '남자'),
    ('여자', '여자'),
)


class PeopleForm(ModelForm):
    class Meta:
        model = People
        fields = ['name', 'gender', 'age', 'address', 'job', 'cellphone',
                  'email', 'hobby', 'image', 'password']
        labels = {
            'name': _('이름'),
            'gender': _('성별'),
            'age': _('나이'),
            'address': _('주소'),
            'job': _('직업'),
            'cellphone': _('전화번호'),
            'email': _('E-mail'),
            'hobby': _('취미'),
            'image': _('사진'),
            'password': _('비밀번호'),
        }
        widgets = {
            'password': forms.PasswordInput(),
            'gender': forms.Select(choices=GENDER_CHOICES),
        }


class UpdatePeopleForm(PeopleForm):
    class Meta:
        model = People
        exclude = ['password']
