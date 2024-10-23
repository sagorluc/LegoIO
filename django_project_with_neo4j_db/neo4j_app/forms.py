from django import forms
from .models import Person, Book, Profile
# Form for creating a Person
class PersonForm(forms.Form): 
    name = forms.CharField(max_length=100)
    age  = forms.IntegerField()
    
# Form for creating a Book
class BookForm(forms.Form):     
    title        = forms.CharField(max_length=200)
    genre        = forms.CharField(max_length=100)
    publish_year = forms.IntegerField()
    
    # Field to select the author (Person) for one-to-many relationship
    author_name  = forms.CharField(max_length=100)


# Form for creating a Profile
class ProfileForm(forms.Form):    
    bio     = forms.CharField(max_length=300)
    website = forms.URLField()
    
    # Field to link profile to a person (one-to-one relationship)
    person_name = forms.CharField(max_length=100)
