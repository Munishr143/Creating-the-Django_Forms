from django import forms

g=[['MALE', 'MALE'], ['FEMALE','FEMALE']]
c=[['PYTHON', 'PYTHON'], ['SQL', 'SQL'], ['DJANGO', 'DJANGO']]

class StudentForm(forms.Form):
    name=forms.CharField(max_length=30)
    age=forms.IntegerField()
    email=forms.EmailField()
    date=forms.DateTimeField()
    password=forms.CharField(max_length=30, widget=forms.PasswordInput)
    address=forms.CharField(max_length=500, widget=forms.Textarea(attrs={'cols':20, 'rows': 3}))
    # gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g, widget=forms.RadioSelect)
    # course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c, widget=forms.CheckboxSelectMultiple)