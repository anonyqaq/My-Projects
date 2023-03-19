from users import models
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from users.utils.BootStrap import BootStrapModelForm
from users.utils.encrypt import md5

class UserModelForm(BootStrapModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart"]

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     for name, field in self.fields.items():
        #         field.widget.attrs = {"class": "form-control", "placeholder": field.label}


class PrettyModelForm(BootStrapModelForm):
    moblie = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ],
    )

    class Meta:
        model = models.PrettyNum
        fields = ["moblie", "price", "level", "status"]

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     for name, field in self.fields.itmes():
        #         field.widget.attrs = {"class": "form-control"}


class AdminModelForm(BootStrapModelForm):
    configparser_upassword = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput
    )

    class Meta:
        model = models.Admin
        fields = ["username", "upassword", "configparser_upassword"]
        widgets = {
            "upassword": forms.PasswordInput
        }

    def clean_upassword(self):
        pwd = self.cleaned_data.get("upassword")
        return md5(pwd)

    def clean_configparser_upassword(self):
        pwd = self.cleaned_data.get("upassword")
        confirm = md5(self.cleaned_data.get("configparser_upassword"))
        if pwd != confirm:
            raise ValidationError("密码不一致")

        return confirm


class AdminEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ['username']





