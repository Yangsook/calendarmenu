from django import forms
from .models import MyCalMenu, MyMenu, MyItem

class MyCalMenuForm(forms.ModelForm):
    class Meta:
        model = MyCalMenu
        # fields = '__all__'
        fields = ['userid', 'day', 'menuid']
        labels = {
            'menuid' : '메뉴선택'
        }
        widgets = {
            'userid': forms.HiddenInput(),
            'day': forms.HiddenInput(),
            
        }
    def __init__(self, *args, **kwargs):
        super(MyCalMenuForm, self).__init__(*args, **kwargs)
        self.fields['menuid'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "메뉴를 선택해 주세요"
        }

class MyMenuForm1(forms.ModelForm):
    class Meta:
        model = MyMenu
        # fields = '__all__'
        fields = ['userid', 'menu', 'category']
        widgets = { 'userid': forms.HiddenInput() }

    def __init__(self, *args, **kwargs):
        super(MyMenuForm1, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "카테고리를 선택해 주세요"
        }

class MyMenuForm(forms.ModelForm):
    class Meta:
        model = MyMenu
        # fields = '__all__'
        fields = ['userid', 'menu', 'category', 'note']
        widgets = { 'userid': forms.HiddenInput() }        

    def __init__(self, *args, **kwargs):
        super(MyMenuForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "카테고리를 선택해 주세요"
        }

class MyItemForm(forms.ModelForm):
    class Meta:
        model = MyItem
        # fields = '__all__'
        fields = ['userid', 'item', 'category']    
        widgets = { 'userid': forms.HiddenInput() }  

    def __init__(self, *args, **kwargs):
        super(MyItemForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "카테고리를 선택해 주세요"
        }