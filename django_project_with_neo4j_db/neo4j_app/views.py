from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person, Book, Profile
from .forms import PersonForm, BookForm, ProfileForm
from .create_id import get_next_person_id, get_next_book_id, get_next_profile_id

def home(request):
    persons = Person.nodes.all()
    books = Book.nodes.all()
    profiles = Profile.nodes.all()
    
    # Create dictionaries to map each person (by uid) to their books
    books_written = {}
    books_read = {}
    
    for person in persons:
        key = person.uid if hasattr(person, 'uid') else person.name
        # Books authored by the person
        books_written[key] = person.book_written.all()  
        # Books read by the person
        books_read[key] = person.books_read.all()        
    
    template = 'home.html'
    context = {
        'persons': persons,
        'books': books,
        'profiles': profiles,
        'books_written': books_written,
        'books_read': books_read
    }
    return render(request, template, context)



def get_people(request):
    # Fetch all people from the Neo4j database
    people = Person.nodes.all()
    people_info = ', '.join([f'{p.name} ({p.age})' for p in people])
    
    return HttpResponse(f"People: {people_info}")

def person_detail_view(request, uid):
    person = Person.nodes.get(uid=uid)
    
    # Fetch related data
    books_written = person.book_written.all()
    books_read = person.books_read.all()
    profile = person.profile.single() if person.profile else None
    
    context = {
        'person': person,
        'books_written': books_written,
        'books_read': books_read,
        'profile': profile
    }
    
    return render(request, 'person_detail.html', context)

# View to create a Person, a Profile (one-to-one), and an authored Book (one-to-many)
def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            uid = get_next_person_id()
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            person = Person(uid=uid, name=name, age=age).save()

            # # Create a profile for the person (one-to-one)
            # bio = form.cleaned_data['bio']
            # website = form.cleaned_data['website']
            # if bio and website:              
            #     profile = Profile(uid=uid, bio=bio, website=website).save()
            #     person.profile.connect(profile)

            # # Create a book authored by the person (one-to-many)
            # book_title = form.cleaned_data['book_title']
            # book_genre = form.cleaned_data['book_genre']
            # book_publish_year = form.cleaned_data['book_publish_year']
            # if book_title and book_genre and book_publish_year:
            #     book = Book(uid=uid,title=book_title, genre=book_genre, publish_year=book_publish_year).save()
            #     person.book_written.connect(book)

            return HttpResponse(f"Person '{person.name}' created successfully!")
    else:
        form = PersonForm()

    return render(request, 'person_form.html', {'form': form})

# View to create a Book and associate it with an author (one-to-many)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            uid = get_next_book_id()
            title = form.cleaned_data['title']
            genre = form.cleaned_data['genre']
            publish_year = form.cleaned_data['publish_year']
            book = Book(uid=uid, title=title, genre=genre, publish_year=publish_year).save()

            # Find the author (person)
            author_name = form.cleaned_data['author_name']
            try:
                author = Person.nodes.get(name=author_name)
                author.book_written.connect(book)
                return HttpResponse(f"Book '{book.title}' by author '{author.name}' created successfully!")
            except Person.DoesNotExist:
                return HttpResponse("Author not found")

    else:
        form = BookForm()

    return render(request, 'book_form.html', {'form': form})

# View to create a Profile and link it to a Person (one-to-one)
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            uid = get_next_profile_id()
            bio = form.cleaned_data['bio']
            website = form.cleaned_data['website']
            profile = Profile(uid=uid, bio=bio, website=website).save()

            # Find the person to link with the profile
            person_name = form.cleaned_data['person_name']
            try:
                person = Person.nodes.get(name=person_name)
                person.profile.connect(profile)
                return HttpResponse(f"Profile for '{person.name}' created successfully!")
            except Person.DoesNotExist:
                return HttpResponse("Person not found")

    else:
        form = ProfileForm()

    return render(request, 'profile_form.html', {'form': form})

