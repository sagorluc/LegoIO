from django.urls import path
from neo4j_app.views import(
    home,
    create_book,
    create_person,
    create_profile,
    get_people,
    person_detail_view,
)

urlpatterns = [
    path('', home, name='home'),
    path('create_person/', create_person, name='person'),
    path('create_book/', create_book, name='book'),
    path('create_profile/', create_profile, name='profile'),
    
    # Fatch data
    path('people/', get_people, name='people'),
    path('person_details/<int:uid>/', person_detail_view, name='person_details'),
]
