from django.db import models
from neomodel import (
    StructuredNode,
    StringProperty, 
    IntegerProperty,
    Relationship,
    RelationshipTo,
    RelationshipFrom
)

class Person(StructuredNode):
    uid          = IntegerProperty(unique_index=True)       # Auto-incrementing ID field
    name         = StringProperty(unique_index=True)
    age          = IntegerProperty()
    book_written = RelationshipTo('Book', 'AUTHORED')       # One to many relationship
    profile      = RelationshipTo('Profile', 'HAS_PROFILE') # One to one relationship
    books_read   = Relationship('Book', 'READ')             # Many to many relationship

    def __str__(self):
        return self.name
    
    
    

class Book(StructuredNode):
    uid          = IntegerProperty(unique_index=True)  # Auto-incrementing ID field
    title        = StringProperty()
    genre        = StringProperty()
    publish_year = IntegerProperty()
    author       = RelationshipFrom('Person', 'AUTHORED') # One to many relationship
    readers      = Relationship('Person', 'READ')         # Many to many relationship
    
    def __str__(self):
        return self.title
    
    
    
class Profile(StructuredNode):
    uid     = IntegerProperty(unique_index=True)  # Auto-incrementing ID field
    bio     = StringProperty()
    website = StringProperty()
    person  = Relationship('Person', 'HAS_PROFILE') # One to one relationship
    
    def __str__(self):
        return self.bio
