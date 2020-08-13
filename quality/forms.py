from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from datetime import date


class Factclaimcases_input(forms.ModelForm):
    class Meta:
        model = Factclaimcases
        fields = ("idfactclaimcase", "idtechnican", "thedate", "manufacturedef", "description",)


class Dimtestprocedure_input(forms.ModelForm):
    class Meta:
        model = Dimtestprocedure
        fields = ("idtestprocedure", "idproductfamilly", "idtechnican", "date", "description",)


class Corrective_input(forms.ModelForm):
    correctiveactiondoc = forms.FileField()
    class Meta:
        model = Factclaimcases
        fields = ('correctiveactiondoc',)
