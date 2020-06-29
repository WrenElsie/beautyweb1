from django.forms import ModelForm,  TextInput, URLInput, ClearableFileInput
from .models import Beauty, Good

class BeautyForm(ModelForm):
    class Meta:
        model = Beauty
        exclude = ('user', 'date',)

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'telephone': TextInput(attrs={'class': 'form-control'}),
            'url': URLInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': '名称',
            'address': '地址',
            'telephone': '电话',
            'url': '网站',
        }


class GoodForm(ModelForm):
    class Meta:
        model = Good
        exclude = ('user', 'date', 'beauty',)

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': TextInput(attrs={'class': 'form-control'}),
            'price': TextInput(attrs={'class': 'form-control'}),
            'image': ClearableFileInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': '商品名',
            'description': '描述',
            'price': '价格(元)',
            'image': '图片',
        }

