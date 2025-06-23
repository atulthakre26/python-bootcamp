class Animal:
    def speak(self):
        print("Animal Speak")


class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.bark()
d.speak()