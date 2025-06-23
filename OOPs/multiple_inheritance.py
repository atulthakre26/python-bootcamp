class Father:
    def is_father(self):
        print("this is a father class")

class Mother:
    def is_mother(self):
        print("this is a mother class")

class Child(Father, Mother):
    def is_child(self):
        print("this is a child class")

c = Child()
c.is_father()
c.is_mother()
c.is_child()