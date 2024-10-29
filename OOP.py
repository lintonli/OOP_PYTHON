class People:
    #create a constructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #create a function that calls the method
    def display_people(self):
        print(f"The boys name is {self.name} and his age is {self.age}")

        #create an instance of the class which is an object
peoples = People("Bob", 30)
peoples.display_people()