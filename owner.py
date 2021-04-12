class Owner:
    """
    Attributes:
        name: str
            Name of the person
        rut: str
            National identification number
        dogs: list<Dog>
            List of dogs
    """
    def __init__(self, name, rut, dogs):
        self.name = name
        self.rut = rut
        self.dogs = dogs 

    def add_dog(self, dog):
        self.dogs.append(dog)

    def remove_dog(self, dog_name, dog_date_of_birth, dog_breed):
        for dog in self.dogs:
            if (
                dog.name==dog_name and
                dog.date_of_birth==dog_date_of_birth and
                dog.breed == dog_breed
            ):
                self.dogs.remove(dog)