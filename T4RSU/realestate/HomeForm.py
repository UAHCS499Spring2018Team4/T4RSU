#!/usr/bin/env python3
# encoding=utf-8

from django import forms

class HomeForm(forms.Form):
    post = forms.CharField()
