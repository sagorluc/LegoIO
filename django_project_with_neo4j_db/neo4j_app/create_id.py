from neo4j_app.models import Person, Book, Profile

def get_next_person_id():
    """
        Returns the next available id for the Person node.
        It queries all existing persons, filters out any None values, 
        and finds the highest id, then increments it.
    """
    # Get all persons and their ids, excluding None values
    ids = [p.uid for p in Person.nodes.all() if p.uid is not None]
    print(ids, 'line 13 (create_id.py)')
    
    if ids:
        # If there are valid IDs, return the next one
        return max(ids) + 1
    else:
        # If no persons exist yet, start with ID 1
        return 1
    
    
def get_next_book_id():
    """
        Returns the next available id for the Person node.
        It queries all existing persons, filters out any None values, 
        and finds the highest id, then increments it.
    """
    # Get all persons and their ids, excluding None values
    ids = [p.uid for p in Book.nodes.all() if p.uid is not None]
    print(ids, 'line 13 (create_id.py)')
    
    if ids:
        # If there are valid IDs, return the next one
        return max(ids) + 1
    else:
        # If no persons exist yet, start with ID 1
        return 1
    
    
def get_next_profile_id():
    """
        Returns the next available id for the Person node.
        It queries all existing persons, filters out any None values, 
        and finds the highest id, then increments it.
    """
    # Get all persons and their ids, excluding None values
    ids = [p.uid for p in Profile.nodes.all() if p.uid is not None]
    print(ids, 'line 13 (create_id.py)')
    
    if ids:
        # If there are valid IDs, return the next one
        return max(ids) + 1
    else:
        # If no persons exist yet, start with ID 1
        return 1
