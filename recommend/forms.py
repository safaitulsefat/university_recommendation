from django import forms

class RecommendationForm(forms.Form):
    DEPARTMENT_CHOICES = [
        ('CSE', 'CSE'),
        ('EEE', 'EEE'),
    ]

    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    cost = forms.IntegerField()
    gpa = forms.FloatField()
