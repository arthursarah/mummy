class person():
    def __init__(self,name,DOB,speak,walk,age):
        self.name = name
        self.DOB = DOB
        self.speak = speak
        self.walk = walk
        self.age = age
    def get_name(self):
        return self.name
    def get_DOB(self):
        return self.DOB
    def get_speak(self):
        return self.speak
    def get_walk(self):
        return self.walk
    def get_age(self):
        return self.age
              
       
bb=person("sarah","9/9/2001","hello","walking away","17")
print(bb.get_name())
print(bb.get_DOB())
print(bb.get_speak())
print(bb.get_walk())
print(bb.get_age())