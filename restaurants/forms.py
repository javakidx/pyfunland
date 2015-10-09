# -*- coding: utf-8 -*-
from django import forms

class CommentForm(forms.Form):
    visitor = forms.CharField(max_length=20, label='留言者')
    email = forms.EmailField(max_length=20, required=False, label='電子郵件')
    content = forms.CharField(max_length=200, widget=forms.Textarea, label='評價')

    def clean_content(self):
        content = self.cleaned_data['content']

        if len(content) < 5:
            raise forms.ValidationError('字數不足')
        
        return content
