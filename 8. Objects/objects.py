class Person:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"My name is {self.name}")

person1 = Person("Richard").speak()