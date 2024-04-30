from django import forms

class CalculatorForm(forms.Form):
    num1 = forms.FloatField(label='Number 1')
    num2 = forms.FloatField(label='Number 2')
    operation = forms.ChoiceField(choices=(('+', '+'), ('-', '-'), ('*', '*'), ('/', '/')), label='Operation')
