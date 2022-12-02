from django import forms
from .models import signupuser,adduser


class signupForm(forms.ModelForm):
    class Meta:
        model=signupuser
        fields='__all__'



class adduserForm(forms.ModelForm):
    SUB_SEL=(
        ('python','python'),
        ('java','java'),
        ('php','php'),
        ('.c++','.c++'),
        ('c','c'),
    )
    subject=forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=SUB_SEL
    )

    GEN_SEL=(
        ('male','male'),
        ('female','female'),
    )

    gender=forms.CharField(
        widget=forms.RadioSelect(choices=GEN_SEL)
    )
    
    class Meta:
        model=adduser
        fields=['name','email','gender','subject','address','city']